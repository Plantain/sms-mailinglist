% include header.tpl
<body>
% include menu.tpl
<div class="container">
<div class="jumbotron">
  <form action="send_message">
    Message:</br>
    <textarea name="message" rows="3" cols="20"></textarea>
    </br>
    <input type="submit" name="Send message" class="btn btn-default">
  </form>
</div>
</div>
</body>
% include footer.tpl
