from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
	# Getting the current location Lattitude & Longitude of the User from the Device location.
	rsp=requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyDohUWhL5FdgtM7p5cmqwHBuV9gn5NheDA")
	j=rsp.json()
	lat=j['location']['lat']
	lng=j['location']['lng']
	# Getting the Location address in the string format
	getad=requests.post("https://maps.googleapis.com/maps/api/geocode/json?latlng="+str(lat)+","+str(lng)+"&key=AIzaSyDohUWhL5FdgtM7p5cmqwHBuV9gn5NheDA")
	p=getad.json()
	currentAddress=p['results'][0]['formatted_address'] 
	# Rendering the results to the template to display the results.
	return render_template("panel.html", start=currentAddress,lat=str(lat),lng=str(lng))

if __name__=="__main__":
	app.run()