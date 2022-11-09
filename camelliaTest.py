import camellia
plain = b"This is a text. "
c1 = camellia.CamelliaCipher(key=b'16 byte long key', IV=b'16 byte iv. abcd', mode=camellia.MODE_CBC)
encrypted = c1.encrypt(plain)
