import uuid
import babel.dates
import datetime

class Helpers:
    def __init__(self) -> None:
        pass

    
    def return_uuid(self) -> uuid.UUID:
        return uuid.uuid4()

    def return_time(self) -> babel.dates:
        now = datetime.datetime.now()
        return babel.dates.format_date(now, 'd MMMM yyyy', locale='pl_PL')