def quadrant(x, y):
    # Write your code here
    if x > 0:       # Positive X
        if y > 0:       # Positive Y
            quad = "I"
        elif y < 0:     # Negative Y
            quad = "IV"
        else:           # Y equal to 0
            quad = "X axis"
    elif x < 0:     # Negative X
        if y > 0:       # Positive Y
            quad = "II"
        elif y < 0:     # Negative Y
            quad = "III"
        else:           # Y equal to 0
            quad = "X axis"
    else:           # X equal to 0
        if y == 0:
            quad = "Origin"
        else:
            quad = "Y axis"
    return quad


def main():
    x = float(input("Enter X coordinate of the point: "))
    y = float(input("Enter Y coordinate of the point: "))
    print(f"The point is in quadrant: {quadrant(x, y)}")


if __name__ == '__main__':
    main()
