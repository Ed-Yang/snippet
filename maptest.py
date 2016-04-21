from googlemaps import GoogleMaps 

mapService = GoogleMaps()

directions = mapService.directions('texarkana', 'atlanta')

for step in directions['Directions']['Route'][0]['Step']:
    print step['descriptionHtml']

