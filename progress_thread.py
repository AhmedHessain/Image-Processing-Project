import random
import time
from PyQt5.QtCore import QThread, pyqtSignal
import threading

class ProgressThread(QThread):
    progress_update = pyqtSignal(int)

    def __init__(self,worker_function):
        self.TaskDone = False
        self.worker_function = worker_function
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):       
        t1=threading.Thread(target=self.progressing,daemon=True)
        t1.start()
        self.worker_function()
        self.TaskDone = True
        self.progress_update.emit(100)

        
    
    def progressing(self):
        for i in range(95):
            if self.TaskDone:
                break
            self.progress_update.emit(i)
            x=random.randint(1,10)
            time.sleep(x*0.001)


