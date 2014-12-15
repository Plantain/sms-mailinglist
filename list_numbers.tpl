% include header.tpl
<body>
% include menu.tpl
<div class="container">
<div class="jumbotron">
<h3>Numbers:</h3>
 <table class="table">
    <tr>
      <th>#</th>
      <th>Number</th>
    </tr>
  % for number in numbers:
    <tr>
      <td>
      <td>{{number}}</td>
    </tr>
  % end
</table>
</div>
</div>
% include footer.tpl
