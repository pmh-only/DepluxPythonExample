# DepluxPythonExample
[Deplux](https://deplux.io)를 이용하여 무료로 Python 동적 호스팅을 할 수 있는 예제입니다.

### 동적 호스팅 시 확인해야 할것들
1. `Dockerfile`이 똑바로 작성되어 있는지 확인한다 ([파일 참고](Dockerfile))
2. 웹 호스팅시 listen할 포트가 `80`번으로 설정되어 있는지 확인한다
3. 내용이 압축파일 루트에 있는지 확인한다 (예시 참고)

잘못된 예:
```
hosting.zip
ㄴ hosting
   ㄴ app.py
```

올바른 예:
```
hosting.zip
ㄴ app.py
```

### 무료 동적 호스팅 사용법
* `Deplux#6728` 봇이 있는 채널에 `!deplux`를 입력해 가입한다
* `!hosting`을 입력해 호스팅 관리 메뉴로 들어가 새 호스팅을 생성한다
* DM으로 인증 번호가 오면 [이곳](https://deplux.io/Active)에서 호스팅을 활성화 한다
* 다시 `!hosting`을 입력해 호스팅 관리 메뉴가 뜨면 "호스팅 파일 업로드"를 선택하여 .zip 압축파일을 업로드 한다
* 도커가 생성될때까지 기다린다
