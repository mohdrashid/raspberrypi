<?php
$id=$_POST['id'];
$port=$_POST['port'];
$data=$_POST['data'];
include 'db_connect.php';

$sql = "UPDATE embedded.raspberry_port SET data=".$data." where id=".$id." and port_no=".$port."";
if ($conn->query($sql) === TRUE) {
	echo "OK";
} else {
	echo "Error: " . $sql . "<br>" . $conn->error;
}
$conn->close();
?>