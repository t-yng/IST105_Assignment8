<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assignment#8 | IST105</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        max-width: 400px;
        margin: 0 auto;
        padding: 20px;
      }

      h1 {
        text-align: center;
      }

      form {
        max-width: 300px;
        margin: 0 auto;
      }

      .form-group {
        position: relative;
        left: -16px;
        margin-bottom: 15px;
      }

      label {
        margin-right: 6px;
      }

      input {
        width: 140px;
        padding: 5px;
      }

      button {
        display: block;
        margin: 0 auto;
        padding: 10px 20px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
      }

      button:hover {
          background-color: #0056b3;
      }
    </style>
  </head>
  <body>
    <h1>Assignment#8 IST105</h1>
    <form action="/process.php" method="GET">
      <div class="form-group">
        <label for="mac_address">Mac Address: </label>
        <input type="text" id="mac_address" name="mac_address" placeholder="00:00:00:00:00:00" />
      </div>
      <div class="form-group">
        <label for="dhcp_version">DHCP Version: </label>
        <select id="dhcp_version" name="dhcp_version">
          <option value="DHCPv4">DHCPv4</option>
          <option value="DHCPv6">DHCPv6</option>
        </select>
      </div>
      <button>Submit</button>
    </form>
  </body>
</html>
