import socket 
f1=open("window_logs.csv","w")
f2=open("window_logs2.csv","w")

c=0
p=0

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.bind(('0.0.0.0',514))
print('start process:')
count=0
while True:
    try:
        data,addr=sock.recvfrom(65535)
        count+=1
        print("in loop")
        if c<3:
            c=c+1 
            f1.write(addr[0]+" "+(data).decode('utf-8'))
            f1.write("\n")
            
            print("1 write:",count)
            if c==3:
                p=0
                f2.truncate()
                f2.close()
                f2=open("window_logs2.csv","r+")

        elif p<3:
            p=p+1
            f2.write(addr[0]+" "+(data).decode('utf-8'))
            f2.write("\n")
            
            print("1 write")
            if p==3:
                c=0
                f1.truncate()
                f1.close()
                f1=open("window_logs.csv","r+")
    except:
        print("in except 2")
        f1.close()
        f2.close()
        sys.exit()










'''
while True:
    data,addr=sock.recvfrom(65535)
    print((data).decode("utf-8"))
    #sock.sendto(message,addr)
'''