import time
from cryptography.fernet import Fernet

#starting timer
start = time.perf_counter()

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"my deep dark secret")

print("Encrypted: ", token)
middle = time.perf_counter()
print(f'Finished encryption in {round(middle-start, 2)} second(s)')

plaintext = f.decrypt(token)
print("after: ", plaintext)

finish = time.perf_counter()
print(f'Finished overall in {round(finish-start, 2)} second(s)')
