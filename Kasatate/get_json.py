from functools import wraps
import urllib.request as req
import json

def get_weather_data():
    url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/010000.json'
    filename = 'tenki.json'
    req.urlretrieve(url, filename)
    print("get data")
    


def update_weather():
    weather=""
    with open('tenki.json', 'r',encoding="UTF-8") as f:
        data = json.load(f)
        
    for area in data:
        name = area['name']
        # print(name)
        if name == "東京":
            for ts in area['srf']['timeSeries']:
                times = [n for n in ts['timeDefines']]
                if 'weathers' in ts['areas']:
                    for i, v in enumerate(ts['areas']['weathers']):
                        if "晴れ" not in v:
                            # print(v)
                            weather = "hare"
                            break
                        elif "雨" in v:
                            weather = "ame"
                        else:
                            for n, wind in enumerate(ts['areas']['winds']):
                                if "やや強く" in v:
                                    weather = "hare"
                                elif "強く" in v:
                                    weather = "taihu"
                                else:
                                    weather = "hare"
    return weather

if __name__=="__main__":
    weather = ""
    get_weather_data()
    weather=update_weather()
    print(weather)