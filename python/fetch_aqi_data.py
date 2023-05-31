import requests
import pandas as pd


url = "http://air4thai.pcd.go.th/services/getNewAQI_JSON.php?region=1"
response = requests.get(url)
data = response.json()

regions = []
for item in data["stations"]:
    region = {}
    region["name"] = item["nameTH"]
    region["lat"] = item["lat"]
    region["lng"] = item["long"]
    region["aqi"] = item["AQILast"]["AQI"]["aqi"]
    regions.append(region)

print(regions)

nme = []
la = []
ln = []
aqi = []

for i in regions:
    nme.append(i['name'])
    la.append(i['lat'])
    ln.append(i['lng'])
    aqi.append(i['aqi'])

dict = {'name':nme, 'lat':la, 'lng':ln, 'aqi':aqi} 
df = pd.DataFrame(dict)
df.to_csv('aqi.csv')



