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
    
    errors = []
    
    if MedInc <= 0:
        errors.append("Median Income must be greater than 0!")
    
    if HouseAge < 0:
        errors.append("error, HouseAge cannot be in negative")
    
    if AveRooms <=0:
        errors.append("error, Averooms must be greater than 0!")
    
    if AveBedrms <=0:
        errors.append("error, Avebedrooms must be greater than 0!")
    
    if Population <=0:
        errors.append("error, population must be greater than 0")
    
    if AveOccup <=0:
        errors.append("error, occupation must be grater than 0!")
        
    if errors:
        return render_template('index.html', errors=errors)
    
    
            
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