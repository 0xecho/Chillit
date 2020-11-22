from urllib.parse import urlparse
from threading import Timer
from time import time

last_exec = {}
threads = []

def get_input_forever():
	try:
		while True:
			ipt = input()
			yield ipt
	except:
		pass

def get_domain(url):
	return urlparse(url).netloc

def printer(url):
	print(url)

interval = 3

try:
	for url in get_input_forever():
		domain = get_domain(url)
		if not domain in last_exec:
			last_exec[domain] = 0
		cur_time = time()
		last_time = last_exec[domain]
		if cur_time > last_time+interval:
			print(url)
			last_exec[domain] = time()
		else:
			t = Timer((last_time+interval)-cur_time, printer, (url,))
			t.start()
			last_exec[domain] = time() + (last_time+interval)-cur_time
			threads.append(t)
finally:
	for thread in threads:
		thread.join()