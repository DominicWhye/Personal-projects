import socket

mac = "A1-B1-C1-D1-E1-F1"      # (input ur MAC address here) 
ip = "192.168.1.00"          # (input ur IP address here)

packet = bytes.fromhex("FF"*6 + mac.replace("-","")*16)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.sendto(packet, (ip, 9))   #(setting port 9 as most devices listen to this port for WOL, if it doesnt work, can try port 7 or 0)