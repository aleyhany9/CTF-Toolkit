import typer
import requests
from pathlib import Path
from typing import Optional

def admin_finder(
        url: str = typer.Option(..., help="Target base URL (e.g. http://example.com)"),
        wordlist: Path = typer.Option(..., exists=True, readable=True, help="Path to wordlist file"),
        status: Optional[int] = typer.Option(None, help="Only show matching status code (e.g. 200)"),
        save: Optional[Path] = typer.Option(None, help="Optional: Save found paths to file")
):
    print(f"[*] Starting admin panel scan on: {url}")
    found= []

    try:
        paths = wordlist.read_text(encoding="utf-8").splitlines()

        for path in paths:
            if not path.startswith("/"):
                path = "/" + path
            full_url = url.rstrip("/") + path    

            try:
                response = requests.get(full_url, timeout=5)
                if status:
                    if response.status_code == status:
                        line = f"[+] {full_url} [{response.status_code}]"
                        print(line)
                        found.append(line)

                else:
                    line = f"[+] {full_url} [{response.status_code}]"
                    print(line)
                    found.append(line)        
            except requests.RequestException as e:
                print(f"[!] Error with {full_url}: {e}")            
        if save:
            with open(save, "w", encoding="utf-8") as f:
                f.write("\n".join(found))
            print(f"[+] Results saved to {save}")    
    except Exception as e:
                print(f"[! Faild to read wordlist or scan: {e}")