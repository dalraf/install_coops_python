from vars import *
from functions import *

class Caixainstall():
    
    def __init__(self,diretorio):
        self.descricao = "Instalação do caixa"
        self.definicao = "caixainstall"
        self.diretorio = diretorio
    
    def configurar(self):
        createdirarcom(self.diretorio)
        print("Baixando o Caixa")
        if not os.path.isfile(self.diretorio + "\\Setup.jar"):
            file_id = '1M5SFb5f6z459xNLw7COboxXpH-PrBmqq'
            destination = self.diretorio + '\\Setup.jar'
            download_file_from_google_drive(file_id, destination)
            print("Download finalizado")
        print("Executando instalacao")
        subprocess.call('java -jar ' + self.diretorio + "\\Setup.jar", shell=True)
        subprocess.call('move ' + userdesktop + ' Caixa.lnk ' + allusersdesktop, shell=True)

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
        subprocess.call(self.diretorio + "\\sisbr2.0.exe", shell=True)
        subprocess.call('move ' + userdesktop + ' Sisbr 2.0.lnk ' + allusersdesktop, shell=True)


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
        subprocess.call('msiexec /i "' + diretoriocitrix + '\\Citrix10\\Versao 10.1\\PN_10_1.msi"', shell=True)


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
        subprocess.call(self.diretorio + "\\instalador-sicoobnet-windows-amd64.exe", shell=True)


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
        createdirarcom(self.diretorio)
        print("Baixando Adobe Air")
        if not os.path.isfile(self.diretorio + "\\adobeair.exe"):
            file_id = '13fUuPTnwpzIoydnefw9bcdX2h5KbJb0N'
            destination = self.diretorio + '\\adobeair.exe'
            download_file_from_google_drive(file_id, destination)
            print("Download finalizado")
        print("Executando instalacao")
        subprocess.call(self.diretorio + "\\adobeair", shell=True)
 
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