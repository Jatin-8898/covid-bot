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
        text = f'Hello 🙋🏽‍♂, \nThis is a Covid-Bot developed by Jatin Varlyani to provide latest information updates i.e cases in different countries and create awareness to help you and your family stay safe.\n For any emergency 👇 \n 📞 Helpline: 011-23978046 | Toll-Free Number: 1075 \n ✉ Email: ncov2019@gov.in \n\n Please enter one of the following option 👇 \n A. Covid-19 statistics *Worldwide*. \n B. Covid-19 cases in *India*. \n C. Covid-19 cases in *China*. \n D. Covid-19 cases in *USA*. \n E. Coronavirus cases in *Italy*. \n F. How does it *Spread*? \n G. Preventive measures to be taken.'
        msg.body(text)
        responded = True

    if 'A' in incoming_msg:
        # return total cases
        r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
        if r.status_code == 200:
            data = r.json()
            text = f'_Covid-19 Cases Worldwide_ \n\nConfirmed Cases : *{data["cases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}*  \n\n 👉 Type *B* to check cases in *India* \n 👉 Type *B, C, D, E, F, G* to see other options \n 👉 Type *Menu* to view the Main Menu'
            print(text)
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True

    if 'B' in incoming_msg or 'India' in incoming_msg:
        # return cases in india
        r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/india')
        if r.status_code == 200:
            data = r.json()
            text = f'_Covid-19 Cases in India_ \n\nConfirmed Cases : *{data["cases"]}* \n\nToday Cases : *{data["todayCases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}* \n\n 👉 Type *C* to check cases in *China* \n 👉 Type *A, C, D, E, F, G* to see other options \n 👉 Type *Menu* to view the Main Menu'
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True

    if 'C' in incoming_msg or 'China' in incoming_msg:
        # return cases in china
        r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/china')
        if r.status_code == 200:
            data = r.json()
            text = f'_Covid-19 Cases in China_ \n\nConfirmed Cases : *{data["cases"]}* \n\nToday Cases : *{data["todayCases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}* \n\nActive Cases : *{data["active"]}* \n\n 👉 Type *D* to check cases in *USA* \n 👉 Type *A, B, D, E, F, G* to see other options \n 👉 Type *Menu* to view the Main Menu'
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True
    
    if 'D' in incoming_msg or 'USA' in incoming_msg:
        # return cases in usa
        r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/usa')
        if r.status_code == 200:
            data = r.json()
            text = f'_Covid-19 Cases in USA_ \n\nConfirmed Cases : *{data["cases"]}* \n\nToday Cases : *{data["todayCases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}* \n\nActive Cases : *{data["active"]}*  \n\n 👉 Type *E* to check cases in *Italy* \n 👉 Type *A, B, C, E, F, G* to see other options \n 👉 Type *Menu* to view the Main Menu'
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True
    
    if 'E' in incoming_msg or 'Italy' in incoming_msg:
        # return cases in italy
        r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/italy')
        if r.status_code == 200:
            data = r.json()
            text = f'_Covid-19 Cases in Italy_ \n\nConfirmed Cases : *{data["cases"]}* \n\nToday Cases : *{data["todayCases"]}* \n\nDeaths : *{data["deaths"]}* \n\nRecovered : *{data["recovered"]}* \n\nActive Cases : *{data["active"]}* \n\n 👉 Type *F* to check how *Covid-19 Spreads?* \n 👉 Type *A, B, C, E, F, G* to see other options \n 👉 Type *Menu* to view the Main Menu'
        else:
            text = 'I could not retrieve the results at this time, sorry.'
        msg.body(text)
        responded = True
    
    if 'F' in incoming_msg:
        text = f'_Coronavirus spreads from an infected person through_ 👇 \n\n ♦ Small droplets from the nose or mouth which are spread when a person coughs or sneezes \n\n ♦ Touching an object or surface with these droplets on it and then touching your mouth, nose, or eyes before washing your hands \n \n ♦ Close personal contact, such as touching or shaking hands \n Please watch the video for more information 👇 https://youtu.be/0MgNgcwcKzE \n\n 👉 Type G to check the *Preventive Measures* \n 👉 Type *A, B, C, D, E* to see other options \n 👉 Type *Menu* to view the Main Menu'
        msg.body(text)
        msg.media('https://user-images.githubusercontent.com/34777376/77290801-f2421280-6d02-11ea-8b08-fdb516af3d5a.jpeg')
        responded = True
    
    if 'G' in incoming_msg:
        text = f'_Coronavirus infection can be prevented through the following means_ 👇 \n ✔️ Clean hand with soap and water or alcohol-based hand rub \n https://youtu.be/EJbjyo2xa2o \n\n ✔️ Cover nose and mouth when coughing & sneezing with a tissue or flexed elbow \n https://youtu.be/f2b_hgncFi4 \n\n ✔️ Avoid close contact & maintain 1-meter distance with anyone who is coughing or sneezin \n https://youtu.be/mYyNQZ6IdRk \n\n ✔️ Isolation of persons traveling from affected countries or places for at least 14 day \n https://www.mohfw.gov.in/AdditionalTravelAdvisory1homeisolation.pdf \n\n ✔️ Quarantine if advise \n https://www.mohfw.gov.in/Guidelinesforhomequarantine.pdf \n\n 👉 Type *A, B, C, D, E, F* to see other option \n 👉 Type *Menu* to view the Main Menu'
        msg.body(text)
        msg.media('https://user-images.githubusercontent.com/34777376/77290864-1c93d000-6d03-11ea-96fe-18298535d125.jpeg')
        responded = True

    if responded == False:
        msg.body('I only know about corona, sorry!')

    return str(resp)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)