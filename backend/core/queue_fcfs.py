from collections import deque
from .patient import Patient

class FCFS_Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, patient: Patient):
        """Đưa bệnh nhân vào cuối hàng đợi [cite: 3]"""
        self.queue.append(patient)

    def dequeue(self) -> Patient:
        """Lấy bệnh nhân ở đầu hàng ra xử lý [cite: 3]"""
        if self.is_empty():
            return None
        return self.queue.popleft()

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def get_all_patients(self):
        return [p.to_dict() for p in self.queue]
