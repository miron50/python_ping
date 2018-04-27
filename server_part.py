import socket, select

if __name__ == "__main__":

    list_connections = []
    recv = 1024
    local_port = "2222"

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(("localhost", int(local_port)))
    server_sock.listen()
    list_connections.append(server_sock)

    print("Server is started and listen port " + str(local_port))

    while 1:
        read_sockets, write_sockets, error_sockets = select.select(list_connections, [], [])

        for sock in read_sockets:
            if sock == server_sock:
                sockfd, client_ip_port = server_sock.accept()
                list_connections.append(sockfd)
                print("Client (%s, %s) connected to server" % client_ip_port)
            else:
                try:
                    data = sock.recv(recv)
                    if data:
                        sock.send(data)
                    else:
                        raise ConnectionResetError()
                except:
                    print("Client (%s, %s) is disconnected" % client_ip_port)
                    sock.close()
                    list_connections.remove(sock)