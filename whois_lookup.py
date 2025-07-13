import typer
import whois
from pathlib import Path
from typing import Optional
from datetime import datetime

def whois_lookup(
    domain: str = typer.Option(..., help="Target domain (e.g. example.com)"),
    save: Optional[Path] = typer.Option(None, help="Optional: Save the WHOIS data to a file"),
    short: bool = typer.Option(False, "--short", help="show only key fields")
):
    print(f"[*] Performing WHOIS lookup for: {domain}")

    try:
        result = whois.whois(domain)

        if result.expiration_date:
            expiry = result.expiration_date
            if isinstance(expiry, list):
                expiry = expiry[0]
            if isinstance(expiry, datetime):
                if expiry < datetime.now():
                    print("[!] the domain appears to be expired.")
                else:
                    print(f"[+] Domain expires on: {expiry}")

        if short:
            summary = (
                f"[+] Domain: {domain}\n"
                f"[+] Registrar: {result.registrar}\n"
                f"[+] Creation: {result.creation_date}\n"
                f"[+] Expiration: {result.expiration_date}\n"
                f"[+] Name Servers: {result.name_servers}"
            )
            print(summary)

        output = str(result)
        print(output)
        
        if save:
            with open(save, "w", encoding="utf-8") as f:
                f.write(output)
            print(f"[+] Output saved to {save}")

    except Exception as e:
        print(f"[!] error: {e}")            

