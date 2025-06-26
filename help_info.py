import typer

def show_help():
    typer.echo(r"""
  /$$$$$$  /$$$$$$$$ /$$$$$$$$       /$$$$$$$$ /$$$$$$   /$$$$$$  /$$       /$$   /$$ /$$$$$$ /$$$$$$$$
 /$$__  $$|__  $$__/| $$_____/      |__  $$__//$$__  $$ /$$__  $$| $$      | $$  /$$/|_  $$_/|__  $$__/
| $$  \__/   | $$   | $$               | $$  | $$  \ $$| $$  \ $$| $$      | $$ /$$/   | $$     | $$
| $$         | $$   | $$$$$            | $$  | $$  | $$| $$  | $$| $$      | $$$$$/    | $$     | $$
| $$         | $$   | $$__/            | $$  | $$  | $$| $$  | $$| $$      | $$  $$    | $$     | $$
| $$    $$   | $$   | $$               | $$  | $$  | $$| $$  | $$| $$      | $$\  $$   | $$     | $$
|  $$$$$$/   | $$   | $$               | $$  |  $$$$$$/|  $$$$$$/| $$$$$$$$| $$ \  $$ /$$$$$$   | $$
 \______/    |__/   |__/               |__/   \______/  \______/ |________/|__/  \__/|______/   |__/


     CTF Toolkit - Command Reference:

   crack-hash:
    --hash       : The hash value to crack
    --wordlist   : Path to the wordlist file
    --algo       : Hash algorithm (md5, sha1, sha256)

   port-scan:
    --host       : Target IP or domain
    --start      : Start port (default: 1)
    --end        : End port (default: 1024)

   Example Usage:
    python index.py crack-hash --hash <hash> --wordlist wordlist.txt --algo md5
    python index.py port-scan --host 127.0.0.1 --start 1 --end 100
    python index.py show-help
""")
