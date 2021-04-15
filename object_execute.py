import PySimpleGUI as sg
import threading
from functions import Functions

class Object_execute(Functions):

    def __init__(self):
        super(Object_execute).__init__()
        self.init_thread = False
        self.status_icon = ["-","\\","|","/",]
        self.index_icon = 0
        self.define_param()

    def status_running(self):
        self.index_icon += 1
        if self.index_icon > (len(self.status_icon) - 1):
            self.index_icon = 0
        return self.status_icon[self.index_icon]

    def define_param(self):
        self.definicao = ""
        self.descricao = ""

    def thread_configurar(self):
        pass
    
    def verify_thread(self, window, values):
        if self.init_thread == True and self.processo.is_alive():
            window[self.definicao + "status"].update(value=self.status_running())
        
        elif self.init_thread == True and not self.processo.is_alive():
            self.init_thread = False
            window[self.definicao + "status"].update(value="")

        else:
            window[self.definicao + "status"].update(value="")

    def change_gui(self, window, values):
        pass

    def configurar(self, window, values):
        self.diretorio = self.diretorioarcom
        self.change_gui(window, values)
        self.processo = threading.Thread(target=self.thread_configurar, args=())
        self.processo.start()
        self.init_thread = True

    def gui(self):
        return [sg.Checkbox(self.descricao, key=self.definicao, size=(24, 1)), sg.Text("",key=self.definicao + "status", justification='left', size=(2, 1)),]
        
