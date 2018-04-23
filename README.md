PRELIMINARIES:

a. The IP address of the server (routing device) should be 2002::1
b. For gRPC experiment, ports 50051, 50052, 50053, and 50054 should not be used by other applications (otherwise, A_gRPC_20Times, NullServer_gRPC.py, Server_gRPC_Pyroute, and Server_gRPC_Shell should be rewritted)
c. For REST experiment, ports 80, 81, 443, and 444 should be free (otherwise, NullServer_REST.py, Server_REST_Pyroute.py, and Server_REST_Shell.py should be rewritted)
d. For SSH experiment, SSH service should be active on the Server (routing device)
e. SRv6 and Pyroute2 should be installed and active on the Server (routing device)



BEFORE STARTING THE EXPERIMENTS:

This experiment is designed for a two machine secenario in which the SDN controller is considerd as the client and the routing device is considered as the Server.

1. At the beginig this repository should be cloned in to the local machines (both client (controller, and Server)
>> git clone https://github.com/mohammad59mt/srv6-southbound-api-evaluation.git

2. The IP address of the server should be 2002::1. To this end, first find the interface name in the server machine:
>> ip addr
3. Then Change the IP address of the selected interface in the Server
>> sudo ip addr add 2002::1/64 dev <interface name>



HOW TO PERFORM THE gRPC EXPERIMENT:

4. In the Client machine, move in to the gRPC folder
>> cd gRPC/
5. Open the A_gRPC_20Times.py file
>> nano A_gRPC_20Times.py
6. Change the value of "_Device" variable to the selected <interface> in step 2. Now press ctrl+o and then ctrl+x
7. In the server machine, to gRPC folder and run the gRPC servers.
>> sudo python Server_gRPC_Shell.py secure
>> sudo python Server_gRPC_Shell.py insecure
>> sudo python NullServer_gRPC.py secure
>> sudo python NullServer_gRPC.py insecure
8. In the client machine, run A_gRPC_20Times.py
>> sudo python A_gRPC_20Times.py
After the execution is finished the results of the Full process and Just communication parts (with and without packet loss and delay) will be in the gRPC/PureResults folder



HOW TO PERFORM THE REST EXPERIMENT:
9. In the Client machine, move in to the REST folder
>> cd REST/
10. Open the A_REST_20Times.py file
>> nano A_REST_20Times.py
11. Change the value of "_Device" variable to the selected <interface> in step 2. Now press ctrl+o and then ctrl+x
12. In the server machine, to REST folder and run the REST servers.
>> sudo python Server_REST_Shell.py secure
>> sudo python Server_REST_Shell.py insecure
>> sudo python NullServer_REST.py secure
>> sudo python NullServer_REST.py insecure
13. In the client machine, run A_REST_20Times.py
>> sudo python A_REST_20Times.py
After the execution is finished the results of the Full process and Just communication parts (with and without packet loss and delay) will be in the REST/PureResults folder



HOW TO PERFORM THE SSH EXPERIMENT:
14. In the Client machine, move in to the SSH folder
>> cd SSH/
15. Open the A_SSH_20Times.py file
>> nano A_SSH_20Times.py
16. Change the value of "_Device" variable to the selected <interface> in step 2. Now press ctrl+o and then ctrl+x
17. In the client machine, run A_REST_20Times.py
>> sudo python A_SSH_20Times.py
After the execution is finished the results of the Full process and Just communication parts (with and without packet loss and delay) will be in the SSH/PureResults folder



HOW TO PERFORM THE Pyroute2 and Shell EXPERIMENTS:
18. In the server, move in to the LocalRuleEnforcement folder
>> cd LocalRuleEnforcement/
19. Open A_LocalRuleEnforcement_20Times.py
>> nano A_LocalRuleEnforcement_20Times.py
20. Change the value of "_Device" variable to the selected <interface> in step 2. Now press ctrl+o and then ctrl+x
21. In the server, run A_LocalRuleEnforcement_20Times.py
>> sudo python A_LocalRuleEnforcement_20Times.py
After the execution is finished the results of the Full process and Just communication parts (with and without packet loss and delay) will be in the LocalRuleEnforcement folder
