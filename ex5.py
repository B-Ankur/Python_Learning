my_name = "Zed A. Shah"
my_age = 35 
my_height = 74
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

# We embed variable inside astring using {}
# 'f' stands for "format". It tells Python the string needs to be formatted.
print(f"Let's talk about {my_name}.")
print(f"He is {my_height} inches tall.")
print(f"He is {my_weight} pound heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"He's teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
