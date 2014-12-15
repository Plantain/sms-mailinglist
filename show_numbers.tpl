% include header.tpl
<body>
% include menu.tpl
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
% include footer.tpl
