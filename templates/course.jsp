<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%request.setCharacterEncoding("UTF-8"); %>
<!DOCTYPE html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" pageEncoding = "UTF-8"% />
<title>jQuery UI Sortable</title>
<link href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css" rel="stylesheet" type="text/css" />
<style>
.itemBox {
    border:solid 1px black;
    width:400px;
    height:200px;
    padding:10px;
    margin-bottom:10px;
}
.itemBoxHighlight {
    border:solid 1px black;
    width:400px;
    height:200px;
    padding:10px;
    margin-bottom:10px;
    background-color:yellow;
}
.deleteBox {
    float:right;
    display:none;
    cursor:pointer;
}
</style>
<style>
#sortable { list-style-type: none; margin: 0; padding: 0; width: 400px; height:400px}
#sortable li { margin: 0 3px 3px 3px; padding: 0.4em; padding-left: 1.5em; font-size: 1.4em; height: 100px; }
#sortable li span { position: absolute; margin-left: -1.3em; }
</style>
<script type="text/javascript" src="https://code.jquery.com/jquery-1.12.4.min.js" ></script>
<script type="text/javascript" src="https://code.jquery.com/ui/1.12.1/jquery-ui.js" ></script>
<script type="text/javascript">

$(function() {
    $("#itemBoxWrap").sortable({
        placeholder:"itemBoxHighlight",
        start: function(event, ui) {
            ui.item.data('start_pos', ui.item.index());
        },
        stop: function(event, ui) {
            var spos = ui.item.data('start_pos');
            var epos = ui.item.index();
			      reorder();
        }
    });
    
    $( "#sortable" ).sortable();
    $( "#sortable" ).disableSelection();
});

function reorder() {
    $(".itemBox").each(function(i, box) {
        $(box).find(".itemNum").html(i + 1);
    });
}

</script>
<%
String s1 = request.getParameter("select1");
String s2 = request.getParameter("select2");
String s3 = request.getParameter("select3");
%>
</head>
<body>
<br />
<div id="itemBoxWrap"></div>
<br />
<ul id="sortable">
  <li class="ui-state-default"><img src="임시 이미지" width="50" height="50" /><span class="ui-icon ui-icon-arrowthick-2-n-s"></span><%=s1 %></li>
  <li class="ui-state-default"><img src="임시 이미지" width="50" height="50" /><span class="ui-icon ui-icon-arrowthick-2-n-s"></span><%=s2 %></li>
  <li class="ui-state-default"><img src="임시 이미지" width="50" height="50" /><span class="ui-icon ui-icon-arrowthick-2-n-s"></span><%=s3 %></li>
</ul>
</body>
</html>