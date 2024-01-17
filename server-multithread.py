import socket
import sys
from concurrent.futures import ThreadPoolExecutor
import logging

class LogReceiver:
    def __init__(self):
        self.f1 = open("window_logs.csv", "w")
        self.f2 = open("window_logs2.csv", "w")
        self.c = 0
        self.p = 0

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('0.0.0.0', 514))

    def receive_logs(self):
        with ThreadPoolExecutor() as executor:
            try:
                while True:
                    data, addr = self.sock.recvfrom(65535)
                    executor.submit(self.process_logs, data, addr)
            except Exception as e:
                logging.error(f"Exception: {e}")
                self.f1.close()
                self.f2.close()
                sys.exit()

    def process_logs(self, data, addr):
        count = 0
        count += 1

        if self.c < 3:
            self.c = self.c + 1
            self.f1.write(addr[0] + " " + (data).decode('utf-8'))
            self.f1.write("\n")
            logging.info(f"Write 1: {count}")

            if self.c == 3:
                self.p = 0
                self.f2.truncate()
                self.f2.close()
                self.f2 = open("window_logs2.csv", "r+")

        elif self.p < 3:
            self.p = self.p + 1
            self.f2.write(addr[0] + " " + (data).decode('utf-8'))
            self.f2.write("\n")
            logging.info("Write 1")

            if self.p == 3:
                self.c = 0
                self.f1.truncate()
                self.f1.close()
                self.f1 = open("window_logs.csv", "r+")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    log_receiver = LogReceiver()
    log_receiver.receive_logs()
