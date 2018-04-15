my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

my_height_cm = round(74 * 2.54)
my_weight_kg = round(180 * 0.45359237)

print (f"Let's talk about {my_name}.")
#print (f"He's {my_height} inches tall.")
print (f"He's {my_height_cm} centimeters tall.")
#print (f"He's {my_weight} pounds heavy.")
print (f"He's {my_weight_kg} kilograms heavy.")
print (f"Actually that's not too heavy.")
print (f"He's got {my_eyes} eyes and {my_hair} hair.")
print (f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height_cm + my_weight_kg
print (f"If I add {my_age}, {my_height_cm} and {my_weight_kg} I get {total}.")
