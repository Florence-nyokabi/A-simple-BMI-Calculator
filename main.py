# BMI Calculator

print("******************************************************************************")
print("****************************  BMI CALCULATOR  ********************************")
print("******************************************************************************")


m = int(input("Enter your height: "))
kg = int(input("Enter your weight in kilograms: "))
gender = input("Gender (m/f): ")

BMI = kg / ((m / 100) * (m / 100))

if BMI < 19 and gender == "f":
    print("-> Underweight")
if BMI >= 19 and BMI <= 24 and gender == "f":
    print("-> Normal")
if BMI > 24 and gender == "f":
    print("-> Overweight")
if BMI < 20 and gender == "m":
    print("-> Underweight")
if BMI >= 20 and BMI <= 25 and gender == "m":
    print("-> Normal")
if BMI > 25 and gender == "m":
    print("-> Overweight")