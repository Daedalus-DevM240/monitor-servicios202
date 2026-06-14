**import socket**

**import argparse**



**def verificar\_servicio(host, puerto):**

&#x20;   **try:**

&#x20;       **# Esto intenta crear la conexión TCP (El "Handshake")**

&#x20;       **with socket.socket(socket.AF\_INET, socket.SOCK\_STREAM) as s:**

&#x20;           **s.settimeout(1)**

&#x20;           **return s.connect\_ex((host, int(puerto))) == 0**

&#x20;   **except:**

&#x20;       **return False**



**# ... resto de tu lógica en main() ...**

