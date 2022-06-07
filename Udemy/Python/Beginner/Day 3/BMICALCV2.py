# 🚨 Don't change the code below 👇

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


bmi = weight / (height**2)

if(bmi >=35):
    status = "clinically obese"
elif(bmi >=30):
    status = "obese"
elif(bmi >= 25):
    status = "overweight"
elif(bmi >= 18.5):
    status = "normal weight"
elif(bmi < 18.5):
    status = "underweight"

print(f"Your bmi is {round(bmi)}. You are {status}")

