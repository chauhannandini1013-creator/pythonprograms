def number_type(number):
    if number > 0:
        return "Positive"
    if number < 0:
        return "Negative"
    return "Zero"


if __name__ == "_main_":
    number = float(input("Enter a number: "))
    print(number_type(number))