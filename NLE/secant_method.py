import pandas as pd
import numpy as np
import math


def evaluate_function(function_expression, x_value):
    return eval(function_expression, {'x': x_value, 'np': np, 'math': math, 'abs': abs})


def secant_method(x0, x1, tolerance, max_iterations, function_expression):
    function_values = []
    root_approximations = []
    errors = []
    iteration_numbers = []
    
    function_x0 = evaluate_function(function_expression, x0)
    function_x1 = evaluate_function(function_expression, x1)
    iteration_count = 0
    error = 100

    x_next = x1
    function_current = evaluate_function(function_expression, x_next)
    
    function_values.append(function_current)
    root_approximations.append(x_next)
    errors.append(error)
    iteration_numbers.append(iteration_count)
    
    while error > tolerance and function_current != 0 and iteration_count < max_iterations:
        x_next = x1 - (function_x1 * (x1 - x0) / (function_x1 - function_x0))
        function_current = evaluate_function(function_expression, x_next)
        
        function_values.append(function_current)
        root_approximations.append(x_next)
        iteration_count += 1
        error = abs(root_approximations[iteration_count] - root_approximations[iteration_count - 1])
        
        iteration_numbers.append(iteration_count)
        errors.append(error)
        
        x0 = x1
        x1 = x_next
        function_x0 = evaluate_function(function_expression, x0)
        function_x1 = evaluate_function(function_expression, x1)
    
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
    x0 = float(input('Enter X0: '))
    x1 = float(input('Enter X1: '))
    tolerance = float(input('Enter the desired tolerance: '))
    max_iterations = int(input('Enter the maximum number of iterations: '))
    function_expression = input('Enter the function f(x) to evaluate (use x as the variable): ')

    root_approximations, function_values, errors, iteration_numbers = secant_method(
        x0, x1, tolerance, max_iterations, function_expression)
    
    print_results(root_approximations, function_values, errors, iteration_numbers, tolerance, max_iterations)


if __name__ == '__main__':
    main()