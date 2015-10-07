<?php
$id=$_POST['id'];
$port=$_POST['port'];

include 'db_connect.php';

$sql = $conn->prepare('SELECT data from embedded.raspberry_port where id=? and port_no=?');
$sql->bind_param('ii',$id,$port);
$sql->execute();
$result = $sql->get_result();

if ($result->num_rows > 0) {
	if($row = $result->fetch_assoc())
	print $row['data'];
}
else 
	echo 'error';
$conn->close();
?>