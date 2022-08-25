#usersinput
camelCase =  input("camelCase:")
#print "snake_case"
print("snake_case:",end="")

#loop through every letter
for letter in camelCase:
    #check if letter is uppercase
    if letter.isupper():
        print("_" + letter.lower(), end="")
    else:
        print(letter,end="")
print()