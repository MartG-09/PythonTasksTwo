def  convert_fahrenheit_to_celsius_and_vice_versa(temperature, unit = "C" , threshold = 40):
    unit = unit.upper()
    if unit == "C":
        temp = (temperature * 9/5) + 32
        thresh = (threshold * 9/5) + 32

    elif unit == "F":
        temp = (temperature - 32) * (5/9)        
        thresh = (threshold - 32) * (5/9)

    if (temp > thresh):
        return " Heat alert"
    else:
        return " Cold advisory"

temperature = 95
print(convert_fahrenheit_to_celsius_and_vice_versa(temperature , "f" , 100))
