def is_leap(year):
    # Write your code here
    pass


def month_days(month, year):
    # Write your code here
    pass


def next_day(day, month, year):
    # Write your code here
    pass


def main():
    day = int(input("Enter the day: "))
    month = int(input("Enter the day: "))
    year = int(input("Enter the day: "))
    n_day, n_month, n_year = next_day(day, month, year)
    print(f"Next day: {n_day}/{n_month}/{n_year}")


if __name__ == '__main__':
    main()
