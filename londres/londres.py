import gmplot

places ={
    "Musee des sciences" : [51.497987, -0.174573], 
    "Abbey road" : [51.536051, -0.184107],
    "Hamleys Magasin de jouets" : [51.513554, -0.139956],
    "British museum" : [51.519573, -0.126946],
    "Borough market" : [51.505625, -0.091010],
    "Camden town" : [51.540834, -0.148392],
    "natural history museum" : [51.496880, -0.176401],
    "Brick lane market" : [51.521367, -0.071880],
    "Tour de Londres" : [51.508306, -0.075896],
    "Sky garden" : [51.511453, -0.083584],
    "Hms Belfast" : [51.506786, -0.081368],
    "Tower bridge" : [51.505603, -0.075346],
    "London’s nose" : [51.506963, -0.128615],
    "Old operating museum" : [51.505142, -0.088588],
    "Wellcome collection" : [51.526173, -0.134002],
    "Grant museum of zoology" : [51.523766, -0.134658],
    "Cyberdog" : [51.542383, -0.147534],
    "Tate museum" : [51.508206, -0.099320],
    "Stompy garden Le tank" : [51.493111, -0.082658],
    "St pancreas" : [51.531574, -0.126101],
    "Cimetière de high gate" : [51.567160, -0.147071],
    "Long player" : [51.507953, 0.008208],
    "Hoxton street monster supplies" : [51.531508, -0.080268],
    "Viktor wind musée curiosité" : [51.534800, -0.057580],
    "18 folget street" : [51.521066, -0.077732],
    "picadelly circus" : [51.510163, -0.135036],
    "voie 9 3/4" : [51.532385, -0.123943]
}


gmap = gmplot.GoogleMapPlotter(places['Musee des sciences'][0], places['Musee des sciences'][1], 13 )
gmap.apikey = "AIzaSyAmef7s_YghiffePPa08BkBlKEDwSflPSk"
  
# Pass the absolute path 
gmap.draw( "/home/antoine/MISC/apirrone.github.io/londres/index.html" ) 
