An analog clock which consists of two hands one for hour and another for minute. 
You have to calculate the shorter angle formed between hour and minute hand at any given time.

Approach : First convert the minutes to hours then find the difference between the hour values.
Now every hour in clock denotes 30 degrees and total angle  = 360 , hours = 12 , angle per hour = 360/12 = 30
Now we have to find the smaller angle so multiply the difference by 30 and also subtract the multiplied value by 360
and print the one which is smaller than the other 

def calculate_angle(h, m):
    # validate the input
    if not(0 <= h <= 12) or not(0 <= m <= 60):
        print("Wrong input")
        return None

    # Convert minutes to hours
    m = m//5  
    angle = abs(30 * (h - m))
    # Return the smaller angle of two possible angles
    angle = min(360 - angle, angle)

    return angle
