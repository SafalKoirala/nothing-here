#temperature conversion

tmp =float(input("Enter the temperature in Fahrenheit : "))

celsius = (tmp-32)/1.8
celsius = round(celsius, 4)
kelvin = celsius+273.15
kelvin = round(kelvin, 4)

print("Degree Fahrenheit : "+ str(tmp))
print("Degree Celsius : "+ str(celsius))
print("Degree Kelvin : "+ str(kelvin))
