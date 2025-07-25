from colorama import Fore, Style
import threading
from pyngrok import ngrok

def show_banner():
    print(Fore.CYAN + r"""
    ███████╗██╗██████╗ ███████╗██████╗ ██████╗ ███████╗
    ██╔════╝██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝
    █████╗  ██║██████╔╝█████╗  ██████╔╝██████╔╝███████╗
    ██╔══╝  ██║██╔══██╗██╔══╝  ██╔══██╗██╔═══╝ ╚════██║
    ██║     ██║██║  ██║███████╗██║  ██║██║     ███████║
    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝
    """ + Style.RESET_ALL)

def start_interface():
    show_banner()
    print(Fore.GREEN + "[+] Iniciando servidor..." + Style.RESET_ALL)
    tunnel = ngrok.connect(5000)
    print(Fore.YELLOW + f"[+] URL Ngrok: {tunnel.public_url}" + Style.RESET_ALL)
    input("\nPressione Enter para encerrar...")
    ngrok.kill()