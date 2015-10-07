<?php
$mac=$_POST['mac'];
$ip=$_POST['ip'];
include 'db_connect.php';

$sql = $conn->prepare('SELECT * from embedded.raspberry where mac=?');
$sql->bind_param('s', $mac);
$sql->execute();

$result = $sql->get_result();

if ($result->num_rows <= 0) {
	$sql = "INSERT INTO embedded.raspberry (ip, mac)
			VALUES ('".$ip."', '".$mac."')";

	if ($conn->query($sql) === TRUE) {
		echo "OK";
	} else {
		echo "Error: " . $sql . "<br>" . $conn->error;
	}
} else {
	$sql = "UPDATE embedded.raspberry set ip='
			".$ip."' where mac='".$mac."'";

	if ($conn->query($sql) === TRUE) {
		echo "OK";
	} else {
		echo "Error: " . $sql . "<br>" . $conn->error;
	}
}
$conn->close();
?>