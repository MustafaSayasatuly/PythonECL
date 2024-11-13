height=float(input("what is your height?"))
weight=float(input("what is your weight?"))
BMI=weight/(height)**2
print(BMI)

if BMI<=18.4:
  print("you are underwheight")
elif 18.5<=BMI and BMI<=24.9:
  print("you are normal")
elif 25.0<=BMI and BMI<=39.9:
  print("you are overweight")
else:
  print("you are obese")