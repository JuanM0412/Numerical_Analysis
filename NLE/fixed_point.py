import pandas as pd
import numpy as np


def get_user_input():
    initial_guess = float(input('Enter the initial guess X0: '))
    tolerance = float(input('Enter the desired tolerance: '))
    max_iterations = int(input('Enter the maximum number of iterations: '))
    function_expression = input('Enter the function f(x) to evaluate (use x as the variable): ')
    g_expression = input('Enter the function g(x) (use x as the variable): ')
    error_type = int(input('Enter 0 for absolute error or 1 for relative error: '))
    return initial_guess, tolerance, max_iterations, function_expression, g_expression, error_type


def evaluate_function_at_point(function_expression, x):
    function_expression = function_expression.replace('^', '**')
    return eval(function_expression)


def print_result_root_found(root):
    print(f'{root} is an exact root of f(x)')


def print_result_approximation(approximation, tolerance):
    print(f'{approximation} is an approximation of a root of f(x) with a tolerance of {tolerance}')


def print_result_failure(max_iterations):
    print(f'Failed to find a root within {max_iterations} iterations')


def fixed_point_iteration(initial_guess, tolerance, max_iterations, function_expression, g_expression, error_type):
    iteration_data = []

    x = initial_guess
    f_value = evaluate_function_at_point(function_expression, x)
    error = 100
    iteration_count = 0

    iteration_data.append((iteration_count, x, f_value, error))

    while error > tolerance and f_value != 0 and iteration_count < max_iterations:
        x_new = evaluate_function_at_point(g_expression, x)
        f_value = evaluate_function_at_point(function_expression, x_new)
        iteration_count += 1
        if error_type == 0: #absolute error
            error = abs(x_new - x)
        else: #relative error
            error = abs((x_new - x)/x_new)
        x = x_new

        iteration_data.append((iteration_count, x, f_value, error))

    if f_value == 0:
        print_result_root_found(x)
    elif error < tolerance:
        print_result_approximation(x, tolerance)
    else:
        print_result_failure(max_iterations)

    iteration_df = pd.DataFrame(iteration_data, columns=['Iteration', 'X_n', 'f(X_n)', 'Error'])
    print('\nResulting Table:')
    print(iteration_df.to_string(index=False))

    return x, iteration_data


def main():
    initial_guess, tolerance, max_iterations, function_expression, g_expression, error_type = get_user_input()
    _, _ = fixed_point_iteration(initial_guess, tolerance, max_iterations, function_expression, g_expression, error_type)


if __name__ == '__main__':
    main()