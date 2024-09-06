# team_0906

회의
1. 호칭: 님 (최영주 님, 김형칠 님, 권윤우 님, 김동영 님)
2. 도움이 필요할때 손들고, 손든 사람 자리로 모이기
3. git 조장: 최영주님
4. 프로젝트 시간소요되는 장애요소: 파이썬과 mysql 연동, mysql 설치
5. 누구의 컴퓨터의 ip: 김형철님 

한명의 ip와 커리문 mysql
DB구축 
1. 파이썬을 기반으로 myql과 연결하여 코드작업
2. 최종파일 작업자: 김형철 님
3. 어떤 DB를 구축할 것인가?: 고객관리
    DB ip address: 192.168.0.92
    DB user id : test
    DB user pw : 88Einstein$

    Database name : team0906
-   **** DB connection은  창조관 303호실 수업 중에서는 가능합니다. 
    DB table name : customer
 <pre>
 <code>   
	id         	varchar(10),	/* customer ID */
	name		varchar(18),	/* customer name */
	gender		varchar(3), 	/* customer gender*/
	email		varchar(30),	/* customer e-mail */
	birthYear       varchar(4)  	/* customer bitthYear */
 </pre>
 </code> 


4. 어떻게 분담할 것인가?: c:김동영 님 r: 최영주 님 u: 권윤우 님 d: 김형철 님
5. 데이터베이스 만드는것: 김형철 님
6. 고객관리에 대한 테이블 명과 데이터 정리하기: 고객, 
함수 이름 이함수는 어떤 데이터를 함수가 하는일에 대해 코멘트남기기
일을 나누기에는 함수를 사용하는게 좋다
입력받아서 넣고, 있는거 보여주고 수정, 삭제
===============================================================================
절차
파이썬과 mysql연동하는 코드(connect.py/app.ini/config.py)만들기
    1.1 Mysql db 연동 테스트 :  01_connect.py 파일 

각자의 함수 정리
함수 통합
===============================================================================
git사용 규칙
1. 브랜치 만들때 본인 성제외 영문 이름으로 
2. commit명 코멘트 어떤작업(CRUD) 어떤수정(어떤내용을 수정)을 했는지
3. 코드 파일 명 통일 자신이 작업할 함수 풀네임 소문자
4. pull했을때 다른사람의 코드에 이상이 있을 경우 말을 하고 고친 후 push한다
5. 자신이 작성한 코드를 git에 올릴 경우 다른사람의 변경상황을 pull한후 push한다.
