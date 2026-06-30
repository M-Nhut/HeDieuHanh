import random
import asyncio
from .patient import Patient
from .queue_fcfs.py import FCFS_Queue 
class AutoGenerator:
    def __init__(self, queue: FCFS_Queue):
        self.queue = queue
        self.is_running = False

    async def start_generation(self, broadcast_callback):
        self.is_running = True
        while self.is_running:
            e: 4]
            await asyncio.sleep(random.randint(2, 5))
            if not self.is_running:
                break
            
            random_duration = random.randint(5, 15) 
            new_patient = Patient(duration=random_duration)
            self.queue.enqueue(new_patient)
            
          
            await broadcast_callback()

    def stop(self):
        self.is_running = False
