def quadratic_point(a, b, c, x):
    return (x, a*(x**2) + b*x + c)

def get_quadratic_point_error(a, b, c, datapoint):
    data_x, data_y = datapoint
    _, quad_y = quadratic_point(a, b, c, data_x)
    return abs(data_y - quad_y)

def get_total_quadratic_error(a, b, c, dataset):
    total_error = 0.0
    for datapoint in dataset:
        total_error += get_quadratic_point_error(a, b, c, datapoint)
    return total_error

def quadratic_of_best_fit(dataset):
    # y = ax^2 + bx + c
    a_min, a_max = -100, 101
    b_min, b_max = -100, 101
    c_min, c_max = -100, 101
    print(
        f'''
        Range of a values: {a_min} to {a_max}
        Range of b values: {b_min} to {b_max}
        Range of c values: {c_min} to {c_max}
        Number of possible curves: {(a_max - a_min) * (b_max - b_min) * (c_max - c_min)}
        '''
    )
    
    least_error, best_a, best_b, best_c = 1000000000000000000000000000000000000000000000000, 0, 0, 0
    for a in range(a_min, a_max):
        for b in range(b_min, b_max):
            for c in range(c_min, c_max):
                error = get_total_quadratic_error(a, b, c, dataset)
                if error < least_error:
                    least_error = error
                    best_a, best_b, best_c = a, b, c
                    print(f"Newest best fit: y = {best_a}x^2 + {best_b}x + {best_c}")
    print(f"Quadratic of best fit: y = {best_a}x^2 + {best_b}x + {best_c}")
    return (best_a, best_b, best_c, least_error)



