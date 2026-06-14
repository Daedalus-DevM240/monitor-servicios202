import socket
import argparse

# 1. Define la función aquí arriba
def verificar_servicio(host, puerto):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            return s.connect_ex((host, int(puerto))) == 0
    except:
        return False

# 2. La función main que ya tienes debería llamar a la función anterior
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True)
    parser.add_argument("--puertos", nargs='+', type=int, required=True)
    args = parser.parse_args()

    print(f"[*] Iniciando auditoría en {args.host}...")
    for puerto in args.puertos:
        if verificar_servicio(args.host, puerto):
            print(f"[+] Servicio en puerto {puerto}: ONLINE")
        else:
            print(f"[-] Servicio en puerto {puerto}: OFFLINE/BLOQUEADO")

if __name__ == "__main__":
    main()