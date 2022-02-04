"""HW1 Problem 1, developed by Kimlong Nguyen 10.5.21.

This app computes and displays the calorie content 
of a food item in terms of protein, carbs, fat, and total,
given the weight (grams) of each item.
Inputs (from user): weight in grams for protein (float), carb (float), and fat (float)
Output: weight in grams for protein (float), carb (float), fat (float), and total calories (float). 
"""

#inputs
protein_weight = float(input('Enter the weight of protein (grams): '))
carb_weight = float(input('Enter the weight of carb (grams): '))
fat_weight = float(input('Enter the weight of fat (grams): '))

#initialization
fat_cal_unit = 9.0
protein_cal_unit = 4.0
carb_cal_unit = 4.0

#computations
#Total calories is computed by summing the total calories of each essential nutrient. 
#Each nutrient calories is calculated by multiplying its weight by the corresponding calories per gram.
total_cal = (protein_weight * protein_cal_unit) + (carb_weight * carb_cal_unit) + (fat_weight * fat_cal_unit)

#outputs
print('Contents contain')
print(f'{protein_weight:.2f} grams of protein,')
print(f'{carb_weight:.2f} grams of carbs,')
print(f'{fat_weight:.2f} grams of fat,')
print(f'resulting in a total of {total_cal:.2f} calories')