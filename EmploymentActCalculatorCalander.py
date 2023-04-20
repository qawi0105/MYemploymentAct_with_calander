import calendar

# Define a function to calculate basic rate of pay
def calculate_basic_rate():
    total_salary = float(input("Enter your total monthly salary: "))
    working_days = int(input("Enter the number of working days in the month: "))

    basic_rate = total_salary / working_days
    print("Your basic rate of pay is RM {:.2f} per day.".format(basic_rate))

# Display the calendar and prompt the user to select a date
print("Welcome to the Employment Act Calculator!")
print("Please select a month and year:")

year = int(input("Enter the year (e.g. 2023): "))
month = int(input("Enter the month as a number (e.g. 1 for January): "))

cal = calendar.monthcalendar(year, month)
for week in cal:
    print(week)

selected_week = int(input("Enter the week number: "))
selected_day = int(input("Enter the day of the week as a number (0 for Monday, 6 for Sunday): "))

selected_date = cal[selected_week][selected_day]

print("You have selected {} {}/{}.".format(calendar.day_name[selected_day], selected_date, month))

# Call the function to calculate basic rate of pay
calculate_basic_rate()
