import requests
import json

city = "Seoul"
apikey = "6397279066772453ddc642adddc4305a"
lang = "kr"
#units - metric
api = f"""http://api.openweathermap.org/data/2.5/\
weather?q={city}&appid={apikey}&lang={lang}&units=metric"""
rslt = requests.get(api)
#print(rslt.text)
data = json.loads(rslt.text)

#name
print(data["name"],"의 날씨입니다.")
#weather-description
print("날씨는 ",data["weather"][0]["description"],"입니다.")
#main - temp
print("현재 온도는 ",data["main"]["temp"],"입니다.")
#main-feels_like
print("하지만 체감 온도는 ",data["main"]["feels_like"],"입니다.")
#main-temp_min
print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
#main-temp_max
print("최고 기온은 ",data["main"]["temp_max"],"입니다.")
#main-humidity
print("습도는 ",data["main"]["humidity"],"입니다.")
#main-pressure
print("기압은 ",data["main"]["pressure"],"입니다.")
#wind-deg
print("풍향은 ",data["wind"]["deg"],"입니다.")
#wind-speed
print("풍속은 ",data["wind"]["speed"],"입니다.")
