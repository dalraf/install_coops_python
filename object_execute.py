import PySimpleGUI as sg
import threading
from functions import Functions

class Object_execute(Functions):

    def __init__(self):
        super().__init__()
        self.init_thread = False
        self.message_log = ""
        self.define_param()
        self.verify_thread_descricao = "Verify_Thread"

    def reportar(self,msg):
        self.logger.debug(self.definicao + " : " + msg)
        self.message_log = msg
        self.window.write_event_value(self.verify_thread_descricao,self.verify_thread_descricao)

    def define_param(self):
        self.definicao = ""
        self.descricao = ""

    def thread_configurar(self):
        pass
    
    def verify_thread(self, window, values):
        self.window = window
        self.values = values
        if self.init_thread == True and self.processo.is_alive():
            self.window[self.definicao + "status"].update(value=self.message_log)
        
        elif self.init_thread == True and not self.processo.is_alive():
            self.init_thread = False
            self.window[self.definicao + "status"].update(value="")

        else:
            self.window[self.definicao + "status"].update(value="")

    def change_gui(self, window, values):
        self.window = window
        self.values = values

    def configurar(self, window, values):
        self.window = window
        self.values = values
        self.diretorio = self.diretorioarcom
        self.change_gui(window, values)
        self.processo = threading.Thread(target=self.thread_configurar, args=())
        self.processo.start()
        self.init_thread = True

    def gui(self):
        return [sg.Checkbox(self.descricao, key=self.definicao, size=(24, 1)), sg.Input("",key=self.definicao + "status", background_color="White", justification='left', disabled=True, size=(30, 1)),]
        
