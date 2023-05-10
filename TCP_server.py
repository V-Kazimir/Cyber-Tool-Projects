{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter bind IP: 127.0.0.1\n",
      "Enter bind port: 8888\n"
     ]
    },
    {
     "ename": "OSError",
     "evalue": "[WinError 10048] Only one usage of each socket address (protocol/network address/port) is normally permitted",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mOSError\u001b[0m                                   Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-e344296ecd7e>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[0mserver\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0msocket\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msocket\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msocket\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mAF_INET\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msocket\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mSOCK_STREAM\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 9\u001b[1;33m \u001b[0mserver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mbind\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbind_ip\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbind_port\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     10\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     11\u001b[0m \u001b[0mserver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlisten\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mOSError\u001b[0m: [WinError 10048] Only one usage of each socket address (protocol/network address/port) is normally permitted"
     ]
    }
   ],
   "source": [
    "import socket\n",
    "import threading\n",
    "\n",
    "bind_ip = input(\"Enter bind IP: \")\n",
    "bind_port = int(input(\"Enter bind port: \"))\n",
    "\n",
    "server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n",
    "\n",
    "server.bind((bind_ip, bind_port))\n",
    "\n",
    "server.listen(5)\n",
    "\n",
    "print(f\"[*] Listening on {bind_ip}:{bind_port}\")\n",
    "\n",
    "def handle_client(client_socket):\n",
    "    \n",
    "    # send something\n",
    "    client_socket.send(\"Connected\\r\\n\".encode())\n",
    "    \n",
    "    # print out what the client sends\n",
    "    request = client_socket.recv(1024).decode()\n",
    "    \n",
    "    print(f\"[*] Reveived: {request}\")\n",
    "    \n",
    "    # send back a packet\n",
    "    client_socket.send(\"ACK!\\r\\n\".encode())\n",
    "    \n",
    "    client_socket.close()\n",
    "    \n",
    "while True:\n",
    "    client, addr = server.accept()\n",
    "    \n",
    "    print(f\"[*] Accepted connection from: {addr[0]}:{addr[1]}\")\n",
    "    \n",
    "    # spin up our client thread to handle incoming data\n",
    "    client_handler = threading.Thread(target=handle_client,args=(client,))\n",
    "    client_handler.start()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
