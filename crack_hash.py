import typer
import hashlib


def crack_hash(
    hash_value: str = typer.Option(..., "--hash", help="Hash to crack"),
    wordlist: str = typer.Option(..., "--wordlist", help="Path to wordlist file"),
    algo: str = typer.Option("sha256", "--algo", help="Hash algorithm (md5, sha1, sha256)")
):

    try:
        with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
            words = f.readlines()
    except FileNotFoundError:
        typer.echo(f"[!] Wordlist not found: {wordlist}")
        raise typer.Exit()

    hash_func = getattr(hashlib, algo, None)
    if not hash_func:
        typer.echo(f"[!] Unsupported algorithm: {algo}")
        raise typer.Exit()

    typer.echo(f"[*] Cracking using {algo.upper()}...")

    for word in words:
        word = word.strip()
        if hash_func(word.encode()).hexdigest() == hash_value:
            typer.echo(f"[+] Hash cracked! Plaintext: {word}")
            return

    typer.echo("[-] Failed to crack the hash.")
