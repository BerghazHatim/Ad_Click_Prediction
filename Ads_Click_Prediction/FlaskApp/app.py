import numpy as np
from flask import Flask, request,render_template, url_for
import pickle

app = Flask(__name__)#initiation d'app
model = pickle.load(open("model.pkl","rb"))#lire du modele en mode read
print(model)

@app.route('/', methods=['GET'])
def home():
    
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    try:
        Daily = int(request.form['DTPOS']) 

        Age = int(request.form['Age'])

        AreaIncome = int(request.form['AreaIncome'])

        DIUsage = int(request.form['DIU'])

        Gender = int(request.form['Gender'])

        Month = int(request.form['Month'])

        Day = int(request.form['Day'])

        Hour = int(request.form['Hour'])

        Country = int(request.form['Country'])

    except ValueError:

        error = 'Must Complet All The Informations To Procced'
        return render_template('index.html', error=error)

    Values = np.array([Daily,Age,AreaIncome,DIUsage,Gender,Month,Day,Hour,Country]).reshape(-1,9)

    prediction = model.predict(Values)

    output = prediction

    returned_value = "NOT Click On This Advertisement!"
    if output==1:
        returned_value = "Click On This Advertisement!"
    
    return render_template('index.html', prediction_text='The User Will Most Likely {}'.format(returned_value))

if __name__ == "__main__":
    app.run(debug=True)