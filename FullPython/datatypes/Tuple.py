essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

#  IT WILL GIVE ALL SPICES FROM TUPLE
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

# GIVE COMMON ITEM NAME FROM TUPLE
common_spices = essential_spices & optional_spices
print(f"common spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices: {only_in_essential}")


print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")