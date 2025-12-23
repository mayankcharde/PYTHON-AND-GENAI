is_boiling = True  # means 1
stri_count = 5
#  here it add 5+1 =6 
total_actions = stri_count + is_boiling
print(f"total actions: {total_actions}")

milk_present =0  # false
print(f"is there milk? {bool(milk_present)}")

water_hot = True
tea_added = True

can_serve = water_hot  and tea_added
print(f"{can_serve}")
