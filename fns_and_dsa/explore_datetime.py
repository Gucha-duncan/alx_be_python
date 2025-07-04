import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    return f"The current date is: {current_date}"

today = display_current_datetime()
print(today)


def calculate_future_date():
    current_date = datetime.datetime.today()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + datetime.timedelta(days= number_of_days)  
    formatted_date = future_date.strftime("%Y-%m-%d")
    return f"Future date: {formatted_date}"

future_date = calculate_future_date()
print(future_date)

    