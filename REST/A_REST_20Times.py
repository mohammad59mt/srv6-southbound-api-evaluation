import os

_Device = 'enp5s0'
_With_PacketLoss_And_Delay = True
_With_Out_PacketLoss_And_Delay = True
_Packet_Loss = '2%'
_Delay = '150ms'



_Server_Address = '2002::1'
_Prefix1 =  '2000::'
_N = '100'
_Segments = '2000::1e'
_File_Name = '' 

def printInFile(text):
	f1 = open(_File_Name+'.txt','a+')
	f1.write(text)
	f1.close()

#Full Process
_File_Name = 'RESTResults20_FullProcess'  
if _With_Out_PacketLoss_And_Delay:
	#no packet loss
	for i in range(1,21):
		print('Secure communications round '+str(i))
		_Secure = 'yes'
		printInFile('1 Sequential ADD secured:\n')
		os.system('sudo python MeasureClientREST.py -o add -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + '  -u ' + _Secure + ' -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('1 Sequential Del secured:\n')
		os.system('sudo python MeasureClientREST.py -o del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('2 Batch ADD secured:\n')
		os.system('sudo python MeasureClientREST.py -o add -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + '  -u ' + _Secure + ' -n ' + _N  + ' -m b -f ' + _File_Name)
		printInFile('2 Batch Del secured:\n')
		os.system('sudo python MeasureClientREST.py -o del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -n ' + _N  + ' -m b -f ' + _File_Name)

		print('Insecure communications round '+str(i))
		_Secure = 'no'
		printInFile('1 Sequential ADD Insecured:\n')
		os.system('sudo python MeasureClientREST.py -o add -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + '  -u ' + _Secure + ' -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('1 Sequential Del Insecured:\n')
		os.system('sudo python MeasureClientREST.py -o del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('2 Batch ADD Insecured:\n')
		os.system('sudo python MeasureClientREST.py -o add -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + '  -u ' + _Secure + ' -n ' + _N  + ' -m b -f ' + _File_Name)
		printInFile('2 Batch Del Insecured:\n')
		os.system('sudo python MeasureClientREST.py -o del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -n ' + _N  + ' -m b -f ' + _File_Name)

if _With_PacketLoss_And_Delay:
	#add 10 percent packet loss
	os.system('sudo tc qdisc add dev enp0s25 root netem loss '+_Packet_Loss)
	os.system('sudo tc qdisc add dev enp0s25 root netem delay '+_Delay)
	for i in range(1,21):
		print('Secure communications with packet loss round '+str(i))
		_Secure = 'yes'
		printInFile('1 Sequential ADD secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientREST.py -o add -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + '  -u ' + _Secure + ' -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('1 Sequential Del secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientREST.py -o del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('2 Batch ADD secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientREST.py -o add -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + '  -u ' + _Secure + ' -n ' + _N  + ' -m b -f ' + _File_Name)
		printInFile('2 Batch Del secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientREST.py -o del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -n ' + _N  + ' -m b -f ' + _File_Name)

		print('Insecure communications with packet loss round '+str(i))
		_Secure = 'no'
		printInFile('1 Sequential ADD Insecured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientREST.py -o add -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + '  -u ' + _Secure + ' -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('1 Sequential Del Insecured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientREST.py -o del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('2 Batch ADD Insecured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientREST.py -o add -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + '  -u ' + _Secure + ' -n ' + _N  + ' -m b -f ' + _File_Name)
		printInFile('2 Batch Del Insecured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientREST.py -o del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -n ' + _N  + ' -m b -f ' + _File_Name)

	os.system('sudo tc qdisc del dev enp0s25 root netem loss '+_Packet_Loss)
	os.system('sudo tc qdisc del dev enp0s25 root netem delay '+_Delay)

#Just Communication
_File_Name = 'RESTResults20_JustCommunicationPart'  
if _With_Out_PacketLoss_And_Delay:
	#no packet loss
	for i in range(1,21):
		print('Just Communication: Secure communications round '+str(i))
		_Secure = 'yes'
		printInFile('1 Sequential ADD secured:\n')
		os.system('sudo python MeasureClientREST.py -o nul -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + '  -u ' + _Secure + ' -n ' + _N  + ' -m s -f ' + _File_Name)
		#printInFile('1 Sequential Del secured:\n')
		#os.system('sudo python MeasureClientREST.py -o del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('2 Batch ADD secured:\n')
		os.system('sudo python MeasureClientREST.py -o nul -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + '  -u ' + _Secure + ' -n ' + _N  + ' -m b -f ' + _File_Name)
		#printInFile('2 Batch Del secured:\n')
		#os.system('sudo python MeasureClientREST.py -o del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -n ' + _N  + ' -m b -f ' + _File_Name)

		print('Just Communication: Insecure communications round '+str(i))
		_Secure = 'no'
		printInFile('1 Sequential ADD Insecured:\n')
		os.system('sudo python MeasureClientREST.py -o nul -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + '  -u ' + _Secure + ' -n ' + _N  + ' -m s -f ' + _File_Name)
		#printInFile('1 Sequential Del Insecured:\n')
		#os.system('sudo python MeasureClientREST.py -o del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('2 Batch ADD Insecured:\n')
		os.system('sudo python MeasureClientREST.py -o nul -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + '  -u ' + _Secure + ' -n ' + _N  + ' -m b -f ' + _File_Name)
		#printInFile('2 Batch Del Insecured:\n')
		#os.system('sudo python MeasureClientREST.py -o del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -n ' + _N  + ' -m b -f ' + _File_Name)

if _With_PacketLoss_And_Delay:
	#add 10 percent packet loss
	os.system('sudo tc qdisc add dev enp0s25 root netem loss '+_Packet_Loss)
	os.system('sudo tc qdisc add dev enp0s25 root netem delay '+_Delay)
	for i in range(1,21):
		print('Just Communication: Secure communications with packet loss round '+str(i))
		_Secure = 'yes'
		printInFile('1 Sequential ADD secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientREST.py -o nul -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + '  -u ' + _Secure + ' -n ' + _N  + ' -m s -f ' + _File_Name)
		#printInFile('1 Sequential Del secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		#os.system('sudo python MeasureClientREST.py -o del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('2 Batch ADD secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientREST.py -o nul -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + '  -u ' + _Secure + ' -n ' + _N  + ' -m b -f ' + _File_Name)
		#printInFile('2 Batch Del secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		#os.system('sudo python MeasureClientREST.py -o del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -n ' + _N  + ' -m b -f ' + _File_Name)

		print('Just Communication: Insecure communications with packet loss round '+str(i))
		_Secure = 'no'
		printInFile('1 Sequential ADD Insecured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientREST.py -o nul -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + '  -u ' + _Secure + ' -n ' + _N  + ' -m s -f ' + _File_Name)
		#printInFile('1 Sequential Del Insecured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		#os.system('sudo python MeasureClientREST.py -o del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('2 Batch ADD Insecured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientREST.py -o nul -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + '  -u ' + _Secure + ' -n ' + _N  + ' -m b -f ' + _File_Name)
		#printInFile('2 Batch Del Insecured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		#os.system('sudo python MeasureClientREST.py -o del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -n ' + _N  + ' -m b -f ' + _File_Name)

	os.system('sudo tc qdisc del dev enp0s25 root netem loss '+_Packet_Loss)
	os.system('sudo tc qdisc del dev enp0s25 root netem delay '+_Delay)
