from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/weatherapp', methods = ['POST', 'GET'])
def get_weather():
    url = "https://api.openweathermap.org/data/2.5/weather"
    param = {'q': request.form.get('city'), 'units': request.form.get('units'), 'appid': 'd6122b3b5e29e8f83d563a28fb580617'}
    response = requests.get(url,params = param)
    data = response.json()
    return f"data : {data}"


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5003)