# average3.py
def main():
    sum = 0.0
    count = 0
    xStr = input("Enter a number (negative to quit) >> ")
    while xStr != '':
        xStr = eval(xStr)
        sum = sum + xStr
        count = count + 1
        xStr = input("Enter a number(negative to quit)>>")
    print("\n The average of the numbers is", sum/count)


main()
