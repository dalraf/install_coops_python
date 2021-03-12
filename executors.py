from instalacao import *
from configuracao import *



class Executor():
    
    def __init__(self,diretorio):
        self.diretorioarcom = Diretorioarcom(diretorio)
        self.spark = Spark(self.diretorioarcom.diretorio)
        self.adobeair = Adobeair(self.diretorioarcom.diretorio)
        self.java = Java(self.diretorioarcom.diretorio)
        self.teamviewer = Teamviewer(self.diretorioarcom.diretorio)
        self.anydesk = Anydesk(self.diretorioarcom.diretorio)
        self.googlechrome = Googlechrome(self.diretorioarcom.diretorio)
        self.firefox = Firefox(self.diretorioarcom.diretorio)
        self.allprograms = Allprograms(self.diretorioarcom.diretorio)
        self.sisbrinstall = Sisbrinstall(self.diretorioarcom.diretorio)
        self.citrix10install = Citrixinstall(self.diretorioarcom.diretorio)
        self.allcconfiguracao = Allconfiguration(self.diretorioarcom.diretorio)
        self.citrixcleanup = Citrixcleanup(self.diretorioarcom.diretorio)
        self.limpezageral = Limpezageral(self.diretorioarcom.diretorio)
        self.reniciar = Reniciar(self.diretorioarcom.diretorio)
        self.adicionaraodominio = Adicionaraodominio(self.diretorioarcom.diretorio)

class Diretorioarcom():

    def __init__(self,diretorio):
        self.descricao = "Diretório Arcom"
        self.definicao = "diretorioarcom"
        self.diretorio = diretorio
