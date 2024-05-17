from sympy import Symbol, limit, sin, oo

# Define the variable
x = Symbol('x')

# Define the functions
f = 2 * x + 5
g = sin(x) / x

# Calculate the limit as x approaches 3
result1 = limit(f, x, 3)
# Calculate the limit as x approaches 0
result2 = limit(g, x, 0)
# Calculate the limit as x approaches infinity
result3 = limit(f, x, oo)

print(f'Limit as x approaches 3: {result1}')
print(f'Limit as x approaches 0: {result2}')
print(f'Limit as x approaches infinity (oo): {result3}')
