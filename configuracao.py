import PySimpleGUI as sg
from log import error_log
from classes import Object_execute
from functions import *


class Dominio():
    def __init__(self):
        self.descricao = "Domínio:"
        self.definicao = 'dominio'
        self.valor = ""


class Usuario():
    def __init__(self):
        self.descricao = "Usuario:"
        self.definicao = 'usuario'
        self.valor = ""


class Senha():
    def __init__(self):
        self.descricao = "Senha:"
        self.definicao = 'senha'
        self.valor = ""


class Adicionaraodominio(Object_execute):
    def __init__(self):
        self.dominio = Dominio()
        self.usuario = Usuario()
        self.senha = Senha()
        self.descricao = "Adicionar ao domínio"
        self.definicao = "addtodomain"

    def thread_configurar(self):
        reportar("Adicionando ao domínio")
        addtodomain(self.dominio.valor, self.usuario.valor, self.senha.valor)

    def change_gui(self, window, values):
        self.dominio.valor = values[self.dominio.definicao]
        self.usuario.valor = values[self.usuario.definicao]
        self.senha.valor = values[self.usuario.definicao]
        estado = values[self.definicao]
        window[self.dominio.definicao].update(
            disabled=not estado)
        window[self.usuario.definicao].update(
            disabled=not estado)
        window[self.senha.definicao].update(
            disabled=not estado)

    def gui(self):
        dominio = [
            [sg.Checkbox(self.descricao,
                         key=self.definicao, size=(24, 1), enable_events=True)],
            [sg.Text(self.dominio.descricao, justification='left', size=(9, 1)), sg.Input(
                '', key=self.dominio.definicao, background_color='white', border_width=1, justification='left', size=(15, 1), disabled=True)],
            [sg.Text(self.usuario.descricao, justification='left', size=(9, 1)), sg.Input(
                '', key=self.usuario.definicao, background_color='white', border_width=1, justification='left', size=(15, 1), disabled=True)],
            [sg.Text(self.senha.descricao, justification='left', size=(9, 1)), sg.Input(
                '', key=self.senha.definicao, password_char='*', background_color='white', border_width=1, justification='left', size=(15, 1), disabled=True)],
        ]
        return [sg.Frame('Domínio:', dominio, font='Any 12', title_color='black')]


class Citrixcleanup(Object_execute):

    def __init__(self):
        self.descricao = "Limpar registro do Citrix"
        self.definicao = "citrixcleanup"

    def thread_configurar(self):
        reportar("Removendo registro")
        executar("reg delete HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\MSLicensing /f")


class Limpezageral(Object_execute):

    def __init__(self):
        self.descricao = "Limpar diretório Arcom"
        self.definicao = "limpezageral"

    def thread_configurar(self):
        reportar("Removendo " + self.diretorio)
        if os.path.exists(self.diretorio):
            shutil.rmtree(self.diretorio)


class Reniciar(Object_execute):

    def __init__(self):
        self.descricao = "Reniciar cpu após execução"
        self.definicao = "reniciar"

    def thread_configurar(self):
        reportar("Reiniciando...")
        executar("shutdown /t 0 /r")


class OpenvpnStart(Object_execute):

    def __init__(self):
        self.descricao = "Ativar openvpn"
        self.definicao = "openvpnstart"

    def thread_configurar(self):
        reportar("Iniciando Openvpn")
        executar("sc config openvpnservice start=auto")
        executar("net start openvpnservice")


class OpenvpnStop(Object_execute):

    def __init__(self):
        self.descricao = "Desativar openvpn"
        self.definicao = "openvpnstop"

    def thread_configurar(self):
        reportar("Parando Openvpn")
        executar("sc config openvpnservice start=demand")
        executar("net stop openvpnservice")
