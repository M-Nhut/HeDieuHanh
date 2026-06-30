import uuid
import time

class Patient:
    def __init__(self, duration: int):
        self.id = str(uuid.uuid4())[:8] 
        self.arrival_time = int(time.time()) 
        self.duration = duration 
        self.start_time = None 
        self.end_time = None 

    def to_dict(self):
        return {
            "id": self.id,
            "arrival_time": self.arrival_time,
            "duration": self.duration,
            "start_time": self.start_time,
            "end_time": self.end_time
        }
