% include header.tpl
<body>
% include menu.tpl
  <form action="add_numbers">
    Bulk add phone numbers:
    <textarea name="phone_numbers" rows="10" cols="12">
    </textarea>
    <br>
    <input type="submit" name="Add numbers">
  </form>
% include footer.tpl
