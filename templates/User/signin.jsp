<%@ page language="java" contentType="text/html; charset=utf-8" pageEncoding="utf-8" %>


<html lang="en"><head>
    <meta charset="utf-8">
    <title>로그인 화면 - 하루 계획</title>

	<!-- bootstrap css -->
    <link rel="stylesheet" href="${pageContext.request.contextPath}/resources/css/bootstrap.min.css">
	
  </head>
<body class="text-center">

<nav class="navbar navbar-light bg-light">
	<div class="container-fluid">
	하 루 계 획
	</div>
</nav>

    
<main class="form-signin w-100 m-auto">
  <form>
    <img class="mb-4" src="" alt="" width="72" height="57">임시 이미지 공간</img>
    <h1 class="h3 mb-3 fw-normal">하루 계획</h1>

    <div class="form-floating">
      <input type="email" class="mt-3 mb-3 form-control" id="floatingInput" placeholder="name@example.com">
      <label for="floatingInput">이메일 주소</label>
    </div>
    <div class="form-floating">
      <input type="password" class="mt-3 mb-3 form-control" id="floatingPassword" placeholder="Password">
      <label for="floatingPassword">비밀번호</label>
    </div>

    <div class="checkbox mb-3">
      <label>
        <input type="checkbox" value="remember-me"> 이메일 기억하기
      </label>
    </div>
    <button class="w-100 btn btn-lg btn-primary" type="submit">로그인</button>
    <p class="mt-5 mb-1 text-muted">2022-1 공개SW프로젝트</p>
    <p class="mt-1 mb-3 text-muted">코드해적단 CodePirates</p>
  </form>
</main>

</body>
</html>