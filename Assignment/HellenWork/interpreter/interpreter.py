#user input
expression = input("Expression: ")

#covert into variables
x,y,z = expression.split(" ")
#convert variable x and z to float
new_x = float(x)
new_z = float(z)

#Calculate result
if y == "+":
    result = new_x + new_z
if y == "-":
    result = new_x - new_z
if y == "*":
    result = new_x * new_z
if y == "/":
    result = new_x / new_z

print(result)