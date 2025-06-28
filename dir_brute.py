import typer
import requests

def dir_brute(
    url: str = typer.Option(..., "--url", "-u", help="Target base URL (e.g., http://example.com)"),
    wordlist: str = typer.Option(...,"--wordlist","-w", help="Path to wordlist file"),
    status: int = typer.Option(200, "--status", "-s", help="Status code to filter for (default: 200)")
):
    try:
        with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
            words = f.read().splitlines()
    except FileNotFoundError:
        typer.echo(f"[!] Wordlist not found: {wordlist}")
        raise typer.Exit()
    
    typer.echo(f"[*] Starting directory brute-force on: {url} (Expecting status: {status})")

    for word in words:
        full_url = f"{url.rstrip('/')}/{word}"
        try:
            response = requests.get(full_url, timeout=3)
            if response.status_code in [200, 301,302]:
                typer.echo(f"[+] Found: {full_url} (Status: {response.status_code})")

        except requests.RequestException:
            pass        
