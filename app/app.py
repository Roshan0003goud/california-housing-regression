from flask import Flask, render_template, request
import joblib
import numpy as np

model = joblib.load('models/final_model.pkl')
scaler = joblib.load('data/scaler.pkl')
 
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    MedInc= float(request.form.get('MedInc'))
    HouseAge= float(request.form.get("HouseAge"))
    AveRooms= float(request.form.get('AveRooms'))
    AveBedrms= float(request.form.get('AveBedrms'))
    Population= float(request.form.get('Population'))
    AveOccup= float(request.form.get('AveOccup'))
    Latitude= float(request.form.get('Latitude'))
    Longitude=float(request.form.get('Longitude'))
    
    if AveRooms <= 0 or Population <= 0 or HouseAge < 0 or MedInc <= 0:
        return render_template('index.html', error='Please enter valid positive values!')
    
            
    RoomsPerHousehold = AveRooms / AveOccup
    BedroomPerRoom = AveBedrms / AveRooms
    PopulationPerHousehold = Population / AveOccup
    Distance_from_coast = abs(Longitude -(-120))
    scaled_input = np.array([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude, RoomsPerHousehold, BedroomPerRoom, PopulationPerHousehold, Distance_from_coast]])
    scaled_input = scaler.transform(scaled_input)
    prediction = model.predict(scaled_input)
    return render_template('index.html', prediction=round(prediction[0] * 100000, 2))

    

if __name__ == '__main__':
    app.run(debug=True)