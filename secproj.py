import typer
import aestest

app = typer.Typer()

@app.command()
def main(alg: str, filepath: str):
    print(f"Running in secproj; alg: {alg} filepath: {filepath}")
    aestest.aes_func(filepath)

if __name__ == "__main__":
    app()
