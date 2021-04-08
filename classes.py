import threading


class Thread_execute():

    def thread_configurar(self):
        pass

    def configurar(self):
        processo = threading.Thread(target=self.thread_configurar, args=())
        processo.start()