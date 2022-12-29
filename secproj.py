import typer

app = typer.Typer()

@app.command()
def timer(algorithm: str, filePath: str):
    print(f"encryption algorithm: {algorithm} file path: {filePath}")

if __name__ == "__main__":
    app()
