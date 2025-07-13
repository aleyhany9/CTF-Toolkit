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
   --hash      <HASH>         (required) The hash to crack 
   --wordlist  <FILE>         (required) Path to the wordlist file
   --algo      md5 | sha1 | sha256       hash algorithm to use (default: sha256)

2. port-scan         Scan open ports on a target
   --host      <IP or domain> (required) Target IP address or domain name
   --start     <start port>              Start port (default: 1)  
   --end       <end port>                End port (default: 1024)

3. encode-tool       Encode or decode text
   --text      <TEXT>         (required) Text to encode or decode
   --type      base64 | hex | url        Encoding type (required)
   --decode                   (optional) Decode instead of encode 
               
4. dir-brute         Bruteforce directories on a web target
   --url       <URL>           (required) Base URl (e.g., http://example.com)
   --wordlist  <FILE>          (required) Path to the wordlist file                              
   --status    <CODE>          (optional) HTTP status code to match (default: 200) 
               
5. subdomain-enum    Enumerate subdomains for a domain
   --domain    <DOMAIN>        (required) Base domain (e.g., example.com)     
   --wordlist  <File>          (required) Path to subdomain wordlist 
   --status    <CODE>          (optional) Filter by status code (e.g., 200)       

6. dns-lookup        lookup DNS records (A, MX, TXT, etc.)
   --domain    <DOMAIN>        (required) Target domain (e.g., github.com)
   --type      A | MX | TXT    (optional) Record type (default: A)
   --all                       (optional) Get all comman record types
   --save      <FILE>          (optional) save output to a file       

9. ssh-brute         Brute force SSH login using a password list
   --host      <IP/Domain>     (required) Target SSH server
   --user      <USERNAME>      (required) Username to brute force
   --wordlist  <FILE>          (required) Password wordlist
   --port      <PORT>          (default: 22)
   --stop                      Stop on first success (default: 22)
               
8. help              Show this help message

Examples:
──────────
python index.py crack-hash --hash 5d41402abc... --wordlist rockyou.txt --algo md5
python index.py port-scan --host example.com --start 20 --end 80
python index.py encode-tool --text "hello" --type base64
python index.py encode-tool --text "aGVsbG8=" --type base64 --decode
python index.py dir-brute --url http://example.com --wordlist comman.txt 
python index.py subdomain-enum --domain github.com --wordlist subdomain.txt --status 200 
python index.py dns-lookup --domain github.com --type A
python index.py dns-lookup --domain github.com --all --save output.txt              
               
""")
