import PySimpleGUI as sg
import threading

class Object_execute():

    def __init__(self):
        self.definicao = ""
        self.descricao = ""

    def thread_configurar(self):
        pass

    def change_gui(self,window,values):
        pass

    def configurar(self, window, values):
        self.change_gui(window, values)
        processo = threading.Thread(target=self.thread_configurar, args=())
        processo.start()

    def gui(self):
        return [sg.Checkbox(self.descricao, key=self.definicao, size=(24, 1))]