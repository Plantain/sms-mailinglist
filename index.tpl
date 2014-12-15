<html>
<head>
	<title>SMS mailing list</title>
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
</head>
<body>
<form action="send_message">
Message:
<textarea name="message" rows="10" cols="12"></textarea>
</form>
<form action="add_phone_numbers">
Bulk add phone numbers:
<textarea name="phone_numbers" rows="10" cols="12"></textarea>
</br>
<input type="submit" name="Add numbers">
</form>
<table class="table">
<tr><th>#</th></tr>
% for number in numbers:
    <tr>
      <td>{{number}}</td>
    </tr>
% end
</table>
</body>
</html>
