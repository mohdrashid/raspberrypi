<?php
$id=$_POST['mac']; //Takes mac as name value pair in post request

include 'db_connect.php';

$sql = $conn->prepare('SELECT id from embedded.raspberry where mac=?');
$sql->bind_param('s',$id); //Replaces ? in query with value in $id
$sql->execute();
$result = $sql->get_result();

if ($result->num_rows > 0) {

	if($row = $result->fetch_assoc())
	print $row['id'];

}
$conn->close();
?>