import typer
import requests

def subdomain_enum(
        domain: str = typer.Option(..., "--domain", "-d", help="Target domain (e.g., examplae.com)"),
        wordlist: str = typer.Option(..., "--wordlist", "-w", help="Path to subdomain wordlist file"),
        status: int = typer.Option(None, "--status","-s", help="Filter by HTTP status code")
):
    try:
        with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
            subdomains = f.read().splitlines()
    except FileNotFoundError:
        typer.echo(f"[!] wordlist not found: {wordlist}")
        raise typer.Exit()
    
    found = []    
    typer.echo(f"[*] Starting subdomain enumeration for: {domain}")

    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url, timeout=3)
            if status is None or response.status_code == status:
                typer.echo(f"[+] Found: {url} (Status: {response.status_code})")
                found.append(url)
        except requests.RequestException:
            pass    
    
    if not found:
        typer.echo("[-] NO matching subdomains found.")