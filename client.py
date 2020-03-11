import os
from socket import *
from time import sleep
import time

def GetDataRate(message, periode):
    bit = len(message) * 8
    bps = (1000 * bit) / periode
    str_bps = ""
    if bps < 1000:
        str_bps = str(bps) + " bps"
    if bps >= 1000 and bps < 999999:
        str_bps = str(bps/1000)[0:5] + " mbps"
    if bps >= 1000000 and bps < 999999999:
        str_bps = str(bps/1000000)[0:5] + " gbps"
    return str_bps

def main():
    print("------------ÖN AYARLAR------------")
    message = input("Mesajınızı Girin: ")
    periode = int(input("Periyot Girin (Milisaniye): "))
    
    print("------------GÖNDERME DURUMU------------")
    host = "192.168.1.2" # KARŞI TARAFIN IPV4 ADRESİ
    port = 5000
    addr = (host, port)

    UDPSock = socket(AF_INET, SOCK_DGRAM)

    while True:
        send_message = message + ";" + str(time.time()) + ";" + GetDataRate(message, periode)
        UDPSock.sendto(send_message.encode(), addr)
        print("Veri İletildi, Bilgiler Karşı Bilgisayarın Ekranındadır")
        sleep(periode / 1000)

    UDPSock.close()
    os._exit(0)
main()

# ÖNEMLİ NOTLAR:
# SERVER.PY İÇİN HOST: BURADAKİ BİLGİSAYARA AİT IPV4 ADRESİ OLMALI
# SERVER.PY İÇİN PORT: BURADAKİ BİLGİSAYARDA BELİRLENMELİ
# CLIENT.PY İÇİN HOST: KARŞI TARAFDAKİ BİLGİSAYARA AİT IPV4 ADRESİ OLMALI
# CLIENT.PY İÇİN PORT: BU BİLGİSAYARDA BELİRLENEN PORT OLMALI
