% include header.tpl
<body>
% include menu.tpl
  <form action="send_message">
    Message:
    <textarea name="message" rows="10" cols="12"></textarea>
    <input type="submit" name="Send message">
  </form>
</body>
% include footer.tpl
