<%@ page language="java" contentType="text/html; charset=utf-8" pageEncoding="utf-8" %>
<html lang="kr"><head>
    <meta charset="utf-8">
    <title>회원가입 화면 - 하루 계획</title>

	<!-- bootstrap css -->
    <link rel="stylesheet" href="${pageContext.request.contextPath}/resources/css/bootstrap.min.css">
	
  </head>
<body class="text-center">

<nav class="navbar navbar-light bg-light">
	<div class="container-fluid">
	<a href="${pageContext.request.contextPath}/signin.jsp">뒤로 가기</a>
	하 루 계 획
	</div>
</nav>

    
<main class="form-signin w-100 m-auto">
  <form>
    <img class="mb-4" src="" alt="" width="72" height="57">임시 이미지 공간
    <h1 class="h3 mb-3 fw-normal">회원 가입</h1>

	<div class="form-floating">
      <input type="text" class="mt-3 mb-3 form-control" id="floatingName" placeholder="Name">
      <label for="floatingName">사용자명</label>
    </div>
    
    <div class="form-floating">
		<select class="mt-3 mb-3 form-select" id="floatingSelect" aria-label="성별 선택">
		   	<option selected>성별</option>
			<option value="1">남자</option>
			<option value="2">여자</option>
			<option value="3">미선택</option>			
 		</select>
		<label for="floatingSelect">성별을 선택하세요</label>
	</div>
	
	
    
    <div class="row g-2">
    	<div class="col-md">
  		  	<div class="form-floating">
   				<input type="email" class="mt-3 mb-3 form-control" id="floatingInput" placeholder="name@example.com">
  	 	 		<label for="floatingInput">이메일 주소</label>
  	 		</div>
  	 	</div>
  	 	<div class="col-md">
			<button class="mt-3 mb-3 w-100 btn" type="button">중복 이메일 확인</button>
		</div>
    </div>
    
    <div class="form-group">
    	<div class="form-group has-success">	
    		<div class="form-floating">
      			<input type="password" class="mt-3 mb-3 form-control" id="floatingPassword" placeholder="Password">
      			<label for="floatingPassword">비밀번호</label>
    		</div>
    	</div>
    	<div class="form-group has-danger">
    		<div class="form-floating">
      			<input type="password" class="mt-3 mb-3 form-control is-invalid" id="floatingInputInvalid" placeholder="Password">
      			<label for="floatingPassword">비밀번호 확인</label>
      			<div class="invalid-feedback">비밀번호가 일치하지 않습니다</div>
  			</div>
  		</div>
    </div>
    
    <div class="row g-5">
    	<div class="col-md">
    		<div class="form-floating">
				<select class="mt-3 mb-3 form-select" id="floatingSelect" aria-label="선호 활동 선택">
			    	<option selected>걷기</option>
			  		<option value="1">공원</option>
			  		<option value="2">산책로</option>
			  	  	<option value="3">강변</option>
			  	  	<option value="4">식물원</option>
	  			</select>
	  			<label for="floatingSelect">좋아하는 활동을 선택하세요</label>
			</div>
    	</div>
    	<div class="col-md">
    		<div class="form-floating">
				<select class="mt-3 mb-3 form-select" id="floatingSelect" aria-label="선호 활동 선택">
			    	<option selected>마시기</option>
			  		<option value="1">카페</option>
			  		<option value="2">칵테일바</option>
			  	  	<option value="3">주류</option>
			    	<option value="4"></option>
	  			</select>
	  			<label for="floatingSelect">좋아하는 활동을 선택하세요</label>
			</div>
    	</div>
    	<div class="col-md">
    		<div class="form-floating">
				<select class="mt-3 mb-3 form-select" id="floatingSelect" aria-label="선호 활동 선택">
			    	<option selected>먹기</option>
			  		<option value="1">한식</option>
			  		<option value="2">일식</option>
			  	  	<option value="3">중식</option>
			    	<option value="4">양식</option>
	  			</select>
	  			<label for="floatingSelect">좋아하는 활동을 선택하세요</label>
			</div>
    	</div>
    	<div class="col-md">
    		<div class="form-floating">
				<select class="mt-3 mb-3 form-select" id="floatingSelect" aria-label="선호 활동 선택">
			    	<option selected>놀기</option>
			  		<option value="1">당구장</option>
			  		<option value="2">PC방</option>
			  	  	<option value="3">스크린야구</option>
			    	<option value="4">클럽</option>
	  			</select>
	  			<label for="floatingSelect">좋아하는 활동을 선택하세요</label>
			</div>
    	</div>
    	<div class="col-md">
    		<div class="form-floating">
				<select class="mt-3 mb-3 form-select" id="floatingSelect" aria-label="선호 활동 선택">
			    	<option selected>보기</option>
			  		<option value="1">영화</option>
			  		<option value="2">연극</option>
			  	  	<option value="3">공연</option>
			    	<option value="4">만화</option>
	  			</select>
	  			<label for="floatingSelect">좋아하는 활동을 선택하세요</label>
			</div>
    	</div>
    </div>
    
	<div class="form-floating">
   		<input type="email" class="mt-3 mb-3 form-control" id="floatingInput" placeholder="name@example.com">
  		<label for="floatingInput">파트너 이메일 주소</label>
  	</div>
    
    <button class="w-100 btn btn-lg btn-primary" type="submit">회원가입</button>
    <p class="mt-5 mb-1 text-muted">2022-1 공개SW프로젝트</p>
    <p class="mt-1 mb-3 text-muted">코드해적단 CodePirates</p>
  </form>
</main>

</body>
</html>