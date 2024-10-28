import  random
import  string

uppercase = random.choices(string.ascii_uppercase, k=3)
lowercase = random.choices(string.ascii_lowercase, k=3)
number = random.choices(string.digits, k=3)
symbols = random.choices(string.punctuation, k=3)
password = uppercase + lowercase + number + symbols
random.shuffle(password)
print(''.join(password))