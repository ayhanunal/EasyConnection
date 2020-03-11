import os
from socket import *
import time

def SplitData(message):
    data = message.split(";")
    frequency = str(abs(time.time() - float(data[1])))[0:5] + " Hz"
    datarate = data[2]
    sender_message = data[0]
    return frequency, datarate, sender_message

def main():
    host = "192.168.1.1" # BU BİLGİSAYARIN IPV4 ADRESİ
    port = 10000
    buf = 1024

    address = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.bind(address)

    print ("Mesaj Bekleniyor...\n------------------------")

    while True:
        (message, address) = UDPSock.recvfrom(buf)
        frequency, datarate, sender_message = SplitData(message.decode())
        print("Mesaj: " + sender_message)
        print("Veri Oranı: " + datarate)
        print("Frekans: " + frequency)
        print("------------------------")

    UDPSock.close()
    os._exit(0)
main()

# ÖNEMLİ NOTLAR:
# SERVER.PY İÇİN HOST: BURADAKİ BİLGİSAYARA AİT IPV4 ADRESİ OLMALI
# SERVER.PY İÇİN PORT: BURADAKİ BİLGİSAYARDA BELİRLENMELİ
# CLIENT.PY İÇİN HOST: KARŞI TARAFDAKİ BİLGİSAYARA AİT IPV4 ADRESİ OLMALI
# CLIENT.PY İÇİN PORT: BU BİLGİSAYARDA BELİRLENEN PORT OLMALI
