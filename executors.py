import shutil
import zipfile
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



class Allconfiguration():

    def __init__(self,diretorio):
        self.diretorio = diretorio
        self.lista  = [Citrixcleanup(self.diretorio), \
                       Limpezageral(self.diretorio), \
                       Reniciar(self.diretorio),
                    ]
    
    def configurar(self):
        for configuracao in self.lista:
            configuracao.configurar()

class Dominio():
    def __init__(self):
        self.descricao = "Domínio:"
        self.definicao = 'dominio'
        self.valor = ""

class Usuario():
    def __init__(self):
        self.descricao = "Usuario: "
        self.definicao = 'usuario'
        self.valor = ""

class Senha():
    def __init__(self):
        self.descricao = "Senha: "
        self.definicao = 'senha'
        self.valor = ""

class Adicionaraodominio():
    def __init__(self,diretorio):
        self.dominio = Dominio()
        self.usuario = Usuario()
        self.senha = Senha()
        self.descricao = "Adicionar ao domínio"
        self.definicao = "addtodomain"
    
    def configurar(self):
        print("Adicionando ao domínio")
        addtodomain(self.dominio.valor,self.usuario.valor,self.senha.valor)


class Citrixcleanup():
    
    def __init__(self,diretorio):
        self.descricao = "Limpar registro do Citrix"
        self.definicao = "citrixcleanup"
    
    def configurar(self):
        print("Removendo registro")
        subprocess.call("reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\MSLicensing /f")

class Limpezageral():
    
    def __init__(self,diretorio):
        self.descricao = "Limpar diretório Arcom"
        self.definicao = "limpezageral"
        self.diretorio = diretorio
    
    def configurar(self):
        if os.path.exists(self.diretorio):
            shutil.rmtree(self.diretorio)

class Reniciar():
    
    def __init__(self,diretorio):
        self.descricao = "Reniciar cpu após execução"
        self.definicao = "reniciar"
        self.diretorio = diretorio
    
    def configurar(self):
        subprocess.call("shutdown /t0 /r")


class Allprograms():

    def __init__(self,diretorio):
        self.descricao = "Instalação programas padrão"
        self.definicao = "allprograms"
        self.diretorio = diretorio
        self.lista  = [Spark(self.diretorio), \
                    Adobeair(self.diretorio), \
                    Java(self.diretorio), \
                    Teamviewer(self.diretorio), \
                    Anydesk(self.diretorio), \
                    Googlechrome(self.diretorio), \
                    Firefox(self.diretorio), \
                    Sisbrinstall(self.diretorio),
                    Citrixinstall(self.diretorio),
                    Sicoobnetinstall(self.diretorio)               
                    ]
    
    def configurar(self):
        for program in self.lista:
            program.configurar()


class Sisbrinstall():
    
    def __init__(self,diretorio):
        self.descricao = "Instalação do Sisbr 2.0"
        self.definicao = "sisbr20install"
        self.diretorio = diretorio
    
    def configurar(self):
        createdirarcom(self.diretorio)
        print("Baixando sisbr 2.0")
        if not os.path.isfile(self.diretorio + "\\sisbr2.0.exe"):
            file_id = '13E-X5fZZrj2FMZDIcLWJ94c9DgTqUA3f'
            destination = self.diretorio + '\\sisbr2.0.exe'
            download_file_from_google_drive(file_id, destination)
            print("Download finalizado")
        print("Executando instalacao")
        subprocess.call(self.diretorio + "\\sisbr2.0.exe")


class Citrixinstall():
    
    def __init__(self,diretorio):
        self.descricao = "Instalação do Citrix 10"
        self.definicao = "citrix10"
        self.diretorio = diretorio
    
    def configurar(self):
        createdirarcom(self.diretorio)
        diretoriocitrix = self.diretorio + "\\Citrix"
        criardiretorio(diretoriocitrix)
        print("Baixando citrix 10")
        if not os.path.isfile(self.diretorio + "\\Citrix10.zip"):
            file_id = '19o1eGqGL6xR1B9b3VYunea4zzYe3Heb9'
            destination = self.diretorio + '\\Citrix10.zip'
            download_file_from_google_drive(file_id, destination)
            print("Download finalizado")
        print("Executando descompacação")
        with zipfile.ZipFile(self.diretorio + '\\Citrix10.zip', 'r') as citrixzip:
            citrixzip.extractall(diretoriocitrix)
        subprocess.call('msiexec /i "' + diretoriocitrix + '\\Citrix10\\Versao 10.1\\PN_10_1.msi"')


class Sicoobnetinstall():
    
    def __init__(self,diretorio):
        self.descricao = "Instalação do SicoobNet"
        self.definicao = "sicoobnet"
        self.diretorio = diretorio
    
    def configurar(self):
        createdirarcom(self.diretorio)
        if not os.path.isfile(self.diretorio + "\\instalador-sicoobnet-windows-amd64.exe"):
            print("Baixando Sicoobnet Empresarial")
            urlsicoobnet = "https://office-sicoob-instalador.s3-us-west-2.amazonaws.com/instalador-sicoobnet-windows-amd64.exe"
            download = requests.get(urlsicoobnet, allow_redirects=True)
            open(self.diretorio + "\\instalador-sicoobnet-windows-amd64.exe", 'wb').write(download.content)
        subprocess.call(self.diretorio + "\\instalador-sicoobnet-windows-amd64.exe")


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