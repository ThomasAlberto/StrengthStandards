def calculate_wilks_results(squat_weight, bench_weight, deadlift_weight, bodyweight):
    a = -216.0475144
    b = 16.2606339
    c = -0.002388645
    d = -0.00113732
    e = 0.00000701863
    f = -0.00000001291

    total_weight = squat_weight + bench_weight + deadlift_weight
    result = round(total_weight * 500 / (a + (b * bodyweight) + (c * bodyweight ** 2) + (d * bodyweight ** 3) + (e * bodyweight ** 4) + (f * bodyweight ** 5)), 2)
    return result
