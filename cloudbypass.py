import argparse
import requests
import socket
import dns.resolver
import whois
import time
import nmap
import shutil
import sys
import threading
import os
from termcolor import colored

def print_banner():
    """Printing tool banner."""
    banner = """
\033[31m

       (       )        (             ) (            (   (     
   (   )\ ) ( /(        )\ )   (   ( /( )\ )   (     )\ ))\ )  
   )\ (()/( )\())    ( (()/( ( )\  )\()|()/(   )\   (()/(()/(  
 (((_) /(_)|(_)\     )\ /(_)))((_)((_)\ /(_)|(((_)(  /(_))(_)) 
 )\___(_))   ((_) _ ((_|_))_((_)___ ((_|_))  )\ _ )\(_))(_))   
((/ __| |   / _ \| | | ||   \| _ ) \ / / _ \ (_)_\(_) __/ __|  
 | (__| |__| (_) | |_| || |) | _ \\ V /|  _/  / _ \ \__ \__ \  
  \___|____|\___/ \___/ |___/|___/ |_| |_|   /_/ \_\|___/___/  
                                                               
  
					v 1.1
\033[31m
╭────────────────────────────────────────────────────╮
│              Osint IP Scanner                      │
│                                                    │
│                                                    │
│     GitHub    : https://github.com/cazzysoci       │
│                                                    │
│                                                    │
╰────────────────────────────────────────────────────╯
\033[0m
    """
    print(colored(banner, "red"))

def print_intro():
   
    intro_text = """
\033[31m
╔═══════════════════════════════════════════════════╗
║             WELCOME TO CLOUDBYPASS TOOL           ║
║  This tool is designed for OSINT investigations,  ║
║  providing various techniques for IP analysis,    ║
║  reconnaissance, and target information gathering ║
║  						    ║
║           Press Enter to continue...              ║
╚═══════════════════════════════════════════════════╝
\033[0m
"""
    print(colored(intro_text, "red"))
    input()

