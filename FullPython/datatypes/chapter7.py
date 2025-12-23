masala_spices = ("cardamom", "cloves", "cinnamon")
#  BASICALLY WE ASSIGN THE VALUES IN BELOW 3 SPICES
(spice1, spice2 , spice3) = masala_spices
#  HERE WE PRINT 
print(f"main masala spices : {spice1}, {spice2}, {spice3}")


#  ASSIGN THE INTEGER TO EACH OF THEM
ginger_ratio , cardmon_ratio =2,1
print(f"ratio is g : {ginger_ratio} and {cardmon_ratio}")

# HERE WE SWAP THE VALUES OF BOTH 
ginger_ratio , cardmon_ratio = cardmon_ratio, ginger_ratio

#  PRINT THE SWAPED VALUE 
print(f"ratio is G: {ginger_ratio} and {cardmon_ratio}")


#  WE APPLY CHECK HERE 
#  ANSWER WILL TRUE IN BOOLEAN
print(f" is cinnamon in masala spices ?  {'cinnamon' in masala_spices}")