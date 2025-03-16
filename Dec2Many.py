def binary_conv(dec):
    arr = []
    while dec > 0 :
        temp = dec%2
        arr.append(str(temp))
        dec = dec//2 
    binary_rst = "".join(arr[::-1]) 
    return binary_rst 

def octal(dec):
    arr = []
    while dec > 0 :
        temp = dec%8
        arr.append(str(temp))
        dec = dec//8 
    octal_rst = "".join(arr[::-1])   
    return octal_rst

def hex(dec):
    arr = []
    while dec > 0 :
        temp = dec%16
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
    hex_rst = "".join(arr[::-1])  
    return hex_rst


print("Decimal to Binary conversion")
print("#############################")
print()
dec = int(input("Input your decimal number : "))

print("Binary : ",binary_conv(dec))
print("Octal : ", octal(dec))
print("Hexadecimal : ", hex(dec))