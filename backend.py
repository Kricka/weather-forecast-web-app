import requests

def get_data(place,option,days=5):
    api_key="042c0a53137470bd1fd3afb3cf203838"
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={place.title()}&appid={api_key}"
    response=requests.get(url)
    data=response.json()
    filtered_data=data['list'][:8*days]
    match option:
        case "Temperature":
            for item in filtered_data:
                a=[item['dt_txt'] for item in filtered_data]
                b=[item['main']['temp'] for item in filtered_data]
            return a,b

        case "Humidity":
            for item in filtered_data:
                a=[item['dt_txt'] for item in filtered_data]
                b=[item['main']['humidity'] for item in filtered_data]
            return a,b

get_data("Belgrade","Temperature",4)

if __name__=="__main__":
    print(get_data(place="Tokyo",days=None,option=None))
