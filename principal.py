from log import error_log
from instalacao import *
from configuracao import *


class Diretorioarcom():

    def __init__(self, diretorio):
        self.descricao = "Diretório Arcom"
        self.definicao = "diretorioarcom"
        self.diretorio = diretorio


class Programas():

    def __init__(self, diretorio):
        self.lista = []
        self.diretorioarcom = Diretorioarcom(diretorio)
        self.diretorio = diretorio
        self.lista.append(Spark(self.diretorioarcom.diretorio))
        self.lista.append(Adobeair(self.diretorioarcom.diretorio))
        self.lista.append(Java(self.diretorioarcom.diretorio))
        self.lista.append(Caixainstall(self.diretorioarcom.diretorio))
        self.lista.append(Teamviewer(self.diretorioarcom.diretorio))
        self.lista.append(Anydesk(self.diretorioarcom.diretorio))
        self.lista.append(Googlechrome(self.diretorioarcom.diretorio))
        self.lista.append(Firefox(self.diretorioarcom.diretorio))
        self.lista.append(Sisbrinstall(self.diretorioarcom.diretorio))
        self.lista.append(Citrixinstall(self.diretorioarcom.diretorio))
        self.lista.append(Sicoobnetinstall(self.diretorioarcom.diretorio))


class Configuracoes():

    def __init__(self, diretorio):
        self.lista = []
        self.diretorioarcom = Diretorioarcom(diretorio)
        self.lista.append(Adicionaraodominio(self.diretorioarcom.diretorio))
        self.lista.append(Citrixcleanup(self.diretorioarcom.diretorio))
        self.lista.append(OpenvpnStart(self.diretorioarcom.diretorio))
        self.lista.append(OpenvpnStop(self.diretorioarcom.diretorio))
        self.lista.append(Limpezageral(self.diretorioarcom.diretorio))
        self.lista.append(Reniciar(self.diretorioarcom.diretorio))

    def configurar(self):
        for configuracao in self.lista:
            configuracao.configurar()


class Principal():

    def __init__(self, diretorio):
        self.diretorioarcom = Diretorioarcom(diretorio)
        self.programas = Programas(self.diretorioarcom.diretorio)
        self.configuracoes = Configuracoes(self.diretorioarcom.diretorio)
