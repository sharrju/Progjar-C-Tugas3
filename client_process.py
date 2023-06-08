import sys
import socket
import logging
import time
from multiprocessing import Process

def kirim_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    server_address = ('172.18.0.3', 45000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        message = 'TIME\r\n'.encode()
        logging.warning(f"[CLIENT] sending {message}")
        sock.sendall(message)
        # Look for the response
        data = sock.recv(32)
        logging.warning(f"[DITERIMA DARI SERVER] {data}")
    finally:
        logging.warning("closing")
        sock.close()
    return

def send_process():
    p = Process(target=kirim_data)
    p.start()
    p.join()

if __name__=='__main__':
    process_counter = 0
    start_time = time.time()
    while time.time() - start_time < 60:
        send_process()
        process_counter += 1
    logging.warning(f"Total proses yang dibuat: {process_counter}")