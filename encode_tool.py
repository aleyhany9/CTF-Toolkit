import typer
import base64
import urllib.parse
import binascii

def encode_tool(
        text: str = typer.Option(..., "--text", "-t", help="Text to encode or decode (wrap in quotes if it has spaces or symbols)"),
        type: str = typer.Option(..., "--type", "-u", help="Encoding typer: base64, hex, url"),
        decode: bool = typer.Option(False, "--decode", "-d", help="Decode insted of encode")
):
   try:
        if type == "base64":
            if decode:
                result = base64.b64decode(text).decode()
            else:
                result = base64.b64encode(text.encode()).decode()

        elif type == "hex":
            if decode:
                try:
                    result = binascii.unhexlify(text).decode()
                except binascii.Error:
                    typer.echo("[!] Invalid hex input.")
                    raise typer.Exit()
            else:
                result = text.encode().hex()

        elif type == "url":
            if decode:
                result = urllib.parse.unquote(text)
            else:
                result = urllib.parse.quote(text)           

        else:
            typer.echo("[!] Unsupported type. Use base64, hex, or url.")

        typer.echo(f"[+] Result: {result}")


   except Exception as e:
      typer.echo(f"[!] error: {e}")
