import requests

def get_data(place,days):
    api_key="042c0a53137470bd1fd3afb3cf203838"
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={place.title()}&appid={api_key}"
    response=requests.get(url)
    data=response.json()
    filtered_data=data['list'][:8*days]
    return filtered_data

if __name__=="__main__":
    print(get_data(place="Tokyo",days=3,option="Sky"))
