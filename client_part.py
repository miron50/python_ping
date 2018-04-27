import socket, struct, time
import sys

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    host = input("Enter host IP address: ")
    port = input("Enter port: ")
    sock.connect((host, int(port)))

    ping_count = input("Enter ping count: ")
    seq_num = 0
    while seq_num != int(ping_count):
        try:
            seq_num += 1
            pdata = struct.pack("!Hd", seq_num, time.time())
            sock.send(pdata)
            data = sock.recv(1024)
            current_time = time.time()
            (seq, timestamp) = struct.unpack("!Hd", data)
            dif_time = (current_time - timestamp)*1000
            print("seg_number = %u, diff = %.3f ms" % (seq, dif_time))
            time.sleep(1)
        except Exception:
            e = sys.exc_info()[1]
            print(e.args[0])