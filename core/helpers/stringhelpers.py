import random
import string

def generate_random_keystring(length):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

