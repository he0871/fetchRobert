# fetchRobert
online test

client side has 4 scripts which are coded by golang.
client.go : send the size of the map (how many rows and columns) to server
start.go : send the start position to the server
goal.go : send the destination position to server
cost.go : send the cost table to servet
client can send information in any order.

using 'go run' command exeute golang scripts in command prompt like this:
go run client.go



server side has 3 python scripts.
We only need to run app.py which is considered to be a main script.

app.py : build up a http server and distribute the incoming message.
MsgParse.py : extract the information from http packet
SearchPath.py : find the shortest path based on the received information.

BWT:
The port num is 5000 which is default value of Flask
This program treat all the obstacles are same and impenetrable.

Coming soon:
Customer port number: users can set their own port #
Handle error gracefully: firstly, if there is no path from start point to goal?
More test case

background:
https://github.com/calvinfeng/walle_finds_eve
