# Arithmetic operators
a = 10
b = 3
print("Addition:", a + b)  # 13
print("Subtraction:", a - b)  # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)  # 3.3333
print("Floor Division:", a // b)  # 3
print("Modulus:", a % b)  # 1
print("Exponentiation:", a**b)  # 1000

# Comparison operators
print("Equal:", a == b)  # False
print("Not Equal:", a != b)  # True
print("Greater than:", a > b)  # True
print("Less than:", a < b)  # False
print("Greater than or equal to:", a >= b)  # True
print("Less than or equal to:", a <= b)  # False

# Logical operators
x = True
y = False

print("Logical AND:", x and y)  # False
print("Logical OR:", x or y)  # True
print("Logical NOT:", not x)  # False

# Membership operators
my_list = [1, 2, 3, 4, 5]
print("Membership IN:", 3 in my_list)  # True
print("Membership NOT IN:", 6 not in my_list)  # True

# Identity operators
c = a
print("Identity IS:", a is c)  # True
print("Identity IS NOT:", a is not b)  # True

# Assignment operators
d = 5
d += 2  # d = d + 2
print("Assignment += :", d)  # 7
d *= 3  # d = d * 3
print("Assignment *= :", d)  # 21
d -= 4  # d = d - 4
print("Assignment -= :", d)  # 17
d /= 2  # d = d / 2
print("Assignment /= :", d)  # 8.5
d %= 3  # d = d % 3
print("Assignment %= :", d)  # 2.5
d **= 2  # d = d ** 2
print("Assignment **= :", d)  # 6.25
d //= 2  # d = d // 2
print("Assignment //= :", d)  # 3.0
