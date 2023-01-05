import typer
import os
import aestest

app = typer.Typer()

@app.command()
def aes(filepath: str, custom_path: bool = False):
    print(f"Running in secproj; filepath: {filepath} Is custom: {custom_path}")
    if(custom_path == False):
        encFilePath = os.path.join(filepath, "encrypted")
        decFilePath = os.path.join(filepath, "decrypted")
        if not(os.path.exists(encFilePath)):
            os.mkdir(encFilePath)
        if not(os.path.exists(decFilePath)):
            os.mkdir(decFilePath)
    else:
        encFilePath = input("Enter directory for saving encrypted files: ")
        decFilePath = input("Enter directory for saving decrypted files: ")
    aestest.aes_func(filepath, encFilePath, decFilePath)

@app.command()
def camellia(filepath: str, custom_path: bool = False):
    print(f"Running in secproj; filepath: {filepath} Is custom: {custom_path}")
    if(custom_path == False):
        encFilePath = os.path.join(filepath, "encrypted")
        decFilePath = os.path.join(filepath, "decrypted")
        if not(os.path.exists(encFilePath)):
            os.mkdir(encFilePath)
        if not(os.path.exists(decFilePath)):
            os.mkdir(decFilePath)
    else:
        encFilePath = input("Enter directory for saving encrypted files: ")
        decFilePath = input("Enter directory for saving decrypted files: ")
    camelliatest.camellia_func(filepath, encFilePath, decFilePath)

if __name__ == "__main__":
    app()
