import typer
from port_scan import port_scan
from crack_hash import crack_hash
from help_info import show_help
from encode_tool import encode_tool
from dir_brute import dir_brute
from subdomain_enum import subdomain_enum


app = typer.Typer()


app.command("port-scan")(port_scan)
app.command("crack-hash")(crack_hash)
app.command("help")(show_help)
app.command("encode-tool")(encode_tool)
app.command("dir-brute")(dir_brute)
app.command("subdomain-enum")(subdomain_enum)

if __name__ == "__main__":
    app()