"""
    Calculating the BMI of user and Classifying it
"""

'''
    Accepting user input.
'''

height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

'''
    Function to calculate the bmi score
'''


def bmi_cal(height_m, weight_kg):
    bmi = weight_kg / ((height_m / 100) ** 2)
    return bmi


def classify(bmi):
    """
        Classifying based on BMI score
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"


'''
    Function declaration 
'''

bmi_result = bmi_cal(height_m=height, weight_kg=weight)
result = classify(bmi_result)

'''
    Prompting final output
'''
print(f"Your BMI is {bmi_result:.4f}.")
print(f"Based on your BMI, you are classified as {result}.")
