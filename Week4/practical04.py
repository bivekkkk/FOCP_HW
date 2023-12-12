
#Q1
def checkint(a):
    return 0 <= a <= 100

result = checkint(100)
print(result)
#Q2
def countcase(a):
    uppercase=0
    lowercase=0
    for i in a:
        if i.isupper():
            uppercase+=1
        else:
            lowercase+=1
    return uppercase,lowercase
upper,lower=countcase("Test")
print(f"the number of uppercase is {upper} and lowercase={lower}")

#q3
name = input("Hello, what is your name? ")

if not name:
    print("Hello, Stranger!")
else:
    formatted_name = name[:1].upper() + name[1:].lower()
    print(f"Hello, {formatted_name}! Good to meet you!")

#q4
def remove_last_character(input_string):
    if len(input_string) > 1:
        return input_string[:-1]
    else:
        return input_string

input_str = "Hello, World!\n"
result = remove_last_character(input_str)

print(f"Original String: {input_str}")
print(f"Modified String: {result}")

#q5
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

celsius_temperature = 20
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)

print(f"{celsius_temperature} degrees Celsius is {fahrenheit_temperature:.2f} degrees Fahrenheit.")

converted_celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
print(f"The converted temperature back to Celsius: {converted_celsius_temperature:.2f} degrees Celsius.")

#q6

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
user_input = input("Enter the temperature in Celsius (eg. 25C): ")

if user_input.endswith('C') and user_input[:-1].replace('.', '', 1).isdigit():
    celsius_temperature = float(user_input[:-1])
    
    fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
    
    print(f"The equivalent temperature in Fahrenheit: {fahrenheit_temperature:.2f}F")
else:
    print("Invalid input. Please enter a valid temperature in the format 'numberC'.")
#q7
def celsius_to_fahrenheit(celsius):

    return (celsius * 9/5) + 32

min_temperature = float('inf')
max_temperature = float('-inf')
total_temperature = 0

for _ in range(6):
    user_input = input("Enter a temperature in Celsius (e.g., 25C): ")


    if user_input.endswith('C') and user_input[:-1].replace('.', '', 1).isdigit():
        celsius_temperature = float(user_input[:-1])

    
        fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)

        min_temperature = min(min_temperature, fahrenheit_temperature)
        max_temperature = max(max_temperature, fahrenheit_temperature)
        total_temperature += fahrenheit_temperature
    else:
        print("Invalid input. Please enter a valid temperature in the format 'numberC'.")

mean_temperature = total_temperature / 6

print(f"\nMaximum temperature: {max_temperature:.2f}F")
print(f"Minimum temperature: {min_temperature:.2f}F")
print(f"Mean temperature: {mean_temperature:.2f}F")


#q8
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


min_temperature = float('inf')
max_temperature = float('-inf')
total_temperature = 0
count = 0


while True:
    user_input = input("Enter a temperature in Celsius (or press Enter to finish): ")

    
    if not user_input:
        break

    
    if user_input.endswith('C') and user_input[:-1].replace('.', '', 1).isdigit():
        celsius_temperature = float(user_input[:-1])

        
        fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)

        
        min_temperature = min(min_temperature, fahrenheit_temperature)
        max_temperature = max(max_temperature, fahrenheit_temperature)
        total_temperature += fahrenheit_temperature
        count += 1
    else:
        print("Invalid input. Please enter a valid temperature in the format 'numberC'.")


if count > 0:
    
    mean_temperature = total_temperature / count


    print(f"\nMaximum temperature: {max_temperature:.2f}F")
    print(f"Minimum temperature: {min_temperature:.2f}F")
    print(f"Mean temperature: {mean_temperature:.2f}F")
else:
    print("No valid temperatures entered.")
