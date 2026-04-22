import string
import random 


store1 = list(string.ascii_lowercase)
store2 = list(string.ascii_uppercase)
store3 = list(string.digits)
store4 = list(string.punctuation)

user_input = input ("Yoo can you please tell me how many characters you want in your password?  ") # this will ask the users about the number of charaters they want
while True: 
    try:
        characters_length = int(user_input) # Take whatever the user typed into user_input, convert it into an integer number, and save it inside a new variable called characters_length
        if characters_length < 8: #
            print("Please put at least 8 numbers TY")
            user_input = input("Please, Enter your number again:    ")
        else:
            break
    except:
        print("Please, Enter numbers only.")
        user_input = input ("Yoo can you please tell me how many characters you want in your password?  ") # this will ask the users about the number of charaters they want

# here is the shuffle part for all listing - random.shuffle() mixes each list into a random order
random.shuffle(store1) 
random.shuffle(store2)
random.shuffle(store3)
random.shuffle(store4)

# calculate 30 / 20 of the number of characters
'''
This calculates percentages based on the password length.

example 
-  section 1 = 10 * 0.30 = 3 
- section 2 = 10 * 0.20 = 2

so then section 1 will use 3 and section 2 will use 2

so the password will use:
3 lowercase letters
3 uppercase letters
2 digits
2 symbols

in total it will look like this : 3 + 3 + 2 + 2 = 10 characters
'''
section1 = round(characters_length * (30/100))
section2 = round(characters_length * (20/100))

# this will generation of the password | 60% letters and 40% digitis and punctuations
result = [] # this will hold all the password characters before joining them into on string

for x in range(section1):
    result.append(store1[x]) # one lowercase letter
    result.append(store2[x]) # one uppercase letter
for x in range(section2):
    result.append(store3[x])
    result.append(store4[x])

# shuffle result - this will shuffle it again to mix the final password 
random.shuffle(result)
# big output
password = "".join(result) #  turn the list into a string 
print("Strong Password: ", password) # after the final string will get stored in "password"
