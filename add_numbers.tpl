% include header.tpl
<body>
% include menu.tpl
<div class="container">
<div class="jumbotron">
  <form action="add_numbers">
    Bulk add phone numbers:</br>
    <textarea name="phone_numbers" rows="10" cols="20"></textarea>
    <br/>
    <input type="submit" name="Add numbers" class="btn btn-default">
  </form>
</div>
</div>
% include footer.tpl
