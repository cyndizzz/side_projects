weight = float(input("What's your weight in kilograms?\n"))
height = float(input("What's your height in meters?\n"))

bmi = round(weight / (height ** 2),2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you are normal weight")
else:
    print(f"Your BMI is {bmi}, you are overweight")