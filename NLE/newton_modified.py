import pandas as pd
import numpy as np
import math


def evaluate_function(function_expression, x_value):
    return eval(function_expression, {'x': x_value, 'np': np, 'math': math, 'abs': abs})


def newton_raphson_method(initial_guess, tolerance, max_iterations, function_expression, derivative_expression, second_derivative_expression, error_type = 0):
    function_values = []
    root_approximations = []
    errors = []
    iteration_numbers = []
    
    x_current = initial_guess
    function_current = evaluate_function(function_expression, x_current)
    derivative_current = evaluate_function(derivative_expression, x_current)
    second_derivative_current = evaluate_function(second_derivative_expression, x_current)
    iteration_count = 0
    error = 100
    
    function_values.append(function_current)
    root_approximations.append(x_current)
    errors.append(error)
    iteration_numbers.append(iteration_count)
    
    while error > tolerance and function_current != 0 and derivative_current != 0 and iteration_count < max_iterations:
        x_next = x_current - (function_current * derivative_current) / ((derivative_current ** 2) - (function_current * second_derivative_current))
        derivative_current = evaluate_function(derivative_expression, x_next)
        function_current = evaluate_function(function_expression, x_next)
        
        function_values.append(function_current)
        root_approximations.append(x_next)
        iteration_count += 1
        if error_type == 0: #absolute error
            error = abs(root_approximations[iteration_count] - root_approximations[iteration_count - 1])
        else: #relative error
            error = abs((root_approximations[iteration_count] - root_approximations[iteration_count - 1])/root_approximations[iteration_count])
        
        iteration_numbers.append(iteration_count)
        errors.append(error)
        
        x_current = x_next
    
    return root_approximations, function_values, errors, iteration_numbers


def print_results(root_approximations, function_values, errors, iteration_numbers, tolerance, max_iterations):
    results = pd.DataFrame({
        'Iteration': iteration_numbers,
        'x_n': root_approximations,
        'f(x_n)': function_values,
        'Error': errors
    })
    
    print(results)
    
    if function_values[-1] == 0:
        print(f'{root_approximations[-1]} is a root of f(x)')
    elif errors[-1] < tolerance:
        print(f'{root_approximations[-1]} is an approximation of a root of f(x) with tolerance {tolerance}')
    else:
        print(f'Failed to converge in {max_iterations} iterations')
    

def main():
    initial_guess = float(input('Enter the initial value X0: '))
    tolerance = float(input('Enter the desired tolerance: '))
    max_iterations = int(input('Enter the maximum number of iterations: '))
    function_expression = input('Enter the function f(x) to evaluate (use x as the variable): ')
    derivative_expression = input('Enter the derivative of the function f(x) (use x as the variable): ')
    second_derivative_expression = input('Enter the second derivative of the function f(x) (use x as the variable): ')
    error_type = int(input('Enter 0 for absolute error or 1 for relative error: '))

    root_approximations, function_values, errors, iteration_numbers = newton_raphson_method(
        initial_guess, tolerance, max_iterations, function_expression, derivative_expression, second_derivative_expression, error_type)
    
    print_results(root_approximations, function_values, errors, iteration_numbers, tolerance, max_iterations)


if __name__ == '__main__':
    main()