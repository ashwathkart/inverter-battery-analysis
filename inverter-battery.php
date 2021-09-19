<html>

<title>
    Inverter Battery Analysis
</title>

<body>
<meta http-equiv="refresh" content="3000">
<?php
$con=mysqli_connect("localhost","ashwath","Avaritia@123","Inverter");
// Check connection
if (mysqli_connect_errno())
{
echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$result = mysqli_query($con,"SELECT * FROM Battery ORDER BY ID DESC LIMIT 0,10");

echo "<table border='1'>
<tr>
<th>ID</th>
<th>Product</th>
<th>Timestamp</th>
<th>Voltage</th>
</tr>";

while($row = mysqli_fetch_array($result))
{
echo "<tr>";
echo "<td>" . $row['ID'] . "</td>";
echo "<td>" . $row['Product'] . "</td>";
echo "<td>" . $row['Timestamp'] . "</td>";
echo "<td>" . $row['Voltage'] . "</td>";
echo "</tr>";
}
echo "</table>";

mysqli_close($con);
?>

</body>
</html>
