def largest_of_three(num1, num2, num3):
    # Write your code here
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3
    else:    # num2 is >= num1
        if num2 > num3:
            return num2
        else:
            return num3


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    print(largest_of_three(a, b, c))


if __name__ == '__main__':
    main()
