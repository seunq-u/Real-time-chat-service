# 주제: 실시간 채팅 서비스 개발

내용: 파이썬 FastAPI와 WebSockets를 바탕으로 실시간으로 채팅 사이트를
만들어 보려고 합니다.
주제 선정에 어려움을 겪어 예상보다 시간이 오래 걸렸습니다. 늦게 보내드
려서 정말 죄송합니다.
아래는 간단하게 로직 구상과 초안을 만들어 본 것입니다.
로직은 Client -> URL 접속 HTTP 요청으로 웹페이지의 틀을 가져오고, 바
로 웹소켓으로 연결합니다. (수신되는 메시지 또한 실시간으로 받기 위함)
특정 사용자와 대화방 내에서 통신하고, 그 통신 내용은 다음과 같습니다. /
다중 대화방은 지원하지 않음

<사용자1 -> 서버 -> 사용자2 과정>
```json
{
    "type" : "send" 또는 "get",
    "timestamp" : <int: Unix Timestamp>,
    "from" : {
        "userID" : <int>, 
        "username" : <string>},
    "to" : {
        "userID" : <int>,
        "username" : <string>},
    "content" : <string>
}
```
이러한 JSON 데이터를 바탕으로 처리합니다.  
사용자가 상대방과의 대화를 불러오는 과정은 GET요청이며, 채팅 기록 저
장은 따로 DB를 사용할 계획은 아직 없습니다. (JSON 파일 저장) (쓴다면
MongoDB를 생각 중입니다.)  
아직 로그인과 보안에 대해서 고려된 사항은 없으나, 우선 서버와의 통신
구현을 우선순위로 생각하고 있습니다.  
사실 이렇게 보면 문자 SMS, 카톡, 인스타, 페이스북에서 딱 1:1 대화 기능
을 제공하는 서비를 개발해 보려고 합니다. (클론코딩..? 비슷하게 만들기)
다중 대화나, SNS의 게시물 기능은 오히려 일대일 대화 기능에서, HTTP
GET/POST 기능에서 추가한 서비스기 때문에 만약 지금 구상 중인 계획이 일
찍 끝날 수 있다면, 추후에 추가로 개발해 볼 계획입니다.  
감사합니다. 😀