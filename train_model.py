import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

df = pd.read_csv("data/railway_data.csv")

features = [
"Hour",
"Seat_Capacity",
"Number_of_Coaches",
"Platform",
"Weekend",
"Holiday"
]

X = df[features]
y = df["Passenger_Count"]

X_train,X_test,y_train,y_test = train_test_split(
X,y,test_size=0.2,random_state=42
)

model = RandomForestRegressor()

model.fit(X_train,y_train)

pickle.dump(model,open("models/model.pkl","wb"))

print("Model trained and saved")