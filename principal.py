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
        self.diretorioarcom = Diretorioarcom(diretorio)
        self.descricao = "Instalação programas padrão"
        self.definicao = "allprograms"
        self.diretorio = diretorio
        self.obj_spark = Spark(self.diretorioarcom.diretorio)
        self.obj_adobeair = Adobeair(self.diretorioarcom.diretorio)
        self.obj_java = Java(self.diretorioarcom.diretorio)
        self.obj_caixa = Caixainstall(self.diretorioarcom.diretorio)
        self.obj_teamviewer = Teamviewer(self.diretorioarcom.diretorio)
        self.obj_anydesk = Anydesk(self.diretorioarcom.diretorio)
        self.obj_googlechrome = Googlechrome(self.diretorioarcom.diretorio)
        self.obj_firefox = Firefox(self.diretorioarcom.diretorio)
        self.obj_sisbrinstall = Sisbrinstall(self.diretorioarcom.diretorio)
        self.obj_citrix10install = Citrixinstall(self.diretorioarcom.diretorio)
        self.obj_sicoobnetinstall = Sicoobnetinstall(
            self.diretorioarcom.diretorio)

    def lista(self):
        lista = []
        for programa in dir(self):
            if programa.startswith('obj_'):
                lista.append(getattr(self, programa))
        return lista

    def configurar(self):
        for program in self.lista():
            program.configurar()


class Configuracoes():

    def __init__(self, diretorio):
        self.diretorioarcom = Diretorioarcom(diretorio)
        self.obj_citrixcleanup = Citrixcleanup(self.diretorioarcom.diretorio)
        self.adicionaraodominio = Adicionaraodominio(
            self.diretorioarcom.diretorio)
        self.obj_openvpnstart = OpenvpnStart(self.diretorioarcom.diretorio)
        self.obj_openvpnstop = OpenvpnStop(self.diretorioarcom.diretorio)
        self.obj_limpezageral = Limpezageral(self.diretorioarcom.diretorio)
        self.obj_reniciar = Reniciar(self.diretorioarcom.diretorio)

    def lista(self):
        lista = []
        for configuracao in dir(self):
            if configuracao.startswith('obj_'):
                lista.append(getattr(self, configuracao))
        return lista

    def configurar(self):
        for configuracao in self.lista():
            configuracao.configurar()


class Principal():

    def __init__(self, diretorio):
        self.diretorioarcom = Diretorioarcom(diretorio)
        self.programas = Programas(self.diretorioarcom.diretorio)
        self.configuracoes = Configuracoes(self.diretorioarcom.diretorio)
