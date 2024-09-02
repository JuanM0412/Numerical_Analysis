import pandas as pd
import numpy as np
import math
import wdb

def main():
     x = np.pi/4
     tol = 0.5E-3

     selected_function = input('Select between: \n1) cos \n2) sen \n')

     if selected_function == '1':
          cos(x, tol)
     elif selected_function == '2':
          sen(x, tol)


def cos(x, tol):
     selected_error = input('Select among: \n1) Relative error \n2) Absolute error \n3) Both\n')

     if selected_error == '1':
          relative_error_cos(x, tol)
     elif selected_error == '2':
          absolute_error_cos(x, tol)
     elif selected_error == '3':
          relative_error_cos(x, tol)
          absolute_error_cos(x, tol)


def sen(x, tol):
     selected_error = input('Select among: \n1) Relative error \n2) Absolute error \n3) Both\n')

     if selected_error == '1':
          relative_error_sen(x, tol)
     elif selected_error == '2':
          absolute_error_sen(x, tol)
     elif selected_error == '3':
          relative_error_sen(x, tol)
          absolute_error_sen(x, tol)


def absolute_error_cos(x, tol):
     n = 0
     fx = ((-1)**n) * (x**(2*n)) / math.factorial(2*n)
     fm, absolute_error = [], []
     absolute_error.append(100)
     fm.append(fx)

     while absolute_error[n] > tol:
          n += 1
          fx += ((-1)**n) * (x**(2*n)) / math.factorial(2*n)
          fm.append(fx)
          error = abs(fm[n] - fm[n-1])
          absolute_error.append(error)

     table = [absolute_error, fm]
     table = np.transpose(table)
     df = pd.DataFrame(table, columns = ['Absolute error', 'cos(x)'])
     print(df)


def relative_error_cos(x, tol):
     n = 0
     fx = ((-1)**n) * (x**(2*n)) / math.factorial(2*n)
     fm, relative_error = [], []
     relative_error.append(100)
     fm.append(fx)

     while relative_error[n] > tol:
          n += 1
          fx += ((-1)**n) * (x**(2*n)) / math.factorial(2*n)
          fm.append(fx)
          error = abs((fm[n] - fm[n-1]) / fm[n])
          relative_error.append(error)

     table = [relative_error, fm]
     table = np.transpose(table)
     df = pd.DataFrame(table, columns = ['Relative error', 'cos(x)'])
     print(df)


def absolute_error_sen(x, tol):
     n = 0
     fx = ((-1)**n) * (x**(2*n + 1)) / math.factorial(2*n + 1)
     fm, absolute_error = [], []
     absolute_error.append(100)
     fm.append(fx)

     while absolute_error[n] > tol:
          n += 1
          fx += ((-1)**n) * (x**(2*n + 1)) / math.factorial(2*n + 1)
          fm.append(fx)
          error = abs(fm[n] - fm[n-1])
          absolute_error.append(error)

     table = [absolute_error, fm]
     table = np.transpose(table)
     df = pd.DataFrame(table, columns = ['Absolute error', 'sen(x)'])
     print(df)


def relative_error_sen(x, tol):
     n = 0
     fx = ((-1)**n) * (x**(2*n + 1)) / math.factorial(2*n + 1)
     fm, relative_error = [], []
     relative_error.append(100)
     fm.append(fx)

     while relative_error[n] > tol:
          n += 1
          fx += ((-1)**n) * (x**(2*n + 1)) / math.factorial(2*n + 1)
          fm.append(fx)
          error = abs((fm[n] - fm[n-1]) / fm[n])
          relative_error.append(error)

     table = [relative_error, fm]
     table = np.transpose(table)
     df = pd.DataFrame(table, columns = ['Relative error', 'sen(x)'])
     print(df)


if __name__ == '__main__':
     main()