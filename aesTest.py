from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

myPlainTxt = "Hello how are you? Fine thank you. I have altered the deal.  2 + 2 is 4, minus 1 that's 3"
#b changes key into bytes
key = pad(b"mykey",AES.block_size) #pad will make key into byte size, specified by second parameter, in this case AES.block_size
iv=pad(b"myiv",AES.block_size) #initialization vector
