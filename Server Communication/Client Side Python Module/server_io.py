#Usage
''''
Syntax +> get_ip(interface) returns ip of the network interface the raspberry, ethx for ethernet port and wlanx for wireless 
interface where x is number, for eg. eth0.
By default it return ip of eth0 interface
Usage  => get_ip('wlan0'): to get ip of wireless lan
---------------------------------------------------------------------------------------------------
Syntax +> get_mac(): returns the mac address of raspberry pi

Syntax +> set_server_ip(server_adds)
Usage  => set_server_ip('http://10.25.33.5') : call only if server ip differs from the default one
---------------------------------------------------------------------------------------------------
Syntax +>register_pi(path) or register_pi(path,parameter)
Usage  =>

register.php expects uid and ip in post request
<?php
$mac=$_POST['mac'];
$ip=$_POST['ip']; ...?>

register_pi('/embedded/register.php') : where '/embedded/register.php' is the path where the register script is stored or
register_pi('/embedded/register.php',{'uid':xyz,'ip_add':get_ip('eth0')}) : if the parameter used for registering
differs from the default server implementation
---------------------------------------------------------------------------------------------------
Syntax +>get_id(path) or get_id(path,parameter)
Usage  =>

get_id.php expects mac in post request
<?php
$id=$_POST['mac']; ...?>

id=get_id('/embedded/get_id.php') : Used to get id of raspberry in the server using default server implementation
id=get_id('/embedded/get_id.php',{'uid':xyz}) : if the parameter used for registering
differs from the default server implementation
---------------------------------------------------------------------------------------------------
Syntax +>register_port(path,port,direction) or register_port(path,port,direction,parameter)
Usage  =>

reg_port.php expects id,port and io in post request
<?
$id=$_POST['id'];
$port=$_POST['port'];
$io=$_POST['io'];...?>

register_port('/embedded/reg_port.php',7,1) : Register Port using default implementation
register_port('/embedded/reg_port.php',7,1,{'no':x,'port_no':y,'dir':z,'íp':w}): if the parameter used for registering
differs from the default server implementation
---------------------------------------------------------------------------------------------------
Syntax +>write_data(path,ids,port,data) or write_data(path,ids,port,data,parameter)
Usage  =>

insert_data.php expects id,port and data in post request
<?php
$id=$_POST['id'];
$port=$_POST['port'];
$data=$_POST['data'];..?>

write_data('/embedded/insert_data.php',id,7,56):Write Data to server using default server implementation
write_data('/embedded/insert_data.php',id,7,56,{'no':z,'p':y,'data':k}): if the parameter used for registering
differs from the default server implementation
---------------------------------------------------------------------------------------------------
Syntax +>read_data(path,ids,port) or read_data(path,ids,port,parameter)
Usage  =>

retrieve_data.php expects id and port in post request
<?php
$id=$_POST['id'];
$port=$_POST['port'];..?>

read_data('/embedded/retrieve_data.php',id,7): Read Data from server using default server implementation
read_data('/embedded/retrieve_data.php',id,7,{'x':y,'z':r,'d':c}): if the parameter used for registering
differs from the default server implementation
'''


import requests
'''http://www.python-requests.org/en/latest/ : Library for making requests to server'''
import uuid #Library  for getting Universally Unique Identifier
import socket,fcntl,struct
'''
socket: Library to provides access to socket interface
fcntl: performs file control and I/O control on file descrserver_addtors[variables] [Unix Library: Works only in unix based system]
struct: performs conversions between Python values and C structs represented as Python strings
'''
#Global Variables---------------------------------------
mac=hex(uuid.getnode()) # Gets MAC address of the device and stores it into variable mac
server_add='10.25.32.184' #Setting default server address
identity=0 #Id of the rasberry in the server
#End of Global Variables--------------------------------

def get_mac():
    return hex(uuid.getnode())

def set_server_ip(server_adds): #To be called only if the server server address changes
    global server_add #Tells compiler that this server_add is the server_add referenced above in global scope
    server_add=server_adds

def get_ip(interface='eth0'):#Return the server_add address of a given interface
    SIOCGIFADDR = 0x8915
    s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #Creates an endpoint for communication and returns a descrserver_addtor
    #Syntax : socket.socket(Address Family(IPv4,IPv6,etc),Socket Type(Datagram,stream communication,etc))
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(),SIOCGIFADDR
                ,struct.pack('256s',interface[:15]))[20:24])
        #Return server_addv4 address of the server
                                                                                
def register_pi(path,parameter=None): #Registers raspberry pi with server
        #Server takes parameters uid and server_add to register/update a device details in the server.
    if(parameter==None):
        parameter={'mac':mac,'ip':get_ip('eth0')}
    post_response=requests.post(url=server_add+path,data=parameter)
        #Using post methode offered by request library to write values to the server
    if(post_response.text=='OK'): #If server returns OK message go inside this block
        return True
    return False

def get_id(path,parameter={'mac':mac}): #Returns id of the raspberry pi as registered in the server
        #server uses uuid to uniquely identify each unit as server_add address can vary
    post_response=requests.post(url=server_add+path,data=parameter)
    global identity
    identity = post_response.text
    return identity

def register_port(path,port,direction,parameter=None): #Registers rasberry pi ports in the server for use as input/output
#0 for output and 1 for input in the direction field
    global identity
    if parameter==None:
        parameter={'id':identity,'port':port,'io':direction} 
        #server takes parameters id,port and io to register/update a port in the server
    post_response=requests.post(url=server_add + path
                                ,data=parameter)
    if(post_response.text=='OK'):
        return True
    return False

def read_data(path,ids,port,parameter=None): #Reads port data from server using unique id of the device and port number
#can be used to read port data from a different device using id of that device
    if parameter==None:
        parameter={'id':ids,'port':port}
    post_response=requests.post(url=server_add +path,data=parameter)
    if(post_response.text=='Error'):
        print "Error Reading value !!!!\nNo record exists for the given port number"
    else:
        return post_response.text
    
def write_data(path,ids,port,data,parameter=None):#Sends data of the given port of the given id to the serve 
    if parameter==None:
        parameter={'id':ids,'port':port,'data':data}
    post_response=requests.post(url=server_add +path,data=parameter)
    if(post_response.text=='OK'):
        return True
    return False
	

