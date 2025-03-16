print("Decimal to Binary conversion")
print("#############################")
print()

dec = int(input("Input your decimal number : "))

arr = []

while dec > 0 :
    temp = dec%16
    print(dec)
    if temp == 10 :
        temp = "A"
    elif temp == 11 :
        temp = "B"
    elif temp == 12 :
        temp = "C"
    elif temp == 13 :
        temp = "D"
    elif temp == 14 :
        temp = "E"
    elif temp == 15 :
        temp = "F"
    arr.append(str(temp))
    dec = dec//16 
    
            
print(arr)
hex = "".join(arr[::-1])    

print("Hex : ", hex)