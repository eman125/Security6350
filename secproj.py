import typer
import aesTest

app = typer.Typer()

@app.command()
def main(alg: str, filepath: str):
    print(f"Running in secproj; alg: {alg} filepath: {filepath}")

if __name__ == "__main__":
    app()
