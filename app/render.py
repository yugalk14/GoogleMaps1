from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
	rsp=requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyDohUWhL5FdgtM7p5cmqwHBuV9gn5NheDA")
	j=rsp.json()
	lat=j['location']['lat']
	lng=j['location']['lng']
	getad=requests.post("https://maps.googleapis.com/maps/api/geocode/json?latlng="+str(lat)+","+str(lng)+"&key=AIzaSyDohUWhL5FdgtM7p5cmqwHBuV9gn5NheDA")
	p=getad.json()
	currentAddress=p['results'][0]['formatted_address']
	return render_template("panel.html", start=currentAddress,lat=str(lat),lng=str(lng))

if __name__=="__main__":
	app.run()