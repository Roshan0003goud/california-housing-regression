# california-housing-regression
MAchine learning web app that predicts the hosue prices in california

## live demo

[click here to try tha app](https://california-housing-predictor-5r5a.onrender.com/)

## Description
- What my app does means, with your inputs like(Medinc, AveRooms, AveBedrooms, location, occupation) it predicts the house prices in that area.
-  I have used Random Forest algorithm for my model .
-  And trained model on the california housing dataset from scikit .

## Dataset
- I have imported dataset from sklearn.datasets
- Afer cleaning data i have 19,629 rows.
- I have 8 features in this dataset, And 4 feature engineered, so in totall 12 .

## Methodology
- Cleaned the dataset — removed outliers, 19,629 rows remaining
- Feature Engineering — created 4 new columns for better model understanding
- Split data 80% training, 20% testing
- Trained 6 models (Linear Regression, Ridge, Lasso, Decision Tree, Random Forest, Gradient Boosting) — Random Forest performed best
- Final model metrics: R²=0.7606, MAE=0.3341, RMSE=0.4880

## Tech Stack 
- Language- python
- Framwework for website - Flask
- libraries- scikit-learn, numpy, joblib, pandas.
- Depoly - Render

## What I have learnt 
- I learned how to clean real-world data — removing outliers and handling bad values
- I learned that Random Forest performs better than simple models like Linear Regression
- I learned how to build and deploy a web app using Flask and Render
- I learned that feature engineering (creating new columns) can improve model accuracy

## How to Run Locally

```bash
git clone https://github.com/Roshan0003goud/california-housing-regression.git
cd california-housing-regression
pip install -r requirements.txt
python app/app.py
```

Then open your browser and go to `http://127.0.0.1:5000`

## Project Structure
california-housing-regression/
├── app/
│   ├── app.py                  # Flask web application
│   ├── templates/
│   │   └── index.html          # HTML frontend
│   └── static/
│       └── feature_importance.png
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_preparation.ipynb
│   └── 03_modeling.ipynb
├── models/
│   └── final_model.pkl         # Trained Random Forest model
├── data/
│   └── scaler.pkl              # StandardScaler
├── requirements.txt
└── README.md

## Insights
- Median Income has highest correlation with price.
- Location(latitude/longitude) has as significant impact on house prices- manily on coastal and urban areas are more expensive.
