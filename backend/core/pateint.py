import uuid
import time

class Patient:
    def __init__(self, duration: int):
        self.id = str(uuid.uuid4())[:8] # Định nghĩa ID rút gọn [cite: 2]
        self.arrival_time = int(time.time()) # Đồng bộ mốc thời gian thực theo giây hệ thống [cite: 5]
        self.duration = duration # Thời gian khám [cite: 2]
        self.start_time = None # Thời gian bắt đầu khám [cite: 2]
        self.end_time = None # Thời gian kết thúc khám [cite: 2]

    def to_dict(self):
        return {
            "id": self.id,
            "arrival_time": self.arrival_time,
            "duration": self.duration,
            "start_time": self.start_time,
            "end_time": self.end_time
        }
