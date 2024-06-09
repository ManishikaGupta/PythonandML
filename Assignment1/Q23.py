'''Write a program that converts temperature from Celsius to Fahrenheit
and vice versa based on user input.'''
tempFah=float(input("Enter the Temperature in Fahrenheit:"))
tempCel=float(input("Enter the Temperature in Celcius:\n"))
celcius=5.0/9.0*(tempFah-32)
Fahrenheit=(tempCel*9/5)+32
print("Temperature in Fahrenheit={}".format(Fahrenheit))
print("Temperature in Celcius ={}\n".format(celcius))

