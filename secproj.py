import typer
import aestest

app = typer.Typer()

@app.command()
def aes(filepath: str, custom_path: bool = False):
    print(f"Running in secproj; filepath: {filepath} Is custom: {custom_path}")
    aestest.aes_func(filepath)

@app.command()
def camellia(filepath: str, custom_path: bool = False):
    print(f"Running in secproj; filepath: {filepath} Is custom: {custom_path}")

if __name__ == "__main__":
    app()
