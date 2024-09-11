# message manager
import websockets

class MessageManager:
    def __init__(self) -> None:
        pass

    def __new__(cls):
        if not hasattr(cls,'instance'):
            print('create')
            cls.instance = super(MessageManager, cls).__new__(cls)
        else:
            print('recycle')
        return cls.instance

    def post()