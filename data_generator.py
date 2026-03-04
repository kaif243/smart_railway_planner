import pandas as pd
import numpy as np
import random

cities = [
"Hyderabad","Vijayawada","Tirupati","Chennai","Bangalore",
"Delhi","Agra","Mumbai","Pune","Kolkata",
"Ahmedabad","Jaipur","Lucknow","Bhopal","Nagpur",
"Visakhapatnam","Patna","Coimbatore","Indore","Surat"
]

data = []

for i in range(3000):

    train_id = "T" + str(random.randint(1000,9999))

    source = random.choice(cities)
    destination = random.choice(cities)

    while destination == source:
        destination = random.choice(cities)

    hour = random.randint(0,23)

    weekend = random.choice([0,1])
    holiday = random.choice([0,1])

    passenger = random.randint(200,900)

    seat_capacity = random.choice([500,600,700,800])

    coaches = seat_capacity // 50

    platform = random.randint(1,12)

    delay = random.randint(0,30)

    data.append([
        train_id,
        source,
        destination,
        "2025-03-01",
        hour,
        passenger,
        seat_capacity,
        coaches,
        platform,
        delay,
        weekend,
        holiday
    ])

df = pd.DataFrame(data,columns=[
"Train_ID","Source","Destination","Date","Hour",
"Passenger_Count","Seat_Capacity","Number_of_Coaches",
"Platform","Delay_Minutes","Weekend","Holiday"
])

df.to_csv("data/railway_data.csv",index=False)

print("Dataset generated successfully with multiple cities")