import numpy as np
from scipy.cluster.vq import kmeans2, whiten
import matplotlib.pyplot as plt
import math

places ={
    "Musee des sciences" : {"coords" : [51.497987, -0.174573], "closest" : "aze"},
    "Abbey road" : {"coords" : [51.536051, -0.184107], "closest" : "aze"},
    "Hamleys Magasin de jouets" : {"coords" : [51.513554, -0.139956], "closest" : "aze"},
    "British museum" : {"coords" : [51.519573, -0.126946], "closest" : "aze"},
    "Borough market" : {"coords" : [51.505625, -0.091010], "closest" : "aze"},
    "Camden town" : {"coords" : [51.540834, -0.148392], "closest" : "aze"},
    "natural history museum" : {"coords" : [51.496880, -0.176401], "closest" : "aze"},
    "Brick lane market" : {"coords" : [51.521367, -0.071880], "closest" : "aze"},
    "Tour de Londres" : {"coords" : [51.508306, -0.075896], "closest" : "aze"},
    "Sky garden" : {"coords" : [51.511453, -0.083584], "closest" : "aze"},
    "Hms Belfast" : {"coords" : [51.506786, -0.081368], "closest" : "aze"},
    "Tower bridge" : {"coords" : [51.505603, -0.075346], "closest" : "aze"},
    "London’s nose" : {"coords" : [51.506963, -0.128615], "closest" : "aze"},
    "Old operating museum" : {"coords" : [51.505142, -0.088588], "closest" : "aze"},
    "Wellcome collection" : {"coords" : [51.526173, -0.134002], "closest" : "aze"},
    "Grant museum of zoology" : {"coords" : [51.523766, -0.134658], "closest" : "aze"},
    "Cyberdog" : {"coords" : [51.542383, -0.147534], "closest" : "aze"},
    "Tate museum" : {"coords" : [51.508206, -0.099320], "closest" : "aze"},
    "Stompy garden Le tank" : {"coords" : [51.493111, -0.082658], "closest" : "aze"},
    "St pancreas" : {"coords" : [51.531574, -0.126101], "closest" : "aze"},
    "Cimetière de high gate" : {"coords" : [51.567160, -0.147071], "closest" : "aze"},
    "Long player" : {"coords" : [51.507953, 0.008208], "closest" : "aze"},
    "Hoxton street monster supplies" : {"coords" : [51.531508, -0.080268], "closest" : "aze"},
    "Viktor wind musée curiosité" : {"coords" : [51.534800, -0.057580], "closest" : "aze"},
    "18 folget street" : {"coords" : [51.521066, -0.077732], "closest" : "aze"},
    "picadelly circus" : {"coords" : [51.510163, -0.135036], "closest" : "aze"},
    "voie 9 3/4" : {"coords" : [51.532385, -0.123943], "closest" :"aze"}
}

# def measure(coords1, coords2):
#     lat1 = coords1[0]
#     lon1 = coords1[1]
#     lat2 = coords2[0]
#     lon2 = coords2[1]
#     R = 6378.137 # Radius of earth in KMs
#     dLat = lat2 * np.pi / 180 - lat1 * np.pi / 180;
#     dLon = lon2 * np.pi / 180 - lon1 * np.pi / 180
#     a  = np.sin(dLat/2) * np.sin(dLat/2) + np.cos(lat1*np.pi/180) * np.cos(lat2*np.pi/180) * np.sin(dLon/2) * np.sin(dLon/2)
#     c = 2 * math.atan2(np.sqrt(a), np.sqrt(1-a))
#     d = R*c
#     return d * 1000 # meters

# for k1, v1 in places.items():
#     closest = ["aze", 10000000]
#     for k2, v2 in places.items():
#         if k1 == k2:
#             continue
#         dist = measure(v1["coords"], v2["coords"])
#         if dist < closest[1]:
#             closest = [k2, dist]
#     places[k1]["closest"] = closest

# near = {}
    
    





        
    




coordinates = []
names = []
for k, v in places.items():
    coordinates.append(v["coords"])
    names.append(k)
coordinates = np.array(coordinates)

# exit()
plt.scatter(coordinates[:,0], coordinates[:,1]);
plt.show()
exit()
    
# for c in coordinates:
#     print(c)
coordinates = np.array(coordinates)
x, y = kmeans2(whiten(coordinates), 8, iter = 20)
plt.scatter(coordinates[:,0], coordinates[:,1], c=y);
plt.show()
# print(x, y)
exit()





file = open("index.html", 'w')

file.write('<html>')
file.write('<head>')
file.write('</head>')
file.write('<body>')
for k, v in places.items():
    file.write('<a href="https://maps.google.com/?q='+str(v["coords"][0])+','+str(v["coords"][1])+'">'+k+'</a>')
    file.write('<br>')
file.write('</body>')
file.write('</html>')

file.close()
