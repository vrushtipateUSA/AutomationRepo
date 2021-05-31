Hourly_rate = int(input("enter the hourly rate"))
Hours_worked = int(input("How many days have you worked"))

emp_salary = Hourly_rate * Hours_worked

if Hours_worked <= 40:
    print("emp_salary", Hourly_rate * Hours_worked)
elif Hours_worked > 40:
    print()