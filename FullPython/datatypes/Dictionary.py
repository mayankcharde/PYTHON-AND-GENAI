chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

#  HERE WE CREATE A EMPTY DICTIONARY AND ADDDING THE KEY VALUE PAIRS TO IT 
chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe: {chai_recipe}")

#  DELETING THE LIQUID FROM DICTIONARY
del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")

print(f"Is sugar in the order? {'sugar' in chai_order}")


#  HERE WE CREATE A DICTIONARY
chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}

last_item = chai_order.popitem()
print(f"removed last item: {last_item}")

#  HERW WE ARE ADDING 2 DICTIONARY
extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
print(f"updated chai recipe: {chai_recipe}")


customer_note = chai_order.get("size", "No Note")
print(f" customer_note is: {customer_note}")


