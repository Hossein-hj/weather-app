import requests
import datetime

city_name = ("qom").capitalize()
Apikey="97149a9ce6e74f2936db6e14180a2a36"
my_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={Apikey}"
response = requests.get(url=my_url)

if response.status_code== 200:
    data = response.json()
    lat = data[0]['lat']
    lon = data[0]['lon']
    print(lat, lon)
    country = data[0]['country']
    # temp_min = data[0]['temp_min']

    # print(temp_min)
    print("start")
    my_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={Apikey}&units=metric"
    response = requests.get(url=my_url)

    if response.status_code == 200:
        
        data = (response.json())
        out_name = data['name'] #esm khoroji

        if out_name == city_name: # label error
            print(data)
            print(data['sys']['sunrise'])
            now_temp = (data['main']['temp'])
            min_temp = (data['main']['temp_min'])
            max_temp = (data['main']['temp_max'])
            temp_avg = ((min_temp)+(max_temp))/2
            print("----------------------------------")
            print(data['weather'][0]['description'])
            print(country)
            
            print(now_temp)
            print(max_temp)
            print(min_temp)
            print(temp_avg)
            print(f"vazeeat hava:{data['weather'][0]["main"]}")#vazeeat hava
            print(data['weather'][0])
            print(data['main']['sea_level']) #sea
            timestamp = data['sys']['sunrise']
            dt = datetime.datetime.fromtimestamp(timestamp)
            only_time = dt.strftime("%H:%M:%S")
            print(only_time)
            print(out_name)
            print(timestamp)
            print("----------------------------------")
            print(data['sys']['country'])
            print(dt)

            print("----------------------------------")
            print(data)
            print(f"vazeeat hava:{data['weather'][0]["main"]}") #weather
            print(data['weather'][0]['description'])
            print("----------------------------------")


        else:
            print("please enter true name")
            print(city_name)
    