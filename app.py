# save this as app.py
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/logistic_regression', methods=['GET', 'POST'])
def logistic_regression():
    if request.method ==  'POST':
        model = pickle.load(open('lgr.pkl', 'rb'))
        male = float(request.form['gender'])
        age = float(request.form['age'])
        currentSmokeer = float(request.form['currentSmokeer'])
        cigsPerDay = float(request.form['cigsPerDay'])
        BPMeds = float(request.form['BPMeds'])
        prevalentStroke = float(request.form['prevalentStroke'])
        prevalentHyp = float(request.form['prevalentHyp'])
        diabetes = float(request.form['diabetes'])
        totChol = float(request.form['totChol'])
        sysBP = float(request.form['sysBP'])
        diaBP = float(request.form['diaBP'])
        BMI = float(request.form['BMI'])
        heartRate = float(request.form['heartRate'])
        glucose = float(request.form['glucose'])

        prediction = model.predict([[male, age, currentSmokeer, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP
                                     , diaBP, BMI, heartRate, glucose]])

        # print(prediction)

        if(prediction==0):
            prediction="No Risk of Coronary Heart Disease(CHD)"
        else:
            prediction="Risk of Coronary Heart Disease(CHD)"


        return render_template("logistic_regression.html", prediction_text="There is {}".format(prediction))
    else:
        return render_template("logistic_regression.html")

@app.route('/random_forest', methods=['GET', 'POST'])
def random_forest():
    if request.method ==  'POST':
        model = pickle.load(open('rfc.pkl', 'rb'))
        male = float(request.form['gender'])
        age = float(request.form['age'])
        currentSmokeer = float(request.form['currentSmokeer'])
        cigsPerDay = float(request.form['cigsPerDay'])
        BPMeds = float(request.form['BPMeds'])
        prevalentStroke = float(request.form['prevalentStroke'])
        prevalentHyp = float(request.form['prevalentHyp'])
        diabetes = float(request.form['diabetes'])
        totChol = float(request.form['totChol'])
        sysBP = float(request.form['sysBP'])
        diaBP = float(request.form['diaBP'])
        BMI = float(request.form['BMI'])
        heartRate = float(request.form['heartRate'])
        glucose = float(request.form['glucose'])

        prediction = model.predict([[male, age, currentSmokeer, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP
                                     , diaBP, BMI, heartRate, glucose]])

        # print(prediction)

        if(prediction==0):
            prediction="No Risk of Coronary Heart Disease(CHD)"
        else:
            prediction="Risk of Coronary Heart Disease(CHD)"

        return render_template("random_forest.html", prediction_text="There is {}".format(prediction))
    else:
        return render_template("random_forest.html")

@app.route('/naive_bayes', methods=['GET', 'POST'])
def naive_bayes():
    if request.method ==  'POST':
        model = pickle.load(open('nvb.pkl', 'rb'))
        male = float(request.form['gender'])
        age = float(request.form['age'])
        currentSmokeer = float(request.form['currentSmokeer'])
        cigsPerDay = float(request.form['cigsPerDay'])
        BPMeds = float(request.form['BPMeds'])
        prevalentStroke = float(request.form['prevalentStroke'])
        prevalentHyp = float(request.form['prevalentHyp'])
        diabetes = float(request.form['diabetes'])
        totChol = float(request.form['totChol'])
        sysBP = float(request.form['sysBP'])
        diaBP = float(request.form['diaBP'])
        BMI = float(request.form['BMI'])
        heartRate = float(request.form['heartRate'])
        glucose = float(request.form['glucose'])

        prediction = model.predict([[male, age, currentSmokeer, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP
                                     , diaBP, BMI, heartRate, glucose]])

        # print(prediction)

        if(prediction==0):
            prediction="No Risk of Coronary Heart Disease(CHD)"
        else:
            prediction="Risk of Coronary Heart Disease(CHD)"

        return render_template("naive_bayes.html", prediction_text="There is {}".format(prediction))
    else:
        return render_template("naive_bayes.html")
if __name__ == "__main__":
    app.run(debug=True)