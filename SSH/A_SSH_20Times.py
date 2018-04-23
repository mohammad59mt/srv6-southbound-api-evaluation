import os

_With_PacketLoss_And_Delay = True
_With_Out_PacketLoss_And_Delay = True
_UserName = 'mahdi'
_Password = '110'
_Device = 'enp5s0'
_Packet_Loss = '2%'
_Delay = '150ms'



_N = '100'
_Segments = '2000::1e'
_Prefix1 =  '2000::'
_File_Name = ''
_Server_Address = '2002::1'

def printInFile(text):
	f1 = open(_File_Name+'.txt','a+')
	f1.write(text)
	f1.close()
#Full process
#_File_Name = _File_Location + 'PureResults/SSHResults20_FullProcess'
_File_Name = 'SSHResults20_FullProcess'
if _With_Out_PacketLoss_And_Delay:
	#no packet loss
	for i in range(1,21):
		print('Secure communications round '+str(i))
		printInFile('1 Sequential ADD secured:\n')
		os.system('sudo python MeasureSSHexecutionTime.py addsr -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m s -f '+_File_Name)
		#printInFile('1 Sequential Del secured:\n')
		#os.system('sudo python MeasureSSHexecutionTime.py del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m s -f '+_File_Name)
		os.system('sudo python MeasureSSHexecutionTime.py del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m b -f '+_File_Name+'_TEMP_For_Delete')

		printInFile('2 Batch ADD secured:\n')
		os.system('sudo python MeasureSSHexecutionTime.py addsr -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m b -f '+_File_Name)
		#printInFile('2 Batch Del secured:\n')
		#os.system('sudo python MeasureSSHexecutionTime.py del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m b -f '+_File_Name)
		os.system('sudo python MeasureSSHexecutionTime.py del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m b -f '+_File_Name+'_TEMP_For_Delete')

		printInFile('3 Single Connection ADD secured:\n')
		os.system('sudo python MeasureSSHexecutionTime.py addsr -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m si -f '+_File_Name)
		#printInFile('3 Single Connection Del secured:\n')
		#os.system('sudo python MeasureSSHexecutionTime.py del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m si -f '+_File_Name)
		os.system('sudo python MeasureSSHexecutionTime.py del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m b -f '+_File_Name+'_TEMP_For_Delete')

if _With_PacketLoss_And_Delay:
	#add packet loss and delay
	os.system('sudo tc qdisc add dev enp0s25 root netem loss '+_Packet_Loss)
	os.system('sudo tc qdisc add dev enp0s25 root netem delay '+_Delay)
	for i in range(1,21):
		print('Secure communications with packet loss round '+str(i))
		printInFile('1 Sequential ADD secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureSSHexecutionTime.py addsr -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m s -f '+_File_Name)
		#printInFile('1 Sequential Del secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		#os.system('sudo python MeasureSSHexecutionTime.py del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m s -f '+_File_Name)
		os.system('sudo python MeasureSSHexecutionTime.py del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m b -f '+_File_Name+'_TEMP_For_Delete')

		printInFile('2 Batch ADD secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureSSHexecutionTime.py addsr -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m b -f '+_File_Name)
		#printInFile('2 Batch Del secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		#os.system('sudo python MeasureSSHexecutionTime.py del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m b -f '+_File_Name)
		os.system('sudo python MeasureSSHexecutionTime.py del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m b -f '+_File_Name+'_TEMP_For_Delete')

		printInFile('3 Single Connection ADD secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python MeasureSSHexecutionTime.py addsr -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m si -f '+_File_Name)
		#printInFile('3 Single Connection Del secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		#os.system('sudo python MeasureSSHexecutionTime.py del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m si -f '+_File_Name)
		os.system('sudo python MeasureSSHexecutionTime.py del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m b -f '+_File_Name+'_TEMP_For_Delete')

	os.system('sudo tc qdisc del dev enp0s25 root netem loss '+_Packet_Loss)
	os.system('sudo tc qdisc del dev enp0s25 root netem delay '+_Delay)



#Just Communication Servers
#_File_Name = _File_Location + 'PureResults/SSHResults20_JustCommunicationPart'
_File_Name = 'SSHResults20_JustCommunicationPart'
if _With_Out_PacketLoss_And_Delay:
	#no packet loss
	for i in range(1,21):
		print('Just Communication: Secure communications round '+str(i))
		printInFile('1 Sequential ADD secured:\n')
		os.system('sudo python NullMessage_MeasureSSHexecutionTime.py addsr -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m s -f '+_File_Name)
		#printInFile('1 Sequential Del secured:\n')
		#os.system('sudo python NullMessage_MeasureSSHexecutionTime.py del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m s -f '+_File_Name)
		printInFile('2 Batch ADD secured:\n')
		os.system('sudo python NullMessage_MeasureSSHexecutionTime.py addsr -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m b -f '+_File_Name)
		#printInFile('2 Batch Del secured:\n')
		#os.system('sudo python NullMessage_MeasureSSHexecutionTime.py del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m b -f '+_File_Name)
		printInFile('3 Single Connection ADD secured:\n')
		os.system('sudo python NullMessage_MeasureSSHexecutionTime.py addsr -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m si -f '+_File_Name)
		#printInFile('3 Single Connection Del secured:\n')
		#os.system('sudo python NullMessage_MeasureSSHexecutionTime.py del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m si -f '+_File_Name)

if _With_PacketLoss_And_Delay:
	#add packet loss and delay
	os.system('sudo tc qdisc add dev enp0s25 root netem loss '+_Packet_Loss)
	os.system('sudo tc qdisc add dev enp0s25 root netem delay '+_Delay)
	for i in range(1,21):
		print('Just Communication: Secure communications with packet loss round '+str(i))
		printInFile('1 Sequential ADD secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python NullMessage_MeasureSSHexecutionTime.py addsr -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m s -f '+_File_Name)
		#printInFile('1 Sequential Del secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		#os.system('sudo python NullMessage_MeasureSSHexecutionTime.py del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m s -f '+_File_Name)
		printInFile('2 Batch ADD secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python NullMessage_MeasureSSHexecutionTime.py addsr -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m b -f '+_File_Name)
		#printInFile('2 Batch Del secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		#os.system('sudo python NullMessage_MeasureSSHexecutionTime.py del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m b -f '+_File_Name)
		printInFile('3 Single Connection ADD secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		os.system('sudo python NullMessage_MeasureSSHexecutionTime.py addsr -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -s ' + _Segments + ' -d ' + _Device + ' -e encap -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m si -f '+_File_Name)
		#printInFile('3 Single Connection Del secured ('+_Packet_Loss +' loss,'+_Delay+' delay):\n')
		#os.system('sudo python NullMessage_MeasureSSHexecutionTime.py del -i ' + _Server_Address + ' -p ' + _Prefix1 + ' -d ' + _Device + ' -u ' + _UserName + ' -w ' + _Password + ' -n ' + _N  + ' -m si -f '+_File_Name)

	os.system('sudo tc qdisc del dev enp0s25 root netem loss '+_Packet_Loss)
	os.system('sudo tc qdisc del dev enp0s25 root netem delay '+_Delay)
