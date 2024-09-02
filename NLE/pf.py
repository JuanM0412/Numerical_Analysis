import pandas as pd
import numpy as np


def get_user_input():
    """
    Prompts the user for initial values required to execute the fixed-point iteration method.
    Returns the initial guess, tolerance, maximum iterations, the function f(x), and the function g(x).
    """
    initial_guess = float(input("Enter the initial guess X0: "))
    tolerance = float(input("Enter the desired tolerance: "))
    max_iterations = int(input("Enter the maximum number of iterations: "))
    function_expression = input("Enter the function f(x) to evaluate (use 'x' as the variable): ")
    g_expression = input("Enter the function g(x) (use 'x' as the variable): ")
    return initial_guess, tolerance, max_iterations, function_expression, g_expression


def evaluate_function_at_point(function_expression, x):
    """
    Evaluates the mathematical function at a given point.
    The function expression is evaluated at the point 'x'.
    """
    function_expression = function_expression.replace('^', '**')  # Replace ^ with ** for exponentiation
    return eval(function_expression)


def print_result_root_found(root):
    """
    Prints that an exact root has been found.
    """
    print(f"{root} is an exact root of f(x)")


def print_result_approximation(approximation, tolerance):
    """
    Prints that an approximation of the root has been found within the given tolerance.
    """
    print(f"{approximation} is an approximation of a root of f(x) with a tolerance of {tolerance}")


def print_result_failure(max_iterations):
    """
    Prints that the fixed-point method failed to find a root within the maximum number of iterations.
    """
    print(f"Failed to find a root within {max_iterations} iterations")


def fixed_point_iteration(initial_guess, tolerance, max_iterations, function_expression, g_expression):
    """
    Implements the fixed-point iteration method to find a root of the given function.
    The method iterates using x_(n+1) = g(x_n) until the root is found or the tolerance is met.
    """
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
        error = abs(x_new - x)
        x = x_new

        iteration_data.append((iteration_count, x, f_value, error))

    if f_value == 0:
        print_result_root_found(x)
    elif error < tolerance:
        print_result_approximation(x, tolerance)
    else:
        print_result_failure(max_iterations)

    iteration_df = pd.DataFrame(iteration_data, columns=["Iteration", "X_n", "f(X_n)", "Error"])
    print("\nResulting Table:")
    print(iteration_df.to_string(index=False))

    return x, iteration_data


def main():
    """
    Main function that coordinates the execution of the fixed-point iteration method.
    """
    initial_guess, tolerance, max_iterations, function_expression, g_expression = get_user_input()
    _, _ = fixed_point_iteration(initial_guess, tolerance, max_iterations, function_expression, g_expression)


if __name__ == "__main__":
    main()