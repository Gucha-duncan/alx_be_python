FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR



def convert_to_fahrenheit(celsius) :
    
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def get_valid_temperature(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")

    

def main():
 pass
 
    
    