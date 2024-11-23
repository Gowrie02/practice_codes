password = ""

while password != "secure123":
    password = input("give crt password")
    if password == "secure123":
        print('access granded',password)
    else:
        print("wrong password")
attempt = 0
while attempt >3:
    break
