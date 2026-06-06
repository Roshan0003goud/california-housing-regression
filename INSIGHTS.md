## Project overview

1. "This project all about" the predicting the california house prices.
2. In this porject I have used California Housing price dataset from sklearn(scikit-learn)
3. I have trained machine learning model to predict the housing prices.


## Dataset 

1. After Cleaning the dataset i have (19,629)Rows.
2. In total We have 12 features (Columns).
3. And I have created 4 engineered fetures, 
    They are,
            1. RoomPerHoushold = AveRooms / AveOccup
            2. BedroomPerRoom = AveBedrms / AveRooms
            3. PopulationPerHousehold = Population / AveOccup
            4. Distance_from_coast = how far each district from longitude -120.
4. My Target variable in this project is price.


## Key Findings

1. MedInc has strongest correlation with Price.
2. Houses near coast areas are too enpesnsive.
3. During my cleaning data I have removed outliers. Removed outliers are 
    1. Removed rows PRice >= 4.99(the 500k cap)
    2. And also removed AveRooms > 50 and Aveoccup > 20 .

## Best Model 

1. Here I have try couples of algorithms here but i have upper hand in Random Forest. 
2. Final scores i got (MAE = 0.3341, RMSe = 0.4880, R2 = 0.7606)
3. And i have got parameters for this algorithm is 
    1. n_estimators = 300
    2. max_depth = 15
    3. min_sample_split = 2

## Most Important Features

1. To Predict the  price for model MedInc is the important feature .
2. And also we have some other features with less important percentage but eventhought that feature also plays an role for predicitng and price .
3. Those are , Aveoccup, location, Distance_from_coast


## Conclusion 

1. The model achieved 76% acccuracy (R2 = 0.7606)
2. Model Struggles to predict EXpensie houses(above 300k)
3. Future improvemnt : could try more data or xboost for better accuracy


