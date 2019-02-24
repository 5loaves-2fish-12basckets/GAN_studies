import subprocess
import os

def check_directories(dir_list):
    for path in dir_list:
        if not os.path.exists(path):
            os.makedirs(path)

def check_gpu():
	name = 'nvidia-smi'
	query = '--query-gpu=memory.free,memory.total,memory.used'
	form = '--format=csv'
	sp = subprocess.Popen([name, query, form], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out_str = sp.communicate()
	out_list = out_str[0].decode("utf-8").split('\n')[-2].split(',')
	out_list = [int(i[:-4]) for i in out_list]
	return out_list

class gpu_gauge():
	def __init__(self):
		self.free = 0
		self.total = 0
		self.used = 0
		self.refresh()

	def refresh(self):
		status = check_gpu()
		self.free = status[0]
		self.total = status[1]
		self.used = status[2]

	def available(self):
		self.refresh()
		return self.free


def linux_width():
	try:
	    rows, columns = os.popen('stty size', 'r').read().split()
	    return int(columns)
	except:
	    pass
	return 0

class progress_bar():
	def __init__(self):
		width = linux_width()
		if not width: width = 80
		self.width = width - 4
	
	def show_progress(self, percent):
		self.refresh_width()
		bar_area = int(self.width*percent)
		empt_area = self.width - bar_area
		percent_text = str(int(percent*100))+'%'
		print('█'*bar_area+' '*empt_area+percent_text, end = '\r')
	
	def refresh_width(self):
		width = linux_width()
		if not width: width = 80
		self.width = width - 4

