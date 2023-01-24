from data import data

user_input = input("What code do you wish to convert : ").lower()
morse_word = ""

for char in user_input:
    if char in data:
        morse_word += data[char]
    else:
        morse_word += char

print(f"The morsed word for your input is : {morse_word}")
