<?php 
//Database Credentials
$db_user="root";
$db_pass="";
$db_server='localhost';
// Create connection
$conn = new mysqli($db_server, $db_user, $db_pass);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
?>