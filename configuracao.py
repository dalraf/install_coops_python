from vars import *
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


class Adicionaraodominio(Thread_execute):
    def __init__(self, diretorio):
        self.dominio = Dominio()
        self.usuario = Usuario()
        self.senha = Senha()
        self.descricao = "Adicionar ao domínio"
        self.definicao = "addtodomain"

    def thread_configurar(self, dominio, usuario, senha):
        self.dominio.valor = dominio
        self.usuario.valor = usuario
        self.senha.valor = senha
        reportar("Adicionando ao domínio")
        addtodomain(self.dominio.valor, self.usuario.valor, self.senha.valor)


class Citrixcleanup(Thread_execute):

    def __init__(self, diretorio):
        self.descricao = "Limpar registro do Citrix"
        self.definicao = "citrixcleanup"

    def thread_configurar(self):
        reportar("Removendo registro")
        executar("reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\MSLicensing /f")


class Limpezageral(Thread_execute):

    def __init__(self, diretorio):
        self.descricao = "Limpar diretório Arcom"
        self.definicao = "limpezageral"
        self.diretorio = diretorio

    def thread_configurar(self):
        if os.path.exists(self.diretorio):
            shutil.rmtree(self.diretorio)


class Reniciar(Thread_execute):

    def __init__(self, diretorio):
        self.descricao = "Reniciar cpu após execução"
        self.definicao = "reniciar"
        self.diretorio = diretorio

    def thread_configurar(self):
        executar("shutdown /t 0 /r")


class OpenvpnStart(Thread_execute):

    def __init__(self, diretorio):
        self.descricao = "Ativar openvpn"
        self.definicao = "openvpnstart"
        self.diretorio = diretorio

    def thread_configurar(self):
        executar("sc config openvpnservice start=auto")
        executar("net start openvpnservice")


class OpenvpnStop(Thread_execute):

    def __init__(self, diretorio):
        self.descricao = "Desativar openvpn"
        self.definicao = "openvpnstop"
        self.diretorio = diretorio

    def thread_configurar(self):
        executar("sc config openvpnservice start=demand")
        executar("net stop openvpnservice")
