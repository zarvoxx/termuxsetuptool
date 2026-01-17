import os
import sys
import time

# --- SİSTEM AYARLARI ---
OS_TYPE = os.name
CLEAR_CMD = 'cls' if OS_TYPE == 'nt' else 'clear'

def clear():
    os.system(CLEAR_CMD)

# --- RENKLER ---
R = '\033[31m'  # Kırmızı
G = '\033[32m'  # Yeşil
Y = '\033[33m'  # Sarı
C = '\033[36m'  # Turkuaz
W = '\033[37m'  # Beyaz
BOLD = '\033[1m'
RESET = '\033[0m'

def slow_type(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

# --- GİRİŞ PANELİ ---
def login_panel():
    clear()

    logo = f"""{C}{BOLD}
    ███████╗ █████╗ ██████╗ ██╗   ██╗ ██████╗ ██╗  ██╗
    ╚══███╔╝██╔══██╗██╔══██╗██║   ██║██╔═══██╗╚██╗██╔╝
      ███╔╝ ███████║██████╔╝██║   ██║██║   ██║ ╚███╔╝ 
     ███╔╝  ██╔══██║██╔══██╗╚██╗ ██╔╝██║   ██║ ██╔██╗ 
    ███████╗██║  ██║██║  ██║ ╚████╔╝ ╚██████╔╝██╔╝ ██╗
    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝   ╚═════╝ ╚═╝  ╚═╝{RESET}"""
    print(logo)
    
    print(f"\n{C}{'═'*70}{RESET}")
    slow_type(f"{W}  [+] SYSTEM READY. WAITING FOR OPERATOR...{RESET}\n")
    print(f"{C}{'═'*70}{RESET}\n")

    name = input(f"{C}{BOLD}  NICKNAME: {Y}").strip()
    if not name: name = "Zarvox_Guest"
    
    print(f"\n{W}  Authenticating {G}{name}{W}...")
    time.sleep(1)
    return name

# --- ANA MENÜ (Kapanmayı Engelleyen Döngü) ---
def main_loop(nick):
    while True: # Programın kapanmasını engelleyen ana döngü
        clear()
        print(f"""{C}{BOLD}
    ╔══════════════════════════════════════════════════════════════╗
    ║           {W}T E R M U X  S E T U P  T O O L{C}              ║
    ╠══════════════════════════════════════════════════════════════╣
    ║  {W}OPERATOR: {nick.ljust(15)} {C}║  {W}STATUS: AUTHORIZED{C}║
    ╚══════════════════════════════════════════════════════════════╝{RESET}""")
        
        print(f"\n  {G}[1]{W} START ALL-IN-ONE INSTALLATION")
        print(f"  {G}[2]{W} SYSTEM DISCONNECT")
        
        choice = input(f"\n{C}{BOLD}{nick}@zarvox_system:~# {RESET}").strip()

        if choice == "1":
            # Kurulum Fonksiyonu
            clear()
            print(f"{Y}[!] Starting Full Setup...{RESET}\n")
            # Örnek paket listesi
            libs = ["python", "git", "php", "wget", "curl", "nano"]
            for lib in libs:
                print(f"{W}Installing {lib}...{RESET}")
                if OS_TYPE == 'posix':
                    os.system(f"pkg install {lib} -y")
                else:
                    time.sleep(0.3) # Windows simülasyonu
            print(f"\n{G}[+] Setup finished!{RESET}")
            input(f"\n{W}Press Enter to return to menu...{RESET}")
        
        elif choice == "2":
            print(f"\n{R}Shutting down...{RESET}")
            time.sleep(1)
            break # Sadece burada döngü biter ve program kapanır
        
        else:
            print(f"{R}Error: Command not found.{RESET}")
            time.sleep(1)

# --- BAŞLATICI ---
if __name__ == "__main__":
    try:
        user_name = login_panel()
        main_loop(user_name)
    except Exception as e:
        print(f"\n{R}Critical Error: {e}{RESET}")
        input("Press Enter to close...") # Hata olsa bile ekran kapanmaz
    except KeyboardInterrupt:
        print(f"\n{R}Session interrupted.{RESET}")
        sys.exit()