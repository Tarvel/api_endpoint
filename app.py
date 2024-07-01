import requests
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():

    return render_template("index.html")



@app.route('/api/hello', methods=['GET', 'POST'])
def hello():
    name = request.args.get('visitor_name')
    ip = requests.get('https://api.ipify.org?format=json')
    data = ip.json()
    client_ip = data['ip']

    if request.method == "GET":
        
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

        'location': location,

        'greeting': f"Hello, {name.title()}! The temperature is {temperature} degree celcius in {location.title()}"
        }

        return jsonify(response)





if __name__ == "__main__":
     app.run(debug=True)