import socket
import argparse

def verificar_servicio(host, puerto):
    """Intenta conectar a un puerto específico."""
    try:
        # Creamos un socket de tipo TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2) # Tiempo de espera de 2 segundos
            resultado = s.connect_ex((host, puerto))
            if resultado == 0:
                return True # Puerto abierto
            else:
                return False # Puerto cerrado o filtrado
    except Exception as e:
        return False

def main():
    # Configuramos los argumentos para que el script sea profesional
    parser = argparse.ArgumentParser(description="Monitor de servicios para tus apps")
    parser.add_argument("--host", default="127.0.0.1", help="Dirección IP a escanear")
    parser.add_argument("--puertos", type=int, nargs='+', help="Lista de puertos (ej: 3000 5432 80)")
    
    args = parser.parse_args()

    print(f"[*] Iniciando auditoría en {args.host}...")
    for puerto in args.puertos:
        if verificar_servicio(args.host, puerto):
            print(f"[+] Servicio en puerto {puerto}: ONLINE")
        else:
            print(f"[-] Servicio en puerto {puerto}: OFFLINE/BLOQUEADO")

if __name__ == "__main__":
    main()