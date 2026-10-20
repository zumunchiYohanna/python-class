print("Temperature Converter")
print("C: Celsius to Fahrenheit")
print("F: Fahrenheit to Celsius")

conversion = input("Choose a conversion (C or F): ").strip().lower()

if conversion == "c":
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius} C is {fahrenheit} F")
elif conversion == "f":
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit} F is {celsius} C")
else:
    print("Invalid choice. Enter C or F.")