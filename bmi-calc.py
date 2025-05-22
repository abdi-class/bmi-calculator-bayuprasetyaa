# Create BMI calculator fundamental program

print("Welcome to the BMI calculator!")
print("Please enter your weight in kilograms:")
weight = float(input())
print("Please enter your height in meters:")
height = float(input())
print("Calculating your BMI...")
bmi = weight / (height ** 2)
print("Your BMI is: " + str(bmi))
print("Your BMI category is: ", end="")
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight")