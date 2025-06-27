import typer
from port_scan import port_scan
from crack_hash import crack_hash
from help_info import show_help
from encode_tool import encode_tool


app = typer.Typer()


app.command()(port_scan)
app.command()(crack_hash)
app.command("help")(show_help)
app.command("encode-tool")(encode_tool)

if __name__ == "__main__":
    app()