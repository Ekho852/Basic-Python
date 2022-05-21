# Fahrenehit to Celcius to Kelvin Converter

Celcius = -40
Fahrenheit = -40
Kelvin = 500

Celcius_to_Fahrenheit = Celcius * 9/5 + 32
Fahrenheit_to_Celcius = (Fahrenheit - 32) * (5/9)
Celcius_to_Kelvin = Celcius + 273.15
Kelvin_to_Celcius = Kelvin - 273.15

# Celcius to Fahrenheit
print(Celcius, "Celcius is", round(Celcius_to_Fahrenheit, 2), "Fahrenheit")
print()

# Fahrenheit to Celcius
print(Fahrenheit, "Fahrenheit is", round(Fahrenheit_to_Celcius, 2), "Celcius")
print()

# Celcius to Kelvin
print(Celcius, "Celcius is", round(Celcius_to_Kelvin, 2), "Kelvin")
print()

# Kelvin to Celcius
print(Kelvin, "Kelvin is", round(Kelvin_to_Celcius, 2), "Celcius")
print()