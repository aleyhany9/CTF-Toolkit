import typer
import dns.resolver
from pathlib import Path
from typing import Optional


RECORD_TYPES = ["A", "AAAA", "MX", "NS", "CNAME", "TXT", "SOA"]

def resolve_record(domain: str , record_type: str) -> list:
    output = []
    try:
        answer = dns.resolver.resolve(domain, record_type)
        for rdata in answer:
            line = f"[+] {record_type} record: {rdata.to_text()}"
            print(line)
            output.append(line)
    except dns.resolver.NoAnswer:
        line = f"[-] No {record_type} record found"
        print(line)
        output.append(line)
    except dns.resolver.NXDOMAIN:
        line = f"[-] Domain {domain} doesn't exist."
        print(line)
        output.append(line)
    except Exception as e:
        line = f"[!] Error with {record_type} record: {e}"
        print(line)
        output.append(line)
    return output  

def dns_lookup(
        domain: str = typer.Option(..., help="Target domain to look up"),
        type: str = typer.Option("A", help="DNS record type (A, MX, NS, etc.)"),
        all: bool = typer.Option(False, "--all", help="Look up all DNS record types"),
        save: Optional[Path] = typer.Option(None, help="Save output to a file")
):
    print(f"[*] Starting DNS lookup for {domain}")

    result_lines = []
    
    if all:
        for record_type in RECORD_TYPES:
            result_lines.extend(resolve_record(domain, record_type))
    else:
        result_lines.extend(resolve_record(domain, type.upper()))

    if save:
        try:
            with open(save, "w") as f:
                f.write("\n".join(result_lines))
            print(f"Result saved to: {save}")
        except Exception as e:
            print(f"Failed to save file: {e}")
