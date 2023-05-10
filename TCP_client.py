{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import socket\n",
    "\n",
    "# prompts user to input target and port\n",
    "target_host = input(\"Enter target host: \")\n",
    "target_port = int(input(\"Enter target port: \"))\n",
    "\n",
    "# create a socket object\n",
    "client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n",
    "\n",
    "# connect the client\n",
    "client.connect((target_host, target_port))\n",
    "\n",
    "# send some data\n",
    "client.send(b\"GET / HTTP/1.1\\r\\nHost: google.com\\r\\n\\r\\n\")\n",
    "\n",
    "# receive data\n",
    "response = client.recv(4096)\n",
    "\n",
    "print(response.decode())\n"
   ]
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
