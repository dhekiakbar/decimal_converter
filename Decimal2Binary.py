print("Decimal to Binary conversion")
print("#############################")
print()

dec = int(input("Input your decimal number : "))

arr = []

while dec > 0 :
    temp = dec%2
    print(dec)
    arr.append(str(temp))
    dec = dec//2 

binary = "".join(arr[::-1])    

print("Binary : ", binary)