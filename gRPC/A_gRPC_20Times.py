import os

_Device = 'enp5s0'
_With_PacketLoss_And_Delay = True
_With_Out_PacketLoss_And_Delay = True
_Packet_Loss = '2%'
_Delay = '150ms'


_Prefix1 =  '2000::'
_N = '100'
_Segments = '2000::1e'
_File_Name = '' 

def printInFile(text):
	f1 = open(_File_Name+'.txt','a+')
	f1.write(text)
	f1.close()

#Full Process
_File_Name = 'gRPCResults20_FullProcess'  
if _With_Out_PacketLoss_And_Delay:
	#no packet loss
	for i in range(1,21):
		print('Secure communications round '+str(i))
		_Server_Address = '[2002::1]:50051'
		_Secure = 'yes'
		printInFile('1 Sequential ADD secured:\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o add  -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('1 Sequential Del secured:\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('2 Batch ADD secured:\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o  add -n ' + _N  + ' -m b -f ' + _File_Name)
		printInFile('2 Batch Del secured:\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m b -f ' + _File_Name)
		printInFile('3 Single Connection ADD secured:\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o  add -n ' + _N  + ' -m si -f ' + _File_Name)
		printInFile('3 Single Connection Del secured:\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m si -f ' + _File_Name)

		print('Insecure communications round '+str(i))
		_Secure = 'no'
		_Server_Address = '[2002::1]:50052'
		printInFile('1 Sequential ADD insecured:\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o add  -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('1 Sequential Del insecured:\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('2 Batch ADD insecured:\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o  add -n ' + _N  + ' -m b -f ' + _File_Name)
		printInFile('2 Batch Del insecured:\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m b -f ' + _File_Name)
		printInFile('3 Single Connection ADD insecured:\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o  add -n ' + _N  + ' -m si -f ' + _File_Name)
		printInFile('3 Single Connection Del insecured:\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m si -f ' + _File_Name)

if _With_PacketLoss_And_Delay:
	#add 10 percent packet loss
	os.system('sudo tc qdisc add dev enp0s25 root netem loss '+_Packet_Loss)
	os.system('sudo tc qdisc add dev enp0s25 root netem delay '+_Delay)
	for i in range(1,21):
		print('Secure communications with packet loss round '+str(i))
		_Secure = 'yes'
		_Server_Address = '[2002::1]:50051'
		printInFile('1 Sequential ADD secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o add  -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('1 Sequential Del secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('2 Batch ADD secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o  add -n ' + _N  + ' -m b -f ' + _File_Name)
		printInFile('2 Batch Del secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m b -f ' + _File_Name)
		printInFile('3 Single Connection ADD secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o  add -n ' + _N  + ' -m si -f ' + _File_Name)
		printInFile('3 Single Connection Del secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m si -f ' + _File_Name)

		print('Insecure communications with packet loss round '+str(i))
		_Secure = 'no'
		_Server_Address = '[2002::1]:50052'
		printInFile('1 Sequential ADD insecured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o add  -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('1 Sequential Del insecured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('2 Batch ADD insecured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o  add -n ' + _N  + ' -m b -f ' + _File_Name)
		printInFile('2 Batch Del insecured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m b -f ' + _File_Name)
		printInFile('3 Single Connection ADD insecured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o  add -n ' + _N  + ' -m si -f ' + _File_Name)
		printInFile('3 Single Connection Del insecured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m si -f ' + _File_Name)

	os.system('sudo tc qdisc del dev enp0s25 root netem loss '+_Packet_Loss)
	os.system('sudo tc qdisc del dev enp0s25 root netem delay '+_Delay)


#Just Communication
_File_Name = 'gRPCResults20_JustCommunicationPart' 
if _With_Out_PacketLoss_And_Delay:
	#no packet loss
	for i in range(1,21):
		print('Just Communication: Secure communications round '+str(i))
		_Server_Address = '[2002::1]:50053'
		_Secure = 'yes'
		printInFile('1 Sequential ADD secured:\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o add  -n ' + _N  + ' -m s -f ' + _File_Name)
		#printInFile('1 Sequential Del secured:\n')
		#os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('2 Batch ADD secured:\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o  add -n ' + _N  + ' -m b -f ' + _File_Name)
		#printInFile('2 Batch Del secured:\n')
		#os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m b -f ' + _File_Name)
		printInFile('3 Single Connection ADD secured:\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o  add -n ' + _N  + ' -m si -f ' + _File_Name)
		#printInFile('3 Single Connection Del secured:\n')
		#os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m si -f ' + _File_Name)

		print('Just Communication: Insecure communications round '+str(i))
		_Secure = 'no'
		_Server_Address = '[2002::1]:50054'
		printInFile('1 Sequential ADD insecured:\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o add  -n ' + _N  + ' -m s -f ' + _File_Name)
		#printInFile('1 Sequential Del insecured:\n')
		#os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('2 Batch ADD insecured:\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o  add -n ' + _N  + ' -m b -f ' + _File_Name)
		#printInFile('2 Batch Del insecured:\n')
		#os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m b -f ' + _File_Name)
		printInFile('3 Single Connection ADD insecured:\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o  add -n ' + _N  + ' -m si -f ' + _File_Name)
		#printInFile('3 Single Connection Del insecured:\n')
		#os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m si -f ' + _File_Name)

if _With_PacketLoss_And_Delay:
	#add 10 percent packet loss
	os.system('sudo tc qdisc add dev enp0s25 root netem loss '+_Packet_Loss)
	os.system('sudo tc qdisc add dev enp0s25 root netem delay '+_Delay)
	for i in range(1,21):
		print('Just Communication: Secure communications with packet loss round '+str(i))
		_Secure = 'yes'
		_Server_Address = '[2002::1]:50053'
		printInFile('1 Sequential ADD secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o add  -n ' + _N  + ' -m s -f ' + _File_Name)
		#printInFile('1 Sequential Del secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		#os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('2 Batch ADD secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o  add -n ' + _N  + ' -m b -f ' + _File_Name)
		#printInFile('2 Batch Del secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		#os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m b -f ' + _File_Name)
		printInFile('3 Single Connection ADD secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o  add -n ' + _N  + ' -m si -f ' + _File_Name)
		#printInFile('3 Single Connection Del secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		#os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m si -f ' + _File_Name)

		print('Just Communication: Insecure communications with packet loss round '+str(i))
		_Secure = 'no'
		_Server_Address = '[2002::1]:50054'
		printInFile('1 Sequential ADD insecured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o add  -n ' + _N  + ' -m s -f ' + _File_Name)
		#printInFile('1 Sequential Del insecured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		#os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m s -f ' + _File_Name)
		printInFile('2 Batch ADD insecured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o  add -n ' + _N  + ' -m b -f ' + _File_Name)
		#printInFile('2 Batch Del insecured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		#os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m b -f ' + _File_Name)
		printInFile('3 Single Connection ADD insecured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _Secure + ' -o  add -n ' + _N  + ' -m si -f ' + _File_Name)
		#printInFile('3 Single Connection Del insecured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		#os.system('sudo python MeasureClientgRPC.py -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _Secure + ' -o del -n ' + _N  + ' -m si -f ' + _File_Name)

	os.system('sudo tc qdisc del dev enp0s25 root netem loss '+_Packet_Loss)
	os.system('sudo tc qdisc del dev enp0s25 root netem delay '+_Delay)
