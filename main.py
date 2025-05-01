import random
import string
length = int(input("Enter the length of the password: "))
all_charecters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(all_charecters) for _ in range(length))
print(f"the generated password is : {password}")