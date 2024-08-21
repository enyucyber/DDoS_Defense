# DDoS_Defense

Simulation of DDoS attack and defense methods program instructions:

Text files:

tempHistory.txt stores all of traffic for traffic analysis.
blackList.txt stores all traffic have been blacklisted.
stoppedTraffic stores all of traffic in the blacklist have been stopped.


Steps to run the program:

1. Command "python .\refresh.py" should be run first to clear the content of tempHistory.txt, blackList.txt and stoppedTraffic.txt.
2. Split 2 more terminals.
3. Run "python .\server.py" to start the server side.
4. Run "python .\client.py" to start the client side. 
5. Wait couple seconds, then run "python .\DDoSAttack.py" to start the DDoS attack.
6. Wait until you see "--------Timed out! A Client's Request was Aborted!--------" in the client side terminal. It means the DDoS attack is successful.
7. Kill all the terminals.
8. Run "python .\tracfficsAnalysis.py" to analyse traffic history to generate blacklist.
9. Run "python .\server.py" to start the server side again.
10. Run "python .\DDoSAttack.py" again to start the DDoS attack in another terminal again.
11. You will see some revceived connections were terminated in server side terminal.
12. Kill all the terminals.
13. You can set the value of threshold 1 (Recommend change it from 100000 to 1000) and threshold 2 (Recommend change it from 100020 to 1020) at the top of server.py, then save it. Their values are the maximum number of accepted connections respectively. Threshold 1 is for limit the acceptance rate for server. Threshold 2 is for shuting down the server.
14. Run "python .\server.py" to start the server side again.
15. Run "python .\DDoSAttack.py" to start the DDoS attack in another terminal again.
16. When you see "---------------Acceptance Rate is limited!---------------", it means the number of connections in server reached the threashold 1.
17. Later you will see "---------------Server has been Shut Down!---------------" and a alert window. It means the number of connections in server reached the threshold 2. How soon you will see them depends on the values of threshold settings you set.
18. Kill all the terminals.
