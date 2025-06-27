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


Available Tools:
─────────────────────────────────────────────────────────────
1. crack-hash        Crack hashes using a wordlist
   --hash      <HASH>         (required)
   --wordlist  <FILE>         (required)
   --algo      md5 | sha1 | sha256 (default: sha256)

2. port-scan         Scan open ports on a target
   --host      <IP or domain> (required)
   --start     <start port>   (default: 1)
   --end       <end port>     (default: 1024)

3. encode-tool       Encode or decode text
   --text      <TEXT>         (required)
   --type      base64 | hex | url (required)
   --decode                    (optional, for decoding)

4. help              Show this help message

Examples:
──────────
python index.py crack-hash --hash 5d41402abc... --wordlist rockyou.txt --algo md5
python index.py port-scan --host example.com --start 20 --end 80
python index.py encode-tool --text "hello" --type base64
python index.py encode-tool --text "aGVsbG8=" --type base64 --decode
               
""")
