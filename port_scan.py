import typer
import socket


def port_scan(
        host: str = typer.Option(..., "--host", help="Target IP or domain"),
        start: int = typer.Option(1, "--start", help="Start port"),
        end: int = typer.Option(1023, "--end", help="End port")
):

    typer.echo(f"[*] Scanning {host} from port {start} to {end}...")

    for port in range(start, end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((host, port))

            if result == 0 :
                typer.echo(f"[+] Port {port} is OPEN")
            else:
                typer.echo(f"[+] Port {port} is CLOSED ")   
