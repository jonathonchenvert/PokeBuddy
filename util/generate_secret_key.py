from os.path import dirname, abspath, exists, isfile
from django.utils.crypto import get_random_string


BASE_DIR = dirname(dirname(abspath(__file__)))
SECRET_KEY_FILE = f"{BASE_DIR}/PokeBuddy/secret_key"
KEY_LENGTH = 64

# Generate the key
lower_plus_numbers = (list(chr(o) for o in range(0x61, 0x7B)) + list(chr(o) for o in range(0x30, 0x3A)))
punctuation = list('!@#$%^&*(-_=+)')
upper_alpha = list(chr(o) for o in range(0x41, 0x5B))

# Thanks, Stack Overflow! https://stackoverflow.com/a/70821487/4858301
secret = get_random_string(KEY_LENGTH, allowed_chars=lower_plus_numbers + punctuation + upper_alpha,)

# Write key to file
with open(SECRET_KEY_FILE, 'x', newline=None, encoding='utf-8') as f:
    f.write(secret)

if exists(SECRET_KEY_FILE) and isfile(SECRET_KEY_FILE):
    print(f"{SECRET_KEY_FILE} has been created.")
else:
    print(f"{SECRET_KEY_FILE} could not be created.")

