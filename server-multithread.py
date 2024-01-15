import socket
import threading
import sys

class UDPServerThread(threading.Thread):
    def __init__(self, file1, file2):
        super(UDPServerThread, self).__init__()
        self.file1 = file1
        self.file2 = file2

    def run(self):
        c, p = 0, 0
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('0.0.0.0', 514))
        print('Start process:')
        count = 0

        while True:
            try:
                data, addr = sock.recvfrom(65535)
                count += 1
                print("in loop")
                if c < 3:
                    c = c + 1
                    self.file1.write(addr[0] + " " + (data).decode('utf-8'))
                    self.file1.write("\n")

                    print("1 write:", count)
                    if c == 3:
                        p = 0
                        self.file2.truncate()
                        self.file2.close()
                        self.file2 = open("window_logs2.csv", "r+")

                elif p < 3:
                    p = p + 1
                    self.file2.write(addr[0] + " " + (data).decode('utf-8'))
                    self.file2.write("\n")

                    print("1 write")
                    if p == 3:
                        c = 0
                        self.file1.truncate()
                        self.file1.close()
                        self.file1 = open("window_logs.csv", "r+")
            except:
                print("in except 2")
                self.file1.close()
                self.file2.close()
                sys.exit()

def main():
    f1 = open("window_logs.csv", "w")
    f2 = open("window_logs2.csv", "w")

    # Create a thread for the UDP server
    udp_server_thread = UDPServerThread(file1=f1, file2=f2)
    udp_server_thread.start()

if __name__ == '__main__':
    main()
