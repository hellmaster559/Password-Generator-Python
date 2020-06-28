import random
import string

inp = int(input("Enter The Length Of The Pass : "))

def randomString(inp):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(inp))

print("Your Pass Is Ready")
print (randomString(inp))