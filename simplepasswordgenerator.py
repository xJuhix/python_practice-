import random
import string

def generatePassword():

    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    #asks for the length of the desired password as an integer 
    length = int(input("Enter your desired password length: "))

    #this shuffles the characters
    random.shuffle(characters)

    #an empty list to append the characters
    password = []

    #loop for only picking the same amount of random characters as the desired password length 
    for i in range(length):
        password.append(random.choice(characters))

    #this randomly shuffles the chosen characters
    random.shuffle(password)

    #this converts the list to a string and prints it
    print("".join(password))

#calls the function
generatePassword()




