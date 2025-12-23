flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == 'out of stock':
        continue
    if flavour == 'discontinued':
        print(f"{flavour} item found")
        break
    print(f"{flavour} item found")
    
print(f"out of the loop")    