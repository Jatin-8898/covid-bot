from flask import Flask, request
import requests
import json
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/bot', methods=['POST','GET'])
def bot():
    incoming_msg = request.values.get('Body', '')
    #print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    
    if 'Hi' in incoming_msg or 'Hey' in incoming_msg or 'Heya' in incoming_msg or 'Menu' in incoming_msg:
        text = f'Hello 🙋🏽‍♂️, \nThis is a COVID-ChatBot developed by Jatin Varlyani to provide latest information updates and create awareness to help you and your family stay safe.\nFor any emergency 👇 \n 📞 Helpline: 011-23978046 | Toll-Free Number: 1075 \n ✉ Email: ncov2019@gov.in \n\nPlease enter one of the following option 👇 \n A. Coronavirus stats worldwide? \n B. Coronavirus cases in India? \n C. Coronavirus cases in China? \n D. Coronavirus cases in USA?\n E. Coronavirus cases in Italy? \n F. How does it spread? \n G. Preventive measures to be taken'
        msg.body(text)
        responded = True

    if 'A' in incoming_msg:
        # return total cases
        r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
        if r.status_code == 200:
            data = r.json()
            text = f'COVID Cases Worldwide \n Confirmed Cases : {data["cases"]}\nDeaths : {data["deaths"]}\nRecovered : {data["recovered"]}'
            print(text)
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True

    if 'B' in incoming_msg or 'India' in incoming_msg:
        # return total cases
        r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/india')
        if r.status_code == 200:
            data = r.json()
            text = f'COVID Cases in India \n\nConfirmed Cases : *{data["cases"]}* \n\nToday Cases : *{data["todayCases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}* \n\nActive Cases : *{data["active"]}*'
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True

    if 'C' in incoming_msg or 'China' in incoming_msg:
        # return total cases
        r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/china')
        if r.status_code == 200:
            data = r.json()
            text = f'COVID Cases in China \n\nConfirmed Cases : *{data["cases"]}* \n\nToday Cases : *{data["todayCases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}* \n\nActive Cases : *{data["active"]}*'
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True

    if responded == False:
        msg.body('I only know about corona, sorry!')

    return str(resp)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)