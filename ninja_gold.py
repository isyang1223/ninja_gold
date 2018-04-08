from flask import Flask, render_template, request, redirect, session
import random, math
app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def index():
    
    if 'gold' in session:
        session['gold'] = session['gold']
    else:
        session['gold'] = 0

    print session['gold']
    return render_template("root.html", gold = session['gold'])
    


@app.route('/process_money', methods=["POST"])
def playing():
    if "message" not in session:
        session["message"] = []
    if request.form["building"] == "farm":
        earned = random.randrange(10,21)
        session['gold'] += earned
        session['message'].append("Earned " + str(earned) + " golds from the farm!")
    elif request.form["building"] == "cave":
        earned = random.randrange(5,11)
        session['gold'] += earned
        session['message'].append("Earned " + str(earned) + " golds from the cave!")
    elif request.form["building"] == "house":
        earned = random.randrange(2,6)
        session['gold'] += earned
        session['message'].append("Earned " + str(earned) + " golds from the house!")
    elif request.form["building"] == "casino":
        earned = random.randrange(-50,51)
        session['gold'] += earned
        if earned > 0:
            session['message'].append("Earned " + str(earned) + " golds from the casino!")
        else:
            session['message'].append("Entered a casino and lost " + str(abs(earned)) + " golds... Ouch..")
    return redirect('/')

@app.route('/reset', methods=["POST"])
def reset():
    session['gold'] = 0
    session["message"] = []



    return redirect('/')





app.run(debug=True) # run our server