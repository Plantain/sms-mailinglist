% include('header.tpl')
<body>
  <div class="navbar navbar-default" role="navigation">
    <div class="navbar-header">
      <a class="navbar-brand" href="/">SMS Mailing list</a>
    </div>

    <ul class="nav navbar-nav">
      <li><a href="send_message">Send Message</a></li>
      <li><a href="list_numbers">List Numbers</a></li>
      <li><a href="add_numbers">Add Numbers</a></li>
    </ul>
  </div>

  <form action="send_message">
    Message: 
    <textarea name="message" rows="10" cols="12"></textarea>
    <input type="submit" name="Send message">
  </form>

  <form action="add_phone_numbers">
    Bulk add phone numbers: 
    <textarea name="phone_numbers" rows="10" cols="12">
    </textarea>
    <br>
    <input type="submit" name="Add numbers">
  </form>
  <table class="table">
    <tr>
      <th>#</th>
    </tr>
  % for number in numbers:
    <tr>
      <td>{{number}}</td>
    </tr>
  % end
  </table>
</body>
</html>
