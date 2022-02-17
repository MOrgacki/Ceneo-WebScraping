import uuid
from datetime import date

class Helpers:
    def __init__(self) -> None:
        pass

    
    def return_uuid(self) -> uuid.UUID:
        return uuid.uuid4()

    def return_time(self) -> date:
        return date.today().strftime("%d %B %Y")