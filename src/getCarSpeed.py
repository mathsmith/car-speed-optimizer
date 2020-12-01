import math as m


# FUNCTIONS LIST
def light_is_green(v, xt, t):
    """
    Determines if the light will be green when a car passes through it.

    :param v: velocity[km/h] car is going.
    :param xt: distance[km] car must travel to reach the traffic light.
    :param t: duration[h] of time a light is green and red.

    :return: True/False declaring if the light will be green at the instantaneous moment the car passes it.
    """
    time_to_pass_light = xt / v
    units_of_duration = time_to_pass_light / t
    if round(units_of_duration, 10) == (round(units_of_duration, 2)):
        units_of_duration = round(units_of_duration, 10)
        
    units_of_duration_not_natural = time_to_pass_light % t != 0
    duration_interval_upper_bound_odd = all((m.ceil(units_of_duration) % 2 == 1, units_of_duration % 2 != 1))
    units_of_duration_is_even = units_of_duration % 2 == 0
    
    green_condition_1 = all((units_of_duration_not_natural, duration_interval_upper_bound_odd))
    green_condition_2 = units_of_duration_is_even
    green_conditions = (green_condition_1, green_condition_2)
    
    return any(green_conditions)


max_speed = int(float(input()))
light_count = int(float(input()))
light_data = []
for i in range(light_count):
    distance, duration = [int(float(j)) for j in input().split()]
    light_data.append((distance/1000, duration/3600)) # converting to km and h respectively.

best_speed = max_speed
while not all([light_is_green(best_speed, x[0], x[1]) for x in light_data]):
    best_speed -= 1

print(f"{best_speed}")
