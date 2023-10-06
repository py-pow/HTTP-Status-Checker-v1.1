import requests
import argparse
from rich import print
from rich_argparse import *



banner = """ 
██╗  ██╗████████╗████████╗██████╗     ███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██║  ██║╚══██╔══╝╚══██╔══╝██╔══██╗    ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
███████║   ██║      ██║   ██████╔╝    ███████╗   ██║   ███████║   ██║   ██║   ██║███████╗    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██╔══██║   ██║      ██║   ██╔═══╝     ╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║   ██║      ██║   ██║         ███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝         ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""


def parse_args():
    print(f"[bold orange3]{banner} [/]")
    
    parser = argparse.ArgumentParser(formatter_class=RichHelpFormatter,prog="main.py",add_help=True)
    parser._optionals.title = f"[py_pow] >• Coded by py_pow https://github.com/py-pow\n"
    parser.add_argument('--list','-l', metavar="List",required=True, help="Used to specify a list of URLs.")
    parser.add_argument('--status','-s', metavar="Status", help="Specifies the Status Code and saves the specified status code as output only. Ex: 200")
    parser.add_argument('--output','-o', default='output.txt', metavar="Output", help="output is used to display default:output.txt")
    args = parser.parse_args()
    return args, parser
args, parser = parse_args()
def main():

    

    sites_file = args.list
    output_file = args.output 
    print(f"[bold grey46]\[i]> Selected File: {sites_file} [/]")
    print(f"[bold grey46]\[i]> Output File: {output_file} [/]")
    if not args.status:
        print(f"[bold grey46]\[i]> Status: All [/]")
    else:
        print(f"[bold grey46]\[i]> Select Status Code(s): {args.status} [/]")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0',
        'ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    with open(sites_file, "r") as file:
        sites = file.readlines()
        if len(sites) == 0:
            print(f"[bold red]\[i]> websites were not found in the file![/]")
        else:
            print(f"[bold grey46]\[i]> {len(sites)} websites were found in the file![/]")
        

    status_codes_to_check = args.status.split(",") if args.status else []

    status_codes_to_check = [int(code) for code in status_codes_to_check]

    with open(output_file, "w") as output:
        for site in sites:
            site = site.strip()  
            try:
                if not site.startswith(("http://", "https://")):
                    response = requests.get(f"http://" + site, headers=headers)

                if not status_codes_to_check or response.status_code in status_codes_to_check:
                    print(f"[bold blue]Site: {site} Status Code: {response.status_code} [/]")
                    output.write(f"Site: {site} Status Code: {response.status_code}\n")
                    
            except requests.exceptions.Timeout as error:
                print(f"[bold red]Site: {site}  | Error : Timeout[/]")

            except (requests.exceptions.MissingSchema, requests.exceptions.InvalidURL) as error:
                print(f"[bold red]Site: {site}  | Error : Invalid URL[/]")

            except requests.exceptions.ConnectionError as error:
                if "[Errno 11001] getaddrinfo failed" or '[Errno -2] Name or service not known' in str(error):
                    print(f"[bold red]Site: {site}  | Error : Getaddrinfo Failed | Name or service not known[/]")

                elif "Connection aborted." in str(error):
                    print(f"[bold red]Site: {site}  | Error : Connection aborted[/]")
                elif "SSLCertVerificationError" in str(error):
                    print(f"[bold red]Site: {site}  | Error : SSL Error[/]")
                else:
                    print(f"{site} için bilinmeyen bir hata oluştu: {error}")
            except requests.exceptions.RequestException as error:
                print(f"{site} için genel bir istek hatası oluştu: {error}")
            except Exception as error:
                print(f"{site} için bilinmeyen bir hata oluştu: {error}")


if __name__ == "__main__":
    
    try:
        main()
    except FileNotFoundError:
        print(f"[bold red]File Not Found.[/]")
    except KeyboardInterrupt:
        print("CTRL+C :)")
        exit()
