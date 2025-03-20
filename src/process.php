<?php
$PYTHON_SCRIPT = "network_config.py";

$numbers = $_GET['numbers'];
$threshold = $_GET['threshold'];

$output = [];
$result = 0;
exec("python3 $PYTHON_SCRIPT '$numbers' $threshold", $output, $result);

if($result !== 0) {
  echo "<h1 style='color: red'>$output[0]</h1>";
  echo "<a href='/form.php'>Back to form</a>";
  exit;
}
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
      <p>Integers separated by commas: <?= $numbers ?>
      <p>Threshold: <?= $threshold ?>
    </section>
    <section>
      <h2>Results:</h2>
      <?php foreach($output as $key=>$value): ?>
        <?= $value ?>
      <?php endforeach ?>
    </section>
    <a href='/form.php'>Back to form</a>
  </body>
</html>
