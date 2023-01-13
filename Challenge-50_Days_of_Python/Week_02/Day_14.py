# Day_14: Your Salary

def your_salary():
    """
        Takes userinput for Name, Periods taught and Rate per period
        Returns formatted output of Name, Periods and Gross monthly Salary
    """
    rate_per_period = 20
    overtime_rate = 25
    while True:
        teacher = input("\n Enter Name: \t").title()
        period = int(input("\n Enter Number of Periods Taught: \t"))
        if period > 100:
            overtime_pay = (period - 100) * overtime_rate
        else:
            overtime_pay = 0
        rate = int(input("\n Enter agreed rate per period: \t"))
        if rate != rate_per_period:
            rate = int(input("\n Enter agreed rate per period: \t"))
        gross_monthly_salary = (period * rate) + overtime_pay
        print(
            f"\nTeacher: {teacher},\nPeriods: {period},\nGross Monthly Salary: {gross_monthly_salary}")
        print("\nDo you want to confirm entry or try another name?? yes or no")
        choice = input("\nChoice:    ")
        if choice == "no":
            break


your_salary()
