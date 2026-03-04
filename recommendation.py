def coach_recommendation(predicted_passengers,capacity):

    if predicted_passengers > capacity:
        extra = predicted_passengers - capacity
        coaches = extra // 50 + 1
        return f"Add {coaches} extra coaches"

    elif predicted_passengers < capacity*0.5:
        return "Train underutilized"

    else:
        return "Capacity is optimal"