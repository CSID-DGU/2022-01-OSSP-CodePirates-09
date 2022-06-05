<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%request.setCharacterEncoding("UTF-8"); %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=bf769654ad431e4d3f835edc2656c83c&libraries=services"></script>
<title>Insert title here</title>
   <link href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css" rel="stylesheet" type="text/css" />
   <script type="text/javascript" src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
   <script type="text/javascript" src="https://code.jquery.com/ui/1.12.1/jquery-ui.js" ></script>
   <link rel="stylesheet" href="bootstrap.css">
   <link rel="stylesheet" href="bootstrap.min.css">
   <%
		String s1 = request.getParameter("select1");
		String s2 = request.getParameter("select2");
		String s3 = request.getParameter("select3");
	%>

</head>
<style>
    /*body{
  		margin: 0 auto;
  		width: 300px;
	}*/
    ul li{
        list-style: none;
        width: 500px;
        height: 150px;
        font-size: 20px;
        position : relative;
	 	left : 50%;
	 	margin : 0px 0px 0px -250px;
        color: #f3969a;
        border: 1px solid;
        border-color: #f3969a;
        padding: 0.375rem 0.75rem;
 		font-size: 1rem;
		border-radius: 0.4rem;
  		transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    }
    li:hover {
        cursor: pointer;
    }

    .itemBoxHighlight {
        border:solid 1px black;
        width: 500px;
        height: 150px;
        background-color:#f9c7ca;
    }
    
	.wrapper {
	 	position : relative;
	 	width:500px;
	 	height:400px;
	 	left : 50%;
	 	margin : 100px 0px 0px -250px;
	}
</style>
<body>

<div id="map" class = "wrapper"></div>
<!-- 크롤링을 통한 데이터 입력 -->
<ul id="sortable" > 
  <li class="btn-outline-secondary" id = "1" value = "1" data-lat ="33.452344169439975" data-lon = "126.56878163224233" ><img src="임시 이미지" width="50" height="50" /><%=s1 %><span class="ui-icon ui-icon-arrowthick-2-n-s"></span></li>
  <li class="btn-outline-secondary" id = "2" value = "2" data-lat ="33.452739313807456" data-lon = "126.5709308145358"><img src="임시 이미지" width="50" height="50" /><span class="inner2"><%=s2 %><span class="ui-icon ui-icon-arrowthick-2-n-s"></span></span></li>
  <li class="btn-outline-secondary" id = "3" value = "3" data-lat ="33.45178067090639" data-lon = "126.5726886938753"><img src="임시 이미지" width="50" height="50" /><span class="inner3"><%=s3 %><span class="ui-icon ui-icon-arrowthick-2-n-s"></span></span></li>
</ul>

</body>
<script>
    //$("#sortable").sortable();
    var linePath;
    var polyline;
    var distance;
    var markers;
    var iwContent;
    var iwPosition;
    var positions;
    
    var mapContainer = document.getElementById('map'), // 지도를 표시할 div
	mapOption = {
	center: new kakao.maps.LatLng(33.450701, 126.570667), // 지도의 중심좌표
    level: 4, // 지도의 확대 레벨
    mapTypeId : kakao.maps.MapTypeId.ROADMAP // 지도종류
	};
	var map = new kakao.maps.Map(mapContainer, mapOption);
	
	rootc();
	marking();
    $("#sortable").disableSelection(); // 아이템 내부의 글자를 드래그 해서 선택하지 못하도록 하는 기능
    $("#sortable").sortable({
        placeholder:"itemBoxHighlight", /* 이동할 위치 css 적용  */
        start:function(event,ui){
            // 드래그 시작 시 호출
        },
        stop:function(event,ui){
            // 드래그 종료 시 호출
            reorder();
            del();
            rootc();
        }
   });

    function reorder() {
        $("#sortable li").each(function(i, box) {
            $(box).val(i + 1);
        });
    }
    
    function marking(){
    	markers = [];
        iwContent = [];
        iwPosition = [];
        positions = [];
        for(var i=0;i<3;i++){
        	positions[i] = new kakao.maps.LatLng(document.getElementsByTagName('li')[i].dataset.lat, document.getElementsByTagName('li')[i].dataset.lon);
        	marker = new kakao.maps.Marker({
           		map: map,
           		position: positions[i]
            	//position: new kakao.maps.LatLng(document.getElementsByTagName('li')[i].dataset.lat, document.getElementsByTagName('li')[i].dataset.lon)
        		});
        	marker.setMap(map); // 지도에 올린다.
        	markers.push(marker);
        	
        	iwContent[i] = '<div>' + document.getElementsByTagName('li')[i].value+ '</div>';
        	
        	var infowindow = new kakao.maps.InfoWindow({
                content: iwContent[i] // 인포윈도우에 표시할 내용
            });
        	kakao.maps.event.addListener(marker, 'mouseover', makeOverListener(map, marker, infowindow));
            kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(infowindow));
    	}
        map.setCenter(new kakao.maps.LatLng(document.getElementsByTagName('li')[1].dataset.lat,document.getElementsByTagName('li')[1].dataset.lon));
    	
    }
    function rootc(){
    	linePath = [
    	    new kakao.maps.LatLng(document.getElementsByTagName('li')[0].dataset.lat, document.getElementsByTagName('li')[0].dataset.lon),
    	    new kakao.maps.LatLng(document.getElementsByTagName('li')[1].dataset.lat, document.getElementsByTagName('li')[1].dataset.lon),
    	    new kakao.maps.LatLng(document.getElementsByTagName('li')[2].dataset.lat, document.getElementsByTagName('li')[2].dataset.lon) 
    	];

    	// 지도에 표시할 선을 생성합니다
    	polyline = new kakao.maps.Polyline({
    	    path: linePath, // 선을 구성하는 좌표배열 입니다
    	    strokeWeight: 5, // 선의 두께 입니다
    	    strokeColor: '#FFAE00', // 선의 색깔입니다
    	    strokeOpacity: 0.7, // 선의 불투명도 입니다 1에서 0 사이의 값이며 0에 가까울수록 투명합니다
    	    strokeStyle: 'solid' // 선의 스타일입니다
    	});
    	polyline.setMap(map); 
    }

    function makeOverListener(map, marker, infowindow) {
        return function() {
            infowindow.open(map, marker);
        };
    }

    function makeOutListener(infowindow) {
        return function() {
            infowindow.close();
        };
    }
    function del(){//경로 지우기
    	linePath = null;
    	polyline.setMap(null);
    }

    
</script>
</html>
