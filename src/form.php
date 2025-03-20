<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assignment#7 | IST105</title>
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

      .form-group {
        display: flex;
        justify-content: center;
        align-items: center;
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
    <h1>Assignment#7 IST105</h1>
    <form action="/process.php" method="GET">
      <div class="form-group">
        <label for="numbers">Numbers: </label>
        <input type="text" id="numbers" name="numbers" placeholder="3, 5, 7, 9" />
      </div>
      <div class="form-group">
        <label for="threshold">Threshold: </label>
        <input type="text" id="threshold" name="threshold" placeholder="4" />
      </div>
      <button>Submit</button>
    </form>
  </body>
</html>
