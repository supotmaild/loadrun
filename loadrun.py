'''loadrun.py'''
'''11 Jul 2015'''
'''one and only version'''
global program_text
program_text=[]
def load(file_name):
	global program_text
	program_text=[]
	f=open(file_name,'r')
	program_text = f.readlines()
	f.close()
def run():
	global program_text
	j = ''
	for i in program_text:
		if type(i) is str:
			j = j + i
	if (j != ''):
		exec(j + '\n')
		j = ''

