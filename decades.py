# Ask the user for their age and convert the input to an integer
age = int(input("How old are you?\n"))

# Calculate how many full decades are in their age (integer division)
decades = age // 10                      
# Calculate the leftover years after removing the decades (modulus)
years = age % 10                         

# Print the result, converting numbers to strings so they can be joined in the sentence
print("You are " + str(decades) + " decades and " + str(years) + " years old.")  

