import time
import sys
import serial

serconn = serial.Serial("/dev/ttyUSB0", 115200)

def readline():
	line = bytearray()
	char = serconn.read(1)[0]
	while char != 10:
		line.append(char)
		sys.stdout.write( '%c' % char )
		char = serconn.read(1)[0]
	sys.stdout.write( '%c' % char )
	line.append(10)
	return bytes(line)

while True:
	line = readline()
	if line == b'Autobooting in 1 seconds\r\n':
		print("FOUND AUTOBOOTING LINE: STOPPING BOOT, STARTING TRANSFER")
		serconn.write(b'tpl')
		time.sleep(0.2)
		serconn.write(b'setenv ipaddr 192.168.9.101\n')
		time.sleep(0.2)
		serconn.write(b'setenv serverip 192.168.9.100\n')
		time.sleep(4)
		serconn.write(b'tftpboot 0x80000000 recovery.bin\n')
		while readline() != b'done\r\n':
			pass
		time.sleep(2)
		serconn.write(b'erase 0x9f020000 +0x3c0000\n')
		time.sleep(0.2)
		while readline() != b'Erased 60 sectors\r\n':
			pass
		time.sleep(2)
		serconn.write(b'cp.b 0x80000000 0x9f020000 0x3c0000\n')
		time.sleep(0.2)
		while readline() != b'done\r\n':
			pass
		time.sleep(2)
		serconn.write(b'bootm 9f020000\n')
		print("Done! You're now allowed to disconnect the router")
