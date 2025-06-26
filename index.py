import typer
from port_scan import port_scan
from crack_hash import crack_hash
from help_info import show_help


app = typer.Typer()


app.command()(port_scan)
app.command()(crack_hash)
app.command()(show_help)

if __name__ == "__main__":
    app()