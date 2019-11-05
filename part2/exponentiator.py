def exponentiate(a, b):
    return a ** b

square = lambda x: exponentiate(x, 2)
cube = lambda x: exponentiate(x, 3)

def raise_to_fourth_power(x):
    return exponentiate(x, 4)

print(square(2))
print(cube(2))
print(raise_to_fourth_power(2))