def clear_screen():
    """Clear Terminal Screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def animated_loading(message, stop_event, delay=0.1):
    
    animation = "|/-\\"
    idx = 0
    while not stop_event.is_set():  
        print(colored(f"\r{message} {animation[idx % len(animation)]}", "red"), end="", flush=True)
        idx += 1
        time.sleep(delay)
    print(colored("\r", "red"), end="", flush=True)  

def loading_message():
   
    loading_text = "[+] Checking dependencies and connections..."
    stop_event = threading.Event()  
    loading_thread = threading.Thread(target=animated_loading, args=(loading_text, stop_event))
    loading_thread.start()
    time.sleep(3)  
    stop_event.set()  
    loading_thread.join()  
    print(colored("\r[OK] All dependencies are available!                                   \n", "red"), end="", flush=True)
    time.sleep(1)

def dns_enumeration(domain):
    
    stop_event = threading.Event()
    loading_thread = threading.Thread(target=animated_loading, args=("[+] Doing DNS Enumeration...", stop_event))
    loading_thread.start()
    try:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ["8.8.8.8", "1.1.1.1"]
        answers = resolver.resolve(domain, 'A')
        stop_event.set()  
        loading_thread.join()
        print(colored("\r[OK] DNS Enumeration finished!                                     \n", "red"), end="", flush=True)
        print(colored("[+] Looking for IP leaks from DNS...", "red"))
        for rdata in answers:
            print(colored(f"[FOUND] DNS Enumeration: {rdata}", "red"))
    except Exception as e:
        stop_event = threading.Event()
        loading_thread = threading.Thread(target=animated_loading, args=("[+] Doing DNS Enumeration...", stop_event))
        loading_thread.start()
        print(colored("\r[!] DNS Enumeration fail!                                          \n", "red"), end="", flush=True)
        print(colored(f"[!] DNS Enumeration fail: {e}", "red"))

def historical_ip_lookup(domain):
    
    print(colored("[+] Mencari riwayat IP...", "red"))
    try:
        api_key = "F6Xpv0hYeBE0tMqylzkjq79vbuGJh55J"  
        url = f"https://api.securitytrails.com/v1/domain/{domain}/history?apikey={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "records" in data:
                for record in data["records"]:
                    print(colored(f"[FOUND] Historical IP: {record['ip']}", "red"))
            else:
                print(colored("[!] No IP history data found", "red"))
        else:
            print(colored(f"[!] Error: {response.text}", "red"))
    except Exception as e:
        print(colored(f"[!] Historical IP Lookup fail: {e}", "red"))

def direct_ip_leak(domain):
  
    stop_event = threading.Event()
    loading_thread = threading.Thread(target=animated_loading, args=("[+] Trying Direct IP Leak...", stop_event))
    loading_thread.start()
    try:
        ip = socket.gethostbyname(domain)
        stop_event.set()
        loading_thread.join()
        print(colored("\r[OK] Direct IP Leak finished!                                      \n", "red"), end="", flush=True)
        print(colored("[+] Trying to find the original IP...", "yellow"))
        print(colored(f"[FOUND] Direct IP: {ip}", "red"))
    except Exception as e:
        stop_event.set()
        loading_thread.join()
        print(colored("\r[!] Direct IP Leak fail!                                        \n", "red"), end="", flush=True)
        print(colored(f"[!] Failed to find the original IP: {e}", "red"))

def whois_lookup(domain):
  
    stop_event = threading.Event()
    loading_thread = threading.Thread(target=animated_loading, args=("[+] Doing WHOIS Lookup...", stop_event))
    loading_thread.start()
    try:
        info = whois.whois(domain)
        stop_event.set()
        loading_thread.join()
        print(colored("\r[OK] WHOIS Lookup finished!                                        \n", "red"), end="", flush=True)
        print(colored("[+] Do WHOIS Lookup...", "yellow"))
        print(colored(f"WHOIS Data:\n{info}", "red"))
    except Exception as e:
        stop_event.set()
        loading_thread.join()
        print(colored("\r[!] WHOIS Lookup fail!                                          \n", "red"), end="", flush=True)
        print(colored(f"[!] WHOIS Lookup fail: {e}", "red"))

def port_scanning(domain):
 
    stop_event = threading.Event()
    loading_thread = threading.Thread(target=animated_loading, args=("[+] Scanning for open ports...", stop_event))
    loading_thread.start()
    try:
        scanner = nmap.PortScanner()
        scanner.scan(domain, '21,22,80,443,3389', arguments='-T4')
        stop_event.set()
        loading_thread.join()
        print(colored("\r[OK] Port Scanning finished!                                       \n", "green"), end="", flush=True)
        print(colored("[+] Scanning for open ports...", "yellow"))
        for host in scanner.all_hosts():
            print(colored(f"[FOUND] Host: {host}", "red"))
            for proto in scanner[host].all_protocols():
                ports = scanner[host][proto].keys()
                for port in ports:
                    print(colored(f" - Port {port}: {scanner[host][proto][port]['state']}", "red"))
            break  
    except Exception as e:
        stop_event.set()
        loading_thread.join()
        print(colored("\r[!] Port Scanning fail!                                         \n", "red"), end="", flush=True)
        print(colored(f"[!] Port Scanning fail: {e}", "red"))

def menu():
   
    global domain

    menu_color = "\033[31m" 
    reset_color = "\033[0m"   

    while True:
        print_banner()

        print(colored(menu_color + "╔════════════════════════════════════╗", "red"))
        print(colored(menu_color + "║ [1] Enter Target Domain            ║", "red"))
        print(colored(menu_color + "║ [2] DNS Enumeration                ║", "red"))
        print(colored(menu_color + "║ [3] Historical IP Lookup           ║", "red"))
        print(colored(menu_color + "║ [4] Direct IP Leak                 ║", "red"))
        print(colored(menu_color + "║ [5] WHOIS Lookup                   ║", "red"))
        print(colored(menu_color + "║ [6] Port Scanning                  ║", "red"))
        print(colored(menu_color + "║ [7] Exit                           ║", "red"))
        print(colored(menu_color + "╚════════════════════════════════════╝" + reset_color, "red"))

        choice = input(colored("Enter Choice (1-7): ", "red"))
        if choice == "7":
            print(colored("Thank you for your Service", "red"))
            break
        elif choice == "1":
            domain = input(colored("Enter Domain Target: ", "red"))
        elif choice in feature_mapping and domain:
            feature_mapping[choice](domain)
            input(colored("\nPress Enter to return to the main menu...", "red"))
        elif choice in feature_mapping and not domain:
            print(colored("[!] Please enter the Domain first!", "red"))
        else:
            print(colored("[!] Choice not valid!", "red"))

def main():
  
    parser = argparse.ArgumentParser(description="Bypass Cloudflare & Find Real IP")
    parser.add_argument("-d", "--domain", help="Domain target")
    args = parser.parse_args()
    
    global domain
    domain = args.domain if args.domain else ""
    print_banner()  
    print_intro()   
    clear_screen()  
    loading_message()  
    menu()  

feature_mapping = {
    "2": dns_enumeration,
    "3": historical_ip_lookup,
    "4": direct_ip_leak,
    "5": whois_lookup,
    "6": port_scanning
}

if __name__ == "__main__":
    import os
    main()
