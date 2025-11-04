# If condition

a = 10

if a > 5:
    print("a is greater than 5")
else:
    print("a is not greater than 5")

# Elif condition
if a < 5:
    print("a is less than 5")
elif a == 5:
    print("a is equal to 5")
else:
    print("a is greater than 5")

# Nested if condition
if a > 5:
    if a == 10:
        print("a is equal to 10")
    else:
        print("a is not equal to 10")
        
# Ternary operator
print("a is greater than 5" if a > 5 else "a is not greater than 5")

