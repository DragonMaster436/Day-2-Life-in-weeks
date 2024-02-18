# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_as_int = int(age)

total_days = 365 * 90
total_weeks = 52 * 90
total_months = 12 * 90

age_days = age_as_int * 365
age_weeks = age_as_int * 52
age_months = age_as_int * 12

final_days = total_days - age_days
final_weeks = total_weeks - age_weeks
final_months = total_months - age_months



print(f"You have {final_days} days, {final_weeks} weeks, and {final_months} months left.")


