<?php
$PYTHON_SCRIPT = "network_config.py";

$mac_address = $_GET['mac_address'];
$dhcp_version = $_GET['dhcp_version'];

$output = [];
$result = 0;
exec("python3 $PYTHON_SCRIPT '$mac_address' $dhcp_version", $output, $result);

if($result !== 0) {
  echo "<h1 style='color: red'>$output[0]</h1>";
  echo "<a href='/form.php'>Back to form</a>";
  exit;
}

$output = json_decode($output[0], true);

?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assignment#7 Process | IST105</title>
  </head>
  <body>
    <section>
      <h2>Input</h2>
      <p>Mac Address: <?= $mac_address ?>
      <p>DHCP Version: <?= $dhcp_version ?>
    </section>
    <section>
      <h2>Output (Assigned IP and Lease Info):</h2>
      <p>mac_address: <?= $output['mac_address'] ?></p>
      <p>Assigned IP: <?= $output['ip'] ?></p>
      <?php if(isset($output['lease_time'])): ?>
        <p>Lease Time: <?= $output['lease_time'] . " seconds" ?></p>
      <?php endif; ?>
    </section>
    <a href='/form.php'>Back to form</a>
  </body>
</html>
