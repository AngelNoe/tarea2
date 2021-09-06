def parking_cost(hours, minutes):
    # Write your code here
    cost = 0
    if hours == 0 and minutes == 0:
        cost = 0
    elif hours < 2:
        cost = 5
    elif hours == 2 and minutes > 0:
        cost = 17
    else:
        cost = 5 + (hours - 2) * 12
        if minutes <= 15:
            cost += 5
        elif minutes <= 30:
            cost += 8
        elif minutes <= 45:
            cost += 10
        elif minutes <= 60:
            cost += 12
    return cost


def main():
    hours = int(input("Enter number of hours: "))
    minutes = int(input("Enter number of minutes: "))
    print(parking_cost(hours, minutes))


if __name__ == '__main__':
    main()
