import typer
import requests
from typing import Optional
from pathlib import Path


def http_headers(
        url: str = typer.Option(..., help="Target URL (e.g. http://example.com)"),
        save: Optional[Path] = typer.Option(None, help="Save header to a file"),
        show_status: bool = typer.Option(True, "--status/--no-status", help="Show HTTP response status code (default: true)")
):
    print(f"[*] Getting headers for: {url}")

    try:
        response = requests.get(url, timeout=5)

        if show_status:
            print(f"[+] Status code: {response.status_code}\n")

        print("[+] Responce Headers:\n")
        for  key, value in response.headers.items():
            print(f"{key}: {value}")

        if save:
            with open(save, "w", encoding="utf-8") as f:
                for key, value in response.headers.items():
                    f.write(f"{key}: {value}\n")

            print(f"\n[+] Headers saved to: {save}")        

    except requests.exceptions.RequestException as e:
        print(f"[!] Error: {e}")

            