# Security6350
This started as a project for Wireless Security 6350 class at UTPB.  It started as 2 python 
files meant to encrypted then decrypt files using either AES or Camellia cipher and compare how 
long the process takes between the two ciphers.

For the first release, this will be a command line tool where the user will be able to specify 
a cipher and a folder on their machine, then the tool will encrypt and write the encrypted 
files, decrypt and write again, then print how long the process took in seconds.  The tool will 
maintain the original files.

The secproj.py file serves as the main file, and uses the typer python package for the command 
line interface.  The aestest.py and camelliatest.py files do the 
actual encryption and decryption, and utilize the Fernet and Camellia python packages 
respectively.
