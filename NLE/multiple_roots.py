import sympy as sp


def derivate(function):
    variable = sp.symbols('x')
    function = sp.sympify(function)
    
    derivate = sp.diff(function, variable)
    
    return derivate


def evaluate_function(function, x):
    return function.subs(sp.symbols('x'), x)


def find_multiplicity(function, root):
    multiplicity = 0
    function = sp.sympify(function)

    print(evaluate_function(function, root) == 0)
    
    while evaluate_function(function, root) == 0:
        multiplicity += 1
        derivate = derivate.diff()
    
    return multiplicity


def main():
    function = input('Enter the function f(x) to evaluate: ')
    root_input = input('Enter the root to evaluate: ')

    if root_input == 'e':
        root = sp.E
    else:
        root = float(root)

    multiplicity = find_multiplicity(function, root)
    
    print(f'The multiplicity of the root {root} is {multiplicity}')


if __name__ == '__main__':
    main()