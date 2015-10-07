<?php
$id=$_POST['id'];
$port=$_POST['port'];
$io=$_POST['io'];
include 'db_connect.php';

$sql = $conn->prepare('SELECT * from embedded.raspberry_port where id=? and port_no=?');
$sql->bind_param('dd', $id,$port);
$sql->execute();

$result = $sql->get_result();

if ($result->num_rows == 0) {
	$sql = 'INSERT INTO embedded.raspberry_port (id,port_no,in_out)
			VALUES ('.$id.','.$port.','.$io.')';
} else {
    $sql = "UPDATE embedded.raspberry_port SET in_out=".$io."
			where id=".$id." and port_no=".$port."";
}
if ($conn->query($sql) === TRUE) {
		echo "OK";
	} else {
		echo "Error: " . $sql . "<br>" . $conn->error;
	}
$conn->close();
?>