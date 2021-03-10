from vars import *
from functions import *


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


class Diretorioarcom():

    def __init__(self,diretorio):
        self.descricao = "Diretório Arcom"
        self.definicao = "diretorioarcom"
        self.diretorio = diretorio


class Allprograms():

    def __init__(self,diretorio):
        self.descricao = "Instalação programas padrão"
        self.definicao = "allprograms"
        self.diretorio = diretorio
        self.lista  = [Spark(self.diretorio), Adobeair(self.diretorio), Java(self.diretorio), Teamviewer(self.diretorio), Anydesk(self.diretorio), Googlechrome(self.diretorio), Firefox(self.diretorio)]
    
    def configurar(self):
        for program in self.lista:
            program.configurar()


class Spark():
    
    def __init__(self,diretorio):
        self.descricao = "Instalação do Spark"
        self.definicao = "spark"
        self.diretorio = diretorio

    def configurar(self):
        installprograma(self.diretorio,self.definicao)
        appdata = os.getenv('APPDATA')
        if not os.path.exists(appdata + '\\Spark'):
            os.mkdir(appdata + '\\Spark')
        filesparkconf = appdata + '\\Spark\\spark.properties'
        with open(filesparkconf, "w") as sparkconf:
            sparkconf.write(filestringspark)
        sparkconf.close()

class Adobeair():

    def __init__(self,diretorio):
        self.descricao = "Intalação do Adobe Air"
        self.definicao = "adobeair"
        self.diretorio = diretorio
    
    def configurar(self):
        installprograma(self.diretorio,self.definicao)

class Java():

    def __init__(self,diretorio):
        self.descricao = "Instalação do Java"
        self.definicao = "javaruntime"
        self.diretorio = diretorio
    
    def configurar(self):
        installprograma(self.diretorio,'javaruntime --x86SteamSteam')

class Teamviewer():

    def __init__(self,diretorio):
        self.descricao = "Intalação do Teamviewer"
        self.definicao = "teamviewer"
        self.diretorio = diretorio
    
    def configurar(self):
        installprograma(self.diretorio,self.definicao)


class Anydesk():

    def __init__(self,diretorio):
        self.descricao = "Intalação do Anydesk"
        self.definicao = "anydesk.install"
        self.diretorio = diretorio

    def configurar(self):
        installprograma(self.diretorio,self.definicao)


class Googlechrome():

    def __init__(self,diretorio):
        self.descricao = "Intalação do Google Chrome"
        self.definicao = "googlechrome"
        self.diretorio = diretorio
    
    def configurar(self):
        installprograma(self.diretorio,self.definicao)

class Firefox():

    def __init__(self,diretorio):
        self.descricao = "Intalação do Firefox"
        self.definicao = "firefox"
        self.diretorio = diretorio
    
    def configurar(self):
        installprograma(self.diretorio,self.definicao)