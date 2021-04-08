
class Error_log():
    
    def __init__(self):
        self.log = []
        self.stop_thread = False
    
    def addlog(self,msg):
        self.log.append(msg)


error_log = Error_log()