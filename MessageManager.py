# message manager
import time
import websockets
from dataclasses import dataclass
from datetime import datetime
import FileIO

@dataclass
class Message:
    type: str # 받는 사람 기준
    timestamp: int

    user: list[dict]

    history: dict

    # @property
    # def timestamp_as_datetime(self):
    #     return datetime.fromtimestamp(self.timestamp)

@dataclass
class Chat:
    type: str # 받는 사람 기준
    from_user: dict
    to_user: dict
    content: str

class MessageManager:
    
    def __init__(self) -> None:
        pass

    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(MessageManager, cls).__new__(cls)
        return cls.instance

    async def post(data):
        pass

    
    # def new_messgae(self, fname, type, ):
    #     message = Message(
    #         type="get", # 상대 기준 받음
    #         timestamp=time.time(),  # 2023년 11월 01일 00시 00분 (UTC)
    #         from_user={"userID": 123, "username": f"{name}"},
    #         to_user={"userID": 456, "username": f"{name}"},
    #         content="Hello, Bob!"
    #     )
    #     return message

    def read_history(self, id: list[int]):
        id = sorted(id)
        filename = '-'.join(map(str, id))+".json"
        data = FileIO.read_json(filename)
        return data


    def new_chat(self, id: list[int]):
        self.read_history(id)
        # 채팅 인스턴스 생성

    def cls_chat():
        ...