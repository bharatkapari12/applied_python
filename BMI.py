
def calculate_bmi(weight_pound, height_inches):
  
  weight_kg = weight_pound * 0.45359237
  height_meters = height_inches * 0.0254

  bmi = weight_kg / height_meters ** 2

  return bmi

def showBMI(bmi):
  if bmi < 18.5:
    return 'underweight'
  elif bmi >= 18.5 and bmi < 25.0:
    return 'normal'
  elif bmi >= 25 and bmi < 30:
    return 'overwieght'
  else:
    return 'obese'
  
def main():
  weight_pounds=float(input("enter height in pounds: "))
  height_inches=float(input("enter height in inches: "))

  bmi = calculate_bmi(weight_pounds,height_inches)

  bmi_show = showBMI(bmi)

  print(f"your bmi is {bmi} and you are {bmi_show}")

main()










# def calculate_bmi(weight_pounds, height_inches):
#     # Conversion factors
#     pounds_to_kg = 0.45359237
#     inches_to_meters = 0.0254

#     # Convert weight and height to kg and meters
#     weight_kg = weight_pounds * pounds_to_kg
#     height_meters = height_inches * inches_to_meters

#     # Calculate BMI
#     bmi = weight_kg / (height_meters ** 2)

#     return bmi

# def interpret_bmi(bmi):
#     if bmi < 18.5:
#         return "Underweight"
#     elif 18.5 <= bmi < 25.0:
#         return "Normal"
#     elif 25.0 <= bmi < 30.0:
#         return "Overweight"
#     else:
#         return "Obese"

# # Input from the user
# weight_pounds = float(input("Enter your weight in pounds: "))
# height_inches = float(input("Enter your height in inches: "))

# # Calculate BMI
# bmi = calculate_bmi(weight_pounds, height_inches)

# # Interpret BMI
# interpretation = interpret_bmi(bmi)

# # Display the result
# print(f"Your BMI is {bmi:.2f}, which is classified as '{interpretation}'.")










# def calculate_bmi(weight_pounds, height_inches):

#   weight_kg = weight_pounds * 0.45359237
#   height_meters = height_inches * 0.0254
  
# #   calculation of BMI
#   bmi = weight_kg / (height_meters ** 2)
  
#   return bmi


# def main():

#   weight_pounds = float(input("Enter your weight in pounds: "))
#   height_inches = float(input("Enter your height in inches: "))
  
#   # Calculate BMI
#   bmi = calculate_bmi(weight_pounds, height_inches)

#   print("Your BMI is", bmi)


# if __name__ == "__main__":
#   main()




