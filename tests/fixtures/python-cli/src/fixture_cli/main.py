import os
import typer
import httpx

app = typer.Typer()

API_TOKEN = os.getenv("FIXTURE_API_TOKEN")
BASE_URL = os.getenv("FIXTURE_BASE_URL", "https://api.example.com")


@app.command()
def fetch(path: str):
    if not API_TOKEN:
        typer.echo("FIXTURE_API_TOKEN is required", err=True)
        raise typer.Exit(1)
    r = httpx.get(f"{BASE_URL}{path}", headers={"Authorization": f"Bearer {API_TOKEN}"})
    typer.echo(r.text)


if __name__ == "__main__":
    app()
