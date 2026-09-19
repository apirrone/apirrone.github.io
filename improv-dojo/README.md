# Improv Dojo

A personal PWA that hands you a different, hard improvisation workout every day. Same shape as
*One More Time*: one `index.html` (inline CSS + JS, no build step, no dependencies), a `manifest.json`,
a network-first `sw.js` for offline use, and PNG icons rendered from `icon.svg`. No server, no LLM,
no accounts: everything runs in the browser and state lives in `localStorage`.

## What a session looks like

The generator is seeded by the date, so today's session is stable until you hit **Reroll**.
Each block has a time budget, a **Done** button and a rating (*too easy / just right / too hard*)
that moves your level (1–10). The level gates every pool: scales, progressions, rhythm cells,
constraint cards, ear-training sets, lick length and technique density.

| Block | What you get |
|---|---|
| Warm-up | Scale of the day (34 scales, from pentatonics to altered, bebop, augmented, Hungarian minor) on a fretboard diagram, two pattern drills, playback |
| Ear | Intervals, chord qualities, scale degrees over a drone, melodic dictation in today's scale, progression recognition |
| Vocabulary | A generated 2-bar lick in tab, built from the scale that fits the day's main chord, ending on a chord tone; play it back, transpose to 3 keys, mutate it |
| Rhythm | One rhythmic cell (step grid, playable) or an odd meter; improvise using only that cell |
| Harmony | A progression in a random key (blues, ii–V–I, rhythm changes, Coltrane changes, backdoor, sus-b9 vamps…), a synthesized backing track in swing / straight / funk / ballad / pad / drone, and a chord → tones / guide tones / scale table |
| Free improv | Three constraint cards over the same backing |
| Listen & steal | A player and a specific thing to transcribe, then save to the Vault |
| Motif lab | A 3-note motif with a rhythm, developed with named transformations |

Session length (4, 6 or 8 blocks) and a focus (jazz, blues, modal, rhythm, ear) are in **More**.

Other tabs:

- **Ear**: unlimited drills with all-time accuracy per category.
- **Jam**: any progression in any key with the backing track, a scale explorer on the fretboard, and a metronome with odd meters, subdivisions and "drop the click" modes.
- **Vault**: your licks (tab or text). Spaced repetition (1, 3, 7, 14, 30, 60, 120 days); due licks show up in the daily Vocabulary block with new keys to play them in.
- **More**: practice heatmap, level override, session settings, JSON export/import.

## Run locally

```sh
python3 -m http.server 8000
# open http://localhost:8000
```

Any static file server works. Audio needs a user gesture on iOS: tap a play button once.

## Deploy

The app is static, so any static host works. GitHub Pages recipe:

```sh
git init && git add . && git commit -m "Improv Dojo"
gh repo create improv-dojo --public --source=. --push
gh api -X POST repos/{owner}/improv-dojo/pages -f build_type=legacy -f "source[branch]=main" -f "source[path]=/"
```

Then open the Pages URL on your phone and **Add to Home Screen**. `sw.js` is network-first for
the app's own files, so a redeploy is picked up on the next launch; bump `CACHE` in `sw.js`
when you change the shell file list.

## Regenerate icons

```sh
inkscape icon.svg -w 512 -h 512 -o icon-512.png
inkscape icon.svg -w 192 -h 192 -o icon-192.png
inkscape icon.svg -w 180 -h 180 -o apple-touch-icon.png
```
