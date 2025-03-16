print("Decimal to Binary conversion")
print("#############################")
print()

dec = int(input("Input your decimal number : "))

arr = []

while dec > 0 :
    temp = dec%8
    print(dec)
    arr.append(str(temp))
    dec = dec//8 
    
            
print(arr)
oct = "".join(arr[::-1])    

print("Octal : ", oct)