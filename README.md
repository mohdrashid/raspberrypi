# raspberrypi
This project is designed to help 
Use the sudo command below to move created header file [server_io.py] to python library folder in Raspberry Pi
<br>
<br>
<b>sudo mv ~/place_where_its_located/server_io.py /usr/lib/pythonx.y</b>
<br>
replace x.y with persion number of your python compiler
<br>

Once done the header can be imported by writing the following command in python:<br><br>
<b>import server_io as Server</b>
<br><br>
To access function in the header use Server.FunctionName() after importing the header. 
For example to get mac address, use Server.get_mac()
