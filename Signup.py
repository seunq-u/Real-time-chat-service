class Signup():
    def __init__(self) -> None:
        pass

    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(Signup, cls).__new__(cls)
        return cls.instance

    def new_id(self, ):
        ...