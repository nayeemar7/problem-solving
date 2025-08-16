def tempconversion(n):
    return (n * 9/5) + 32

celsius = float(input("Enter temperature in celsius: "))
fahrenheit = tempconversion(celsius)
print("Temperature in Fahrenheit:", fahrenheit)
