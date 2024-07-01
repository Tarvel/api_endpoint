import requests
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")



@app.route('/api/hello', methods=['GET', 'POST'])
def hello():

    name = request.args.get('visitor_name')
    
    if request.method == "GET":


        ip_url_Api = requests.get('https://ipinfo.io/json')
        data = ip_url_Api.json()
        client_ip =  data['ip']
        
        location_url = 'http://ipinfo.io/' + client_ip + '/json'
        search_location_url = requests.get(location_url)
        location_data = search_location_url.json()
        location = location_data['city']
        
        
        api_key = "f41c5eb9a0ff4579925201355240406"
        api_url = "http://api.weatherapi.com/v1/current.json?key=" + api_key + "&q=" + location
        responsse = requests.get(api_url)

        if responsse.status_code == 200:
                data = responsse.json()
                temperature = data['current']['temp_c']

        else:
             return "data unavailable"
        response = {
        'client_ip': client_ip,

        'greeting': f"Hello, {name}! The temperature is {temperature} degree celcius in {location}",

        'location': location
        
        }

        return jsonify(response)





if __name__ == "__main__":
     app.run()