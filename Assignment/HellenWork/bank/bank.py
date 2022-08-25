#prompt user to input datas
answer = input("Greeting:")

character = answer.lower().strip()

#if the answer has hello print $0
if 'hello' in character:
    print("$0")
#check if answer starts with 'h, print$20
elif 'h' == character[0]:
    print("$20")
else:
    print("$100")