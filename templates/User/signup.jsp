<%@ page language="java" contentType="text/html; charset=utf-8" pageEncoding="utf-8" %>
<html lang="kr"><head>
    <meta charset="utf-8">
    <title>회원가입 화면 - 하루 계획</title>

	<!-- bootstrap css -->
    <link rel="stylesheet" href="${pageContext.request.contextPath}/resources/css/bootstrap.min.css">
	
	<style>
	.bg-light{
		height: 1053px;
		padding-top: 55px;
		padding-bottom: 75px;
	}
	.flex-fill.mx-xl-5.mb-2{
		margin: 0 auto;
		width: 700px;
		padding-right: 7rem;
		padding0-left: 7rem;
	}
	</style>
	
  </head>
<body class="text-center">

<nav class="navbar navbar-light">
	<div class="container-fluid">
	<a href="${pageContext.request.contextPath}/signin.jsp">뒤로 가기</a>
	하 루 계 획
	</div>
</nav>

<main class="form-signin w-100 bg-light">
  <form>
    <img class="mb-4" src="" alt="" width="72" height="57">임시 이미지 공간
    <h1 class="h3 mb-3 fw-normal">회원 가입</h1>
	
	<!-- 이메일 -->
    <div class="form-group">
    	<div class="row g-2">
    		<div class="col-md">
  		  		<div class="form-floating">
   					<input type="email" class="mt-3 mb-3 form-control" id="UserEmail" placeholder="name@example.com">
  	 	 			<label for="floatingInput">이메일 주소</label>
  	 			</div>
  	 		</div>
  	 		<div class="col-md">
				<button class="mt-3 mb-1 w-100 btn" type="button">중복 이메일 확인</button>
			</div>
    	</div>
    </div>
    
    <!-- 비밀번호/비밀번호 확인 -->
    <div class="form-group has-success">	
    	<div class="form-floating">
    		<input type="password" class="mt-3 mb-3 form-control is-valid" id="UserPassword" placeholder="Password">
    		<label for="floatingPassword" for="inputValid">비밀번호</label>
    		<div class="valid-feedback"></div>
    	</div>
    </div>
    <div class="form-group has-danger">
    	<div class="form-floating">
    		<input type="password" class="mt-3 mb-3 form-control is-invalid" id="UserPasswordCheck" placeholder="Password">
    		<label for="floatingPassword" for="inputInvalid">비밀번호 확인</label>
    		<div class="invalid-feedback">비밀번호가 일치하지 않습니다</div>
  		</div>
  	</div>
    
    <!-- 사용자명 -->
    <div class="form-floating">
      <input type="text" class="mt-3 mb-3 form-control" id="UserName" placeholder="Name">
      <label for="floatingName">사용자명</label>
    </div>
    
    <!-- 사용자 성별 -->
    <div class="form-floating">
		<select class="mt-3 mb-3 form-select" id="UserSex" aria-label="성별 선택">
		   	<option selected>성별</option>
			<option value="1">남자</option>
			<option value="2">여자</option>
			<option value="3">미선택</option>			
 		</select>
		<label for="floatingSelect">성별을 선택하세요</label>
	</div>
	
	<!-- 사용자 생년월일 -->
   	<div class="row g-3">
   		<div class="col-md">
   			<div class="form-floating">
   				<input type="text" class="mt-3 mb-3 form-control" id="UserBirthYear" aria-label="년 선택">
   				<label for="floatingInput">생년(4자리)을 입력하세요</label>
   			</div>
   		</div>
   		<div class="col-md">
   			<div class="form-floating">
   				<select class="mt-3 mb-3 form-select" id="UserBirthMonth" aria-label="월 선택">
			    	<option selected>월</option>
			  		<option value="1">1</option>
			  		<option value="2">2</option>
			  	  	<option value="3">3</option>
			  	  	<option value="4">4</option>
			  	  	<option value="5">5</option>
			  	  	<option value="6">6</option>
			  	  	<option value="7">7</option>
			  	  	<option value="8">8</option>
			  	  	<option value="9">9</option>
			  	  	<option value="10">10</option>
			  	  	<option value="11">11</option>
			  	  	<option value="12">12</option>
	  			</select>
	  			<label for="floatingSelect">생월을 선택하세요</label>
   			</div>	
   		</div>
   		<div class="col-md">
   			<div class="form-floating">
   				<input type="text" class="mt-3 mb-3 form-control" id="UserBirthDay" aria-label="일 선택">
   				<label for="floatingInput">생일을 입력하세요</label>
   			</div>
   		</div>
   	</div>
    
    <!-- 사용자 선호 활동 -->
    <div class="row g-5">
    	<div class="col-md">
    		<div class="form-floating">
				<select class="mt-3 mb-3 form-select" id="UserPreferenceWalk" aria-label="선호 활동 선택">
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
				<select class="mt-3 mb-3 form-select" id="UserPreferenceDrink" aria-label="선호 활동 선택">
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
				<select class="mt-3 mb-3 form-select" id="UserPreferenceEat" aria-label="선호 활동 선택">
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
				<select class="mt-3 mb-3 form-select" id="UserPreferencePlay" aria-label="선호 활동 선택">
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
				<select class="mt-3 mb-3 form-select" id="UserPreferenceWatch" aria-label="선호 활동 선택">
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
    
    <!-- 파트너 이메일 -->
	<div class="form-floating">
   		<input type="email" class="mt-3 mb-3 form-control" id="PartnerEmail" placeholder="name@example.com">
  		<label for="floatingInput">파트너 이메일 주소</label>
  	</div>
    
    <button class="w-100 btn btn-lg btn-primary" type="submit">회원가입</button>
    <p class="mt-5 mb-1 text-muted">2022-1 공개SW프로젝트</p>
    <p class="mt-1 mb-3 text-muted">코드해적단 CodePirates</p>
    
  </form>
</main>
</body>
</html>
