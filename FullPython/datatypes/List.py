# THIS IS A LIST 
ingredients = ["water", "milk", "black tea"]
# APPENDING THE ITEM 
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
#  REMOVING THE ITEM FORM LIST
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

#  MAKING ANOTHER 2 LIST
spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

#  EXTENDS MEANS JOINS TWO LIST FROM ABOVE 2 LISTS
chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")

# INSERTING THE VALUE IN 2ND INDEX 
chai_ingredients.insert(2, "black tea")
print(f"chai: {chai_ingredients}")

#  POOPING OR REMOVING THE ITEM FROM LST
last_added = chai_ingredients.pop()
print(f"{last_added}")

print(f"chai: {chai_ingredients}")

#  HERE WE REVERING THE PLACE OF EVERY ITEM IN THE LIST
chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")

#  IT WILL SORT THE LIST IN ASCENDING ORDER 
chai_ingredients.sort()
print(f"chai: {chai_ingredients}")

#  MAKE ANOTHER LIST
sugar_levels = [1, 2, 3, 4, 5]
#  IT TELLS US MAX AND MIN VALUE OF LIST
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")

#  MAKED ANOTHER 2 LISTS
base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

#  CONCATINATING TWO LISTS BELOW 
full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix: {full_liquid_mix}")

# ITEMS PRINT 3 TYPES WHEN MULTIPLY FROM 3 
strong_brew = ["black tea", "water"] * 3
print(f"String brew: {strong_brew}")


raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")