import string
import random 

# This is for getting the password length from user
store1 = list(string.ascii_lowercase)
store2 = list(string.ascii_uppercase)
store3 = list(string.digits)
store4 = list(string.punctuation)

user_input = input ("Yoo can you please tell me how many characters you want in your password?  ") # this will ask the users about the number of charaters they want
while True: 
    try:
        characters_length = int(user_input)
        if characters_length < 8:
            print("Please put at least 8 numbers TY")
            user_input = input("Please, Enter your number again:    ")
        else:
            break
    except:
        print("Please, Enter numbers only.")
        user_input = input ("Yoo can you please tell me how many characters you want in your password?  ") # this will ask the users about the number of charaters they want

# here is the shuffle part for all listing 
random.shuffle(store1) 
random.shuffle(store2)
random.shuffle(store3)
random.shuffle(store4)

# calculate 30 / 20 of the number of characters
section1 = round(characters_length * (30/100))
section2 = round(characters_length * (20/100))

# this will generation of the password | 60% letters and 40% digitis and punctuations
result = []

for x in range(section1):
    result.append(store1[x])
    result.append(store2[x])
for x in range(section2):
    result.append(store3[x])
    result.append(store4[x])

# shuffle result 
random.shuffle(result)
# big output
password = "".join(result)
print("Strong Password: ", password)
