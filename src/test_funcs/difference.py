
def calc_diff(old_time: float, new_time: float):
    old_time = old_time * 1000
    new_time = new_time * 1000
    
    percetage_diff = (old_time / new_time) * 100
    
    return percetage_diff

def time_improvement(old_time: float, new_time: float):
    """
    new_time: Seconds\n
    old_time: Seconds
    """
    
    percentage_diff = calc_diff(old_time, new_time)
    
    if percentage_diff > 100:
        final_diff = percentage_diff - 100
        return f"You improved by {round(final_diff, 2)}% Congrats!"
    elif percentage_diff < 100:
        final_diff = 100 - percentage_diff
        return f"You were {round(final_diff, 2)}% from your best time!"

def goals(goal_time, curr_time):
    
    percentage_diff = calc_diff(goal_time, curr_time)
    
    if percentage_diff > 100:
        final_diff = percentage_diff - 100
        return "You already have the time dumbass"
    elif percentage_diff < 100:
        final_diff = 100 - percentage_diff
        time_diff = goal_time - curr_time
        if time_diff < 0:
            time_diff = time_diff * -1
        return f"You need to improve by {round(time_diff, 2)} seconds a {round(final_diff, 2)}% difference"