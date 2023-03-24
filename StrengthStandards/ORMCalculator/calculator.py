def calculate_one_rep_max(weight, reps):
    one_rep_max = weight * (1 + reps / 30)
    return round(one_rep_max, 2)


