print("Please enter the temperature in Fahrenheit")
f = input()

def temp_convert(f):
    celsius = (int(f)-32)*(5/9)
    return "Temperature in Celsius is {}C.".format(round(celsius))

print(temp_convert(f))