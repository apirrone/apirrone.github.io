#!/usr/bin/env python3
"""Self-hosted audio extractor for the One More Time practice app.

Serves GET /audio?v=VIDEOID -> audio bytes (m4a/webm), CORS enabled, so the
app's "Get HQ audio" button can fetch reliably. Run it on any machine the
phone/browser can reach (LAN IP, Tailscale, VPS...), then paste its URL in
the app's Advanced panel (e.g. http://192.168.1.10:8991).

Usage:
    pip install yt-dlp
    python3 audio_server.py [port]

Note: fetching YouTube content this way is against YouTube's Terms of
Service; run it for your own personal practice at your own discretion.
"""
import http.server
import os
import re
import sys
import tempfile

import yt_dlp

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8991
MIME = {".m4a": "audio/mp4", ".mp4": "audio/mp4", ".webm": "audio/webm",
        ".opus": "audio/ogg", ".mp3": "audio/mpeg"}


def download_audio(video_id, tmpdir):
    opts = {
        "format": "bestaudio[ext=m4a]/bestaudio",
        "outtmpl": os.path.join(tmpdir, "audio.%(ext)s"),
        "quiet": True,
        "no_warnings": True,
        "noplaylist": True,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=True)
    for name in os.listdir(tmpdir):
        if name.startswith("audio."):
            return os.path.join(tmpdir, name)
    return None


class Handler(http.server.BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.end_headers()

    def do_GET(self):
        m = re.fullmatch(r"/audio\?v=([\w-]{11})", self.path)
        if not m:
            self.send_response(404)
            self._cors()
            self.end_headers()
            return
        video_id = m.group(1)
        print(f"fetching {video_id} ...")
        try:
            with tempfile.TemporaryDirectory() as tmp:
                path = download_audio(video_id, tmp)
                if not path:
                    raise RuntimeError("yt-dlp produced no file")
                with open(path, "rb") as f:
                    data = f.read()
                mime = MIME.get(os.path.splitext(path)[1], "application/octet-stream")
            self.send_response(200)
            self._cors()
            self.send_header("Content-Type", mime)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            print(f"served {video_id}: {len(data)} bytes ({mime})")
        except Exception as e:
            print(f"error for {video_id}: {e}")
            self.send_response(500)
            self._cors()
            self.end_headers()


if __name__ == "__main__":
    print(f"One More Time audio extractor on http://0.0.0.0:{PORT}")
    print(f"endpoint: GET /audio?v=VIDEOID")
    http.server.ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
