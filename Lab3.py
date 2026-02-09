ذّذذ
password = input("Enter password: ")
if password == "admin123":
    print("Access Granted")
else:
    print("Access Denied")


age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teen")
elif 20 <= age <= 59:
    print("Adult")
else:
    print("Senior")


number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
else:
    print("Not Positive")
if 10 <= number <= 50:
    print("Number is between 10 and 50")
else:
    print("Number is not between 10 and 50")


colour = input("Enter a colour (red, yellow, green): ")
if colour:
    match colour:
        case "red":
            print("Stop")
        case "yellow":
            print("Slow Down")
        case "green":
            print("Go")
        case _:
            print("Unknown colour")
else:
    print("Input cannot be empty")


print("Menu:\n1- Addition\n2- Subtraction\n3- Multiplication\n4- Division")
choice = input("Choose an option: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
match choice:
    case "1":
        print("Result:", num1 + num2)
    case "2":
        print("Result:", num1 - num2)
    case "3":
        print("Result:", num1 * num2)
    case "4":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid option")


score = float(input("Enter student score: "))
if score >= 50:
    print("Passed")
else:
    print("Failed")
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
match grade:
    case "A":
        print("Excellent!")
    case "B":
        print("Very Good!")
    case "C":
        print("Good!")
    case "D":
        print("Needs Improvement")
    case "F":
        print("Failing")