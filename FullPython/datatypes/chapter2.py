spice_mix = set()
print(f"initial spice mix id: {id(spice_mix)}")
print(f"initial spice mix id: {spice_mix}")

spice_mix.add("Ginger")
spice_mix.add("cardmon")
spice_mix.add("lemon")

print(f"initial spice mix id: {spice_mix}")
#  the id is same as above because we are only add items in sets
print(f"initial spice mix id: {id(spice_mix)}")