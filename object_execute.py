import PySimpleGUI as sg
import threading
from functions import Functions


class Object_execute(Functions):
    def __init__(self):
        super().__init__()
        self.window = None
        self.values = None
        self.define_param()
        self.processo = False
        self.message_log = ""
        self.verify_thread_descricao = self.definicao + "-Verify_Thread"

    def reportar(self, msg):
        if msg != "" or msg is not None:
            self.logger.debug(self.definicao + " : " + msg)
            self.message_log = msg
            if self.processo:
                self.window.write_event_value(
                    self.verify_thread_descricao, self.definicao
                )

    def define_param(self):
        self.definicao = ""
        self.descricao = ""

    def thread_configurar(self):
        pass

    def verify_thread(self, window, values):
        self.window = window
        self.values = values

        if self.processo:
            self.window[self.definicao + "status"].update(value=self.message_log)

    def change_gui(self, window, values):
        pass

    def configurar(self, window, values):
        self.window = window
        self.values = values
        self.processo = threading.Thread(target=self.thread_configurar, args=())
        self.processo.start()
        self.processo.join()

    def gui(self):
        return [
            sg.Checkbox(self.descricao, key=self.definicao, size=(24, 1)),
            sg.Input(
                "",
                key=self.definicao + "status",
                background_color="White",
                border_width=1,
                justification="left",
                disabled=True,
                size=(20, 1),
            ),
        ]
