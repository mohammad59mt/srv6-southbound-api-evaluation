import os

_Device = 'enp5s0'
_Prefix1 =  '2000::'
_N = '100'
_Segments = '2000::1e'

def printInFile(text):
	f1 = open('LocalRuleEnforcement20.txt','a+')
	f1.write(text)
	f1.close()


for i in range(1,21):
	printInFile('Pytroute2 add:\n')
	os.system('sudo python MeasureServerExecutionMetrics.py -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -o add  -n ' + _N  + ' -a pyroute2')
	printInFile('Pytroute2 del:\n')
	os.system('sudo python MeasureServerExecutionMetrics.py -p ' + _Prefix1 + ' -d ' + _Device + ' -o delete -n ' + _N  + ' -a pyroute2')
	printInFile('Shell add:\n')
	os.system('sudo python MeasureServerExecutionMetrics.py -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -o  add -n ' + _N  + ' -a shell')
	printInFile('shell del:\n')
	os.system('sudo python MeasureServerExecutionMetrics.py -p ' + _Prefix1 + ' -d ' + _Device + ' -o delete -n ' + _N  + ' -a shell')
