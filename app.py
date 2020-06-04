from flask import Flask, render_template, request
import requests
import datetime

app = Flask(__name__)

# API URL
url = "https://api.covid19api.com/summary"

# Get response in terms of JSON of COVID-19 summary and saves Global while looping since API runs out at times
while True:
    try:
        response = requests.get(url,headers={"Accept": "application/json"}).json()
        break
    except:
        pass

# Stores response as a dictionary for later use
response = dict(response)

# Get current date and format it
time = datetime.datetime.now()
time = time.strftime("%I %M %p, %A %d %B %Y ")

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/global/')
def country():
	return render_template('global.html', response=response, time=time)

@app.route('/country/')
def statistics():
	return render_template('country.html', response=response, time=time)

@app.route('/create/', methods=['POST'])
def countryinfo():
	country_name = request.form['title']
	country_filter = filter(lambda val: val['Country'] == country_name, response["Countries"])
	country_filter = list(country_filter)

	return render_template('countrystats.html', country_filter=country_filter, time=time, response=response)	

@app.route('/comp/')
def comparison():
	return render_template('comp.html', response=response, time=time)

@app.route('/createcomp/', methods=['POST'])
def compinfo():
	country_name1 = request.form['title1']
	country_name2 = request.form['title2']
	country_filter1 = filter(lambda val: val['Country'] == country_name1, response["Countries"])
	country_filter1 = list(country_filter1)
	country_filter2 = filter(lambda val: val['Country'] == country_name2, response["Countries"])
	country_filter2 = list(country_filter2)

	return render_template('countrycomp.html', country_filter1=country_filter1, country_filter2=country_filter2, time=time, response=response)	

@app.route('/about/')
def about():
	return render_template('about.html')

if __name__ == '__main__':
	app.run()


