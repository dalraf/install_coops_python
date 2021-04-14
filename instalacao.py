from log import error_log
from classes import Object_execute
from functions import *


class Caixainstall(Object_execute):

    def __init__(self, diretorio):
        self.descricao = "Instalação do Caixa"
        self.definicao = "caixainstall"
        self.diretorio = diretorio

    def thread_configurar(self):
        createdirarcom(self.diretorio)
        reportar("Baixando o Caixa")
        if not os.path.isfile(self.diretorio + "\\Setup.jar"):
            file_id = '1M5SFb5f6z459xNLw7COboxXpH-PrBmqq'
            destination = self.diretorio + '\\Setup.jar'
            download_file_from_google_drive(file_id, destination)
            reportar("Download finalizado")
        reportar("Executando instalação")
        executar('java -jar ' + self.diretorio + "\\Setup.jar")
        executar('move ' + userdesktop + ' Caixa.lnk ' + allusersdesktop)




class Sisbrinstall(Object_execute):

    def __init__(self, diretorio):
        self.descricao = "Instalação do Sisbr 2.0"
        self.definicao = "sisbr20install"
        self.diretorio = diretorio

    def thread_configurar(self):
        createdirarcom(self.diretorio)
        reportar("Baixando sisbr 2.0")
        if not os.path.isfile(self.diretorio + "\\sisbr2.0.exe"):
            file_id = '13E-X5fZZrj2FMZDIcLWJ94c9DgTqUA3f'
            destination = self.diretorio + '\\sisbr2.0.exe'
            download_file_from_google_drive(file_id, destination)
            reportar("Download finalizado")
        reportar("Executando instalação")
        executar(self.diretorio + "\\sisbr2.0.exe")
        executar('move ' + userdesktop + ' Sisbr 2.0.lnk ' + allusersdesktop)


class Citrixinstall(Object_execute):

    def __init__(self, diretorio):
        self.descricao = "Instalação do Citrix 10"
        self.definicao = "citrix10"
        self.diretorio = diretorio

    def thread_configurar(self):
        createdirarcom(self.diretorio)
        diretoriocitrix = self.diretorio + "\\Citrix"
        criardiretorio(diretoriocitrix)
        reportar("Baixando citrix 10")
        if not os.path.isfile(self.diretorio + "\\Citrix10.zip"):
            file_id = '19o1eGqGL6xR1B9b3VYunea4zzYe3Heb9'
            destination = self.diretorio + '\\Citrix10.zip'
            download_file_from_google_drive(file_id, destination)
            reportar("Download finalizado")
        reportar("Executando descompactação")
        with zipfile.ZipFile(self.diretorio + '\\Citrix10.zip', 'r') as citrixzip:
            citrixzip.extractall(diretoriocitrix)
        reportar("Executando instalação")
        executar('msiexec /i "' + diretoriocitrix +
                 '\\Citrix10\\Versao 10.1\\PN_10_1.msi"')


class Sicoobnetinstall(Object_execute):

    def __init__(self, diretorio):
        self.descricao = "Instalação do SicoobNet"
        self.definicao = "sicoobnet"
        self.diretorio = diretorio

    def thread_configurar(self):
        createdirarcom(self.diretorio)
        if not os.path.isfile(self.diretorio + "\\instalador-sicoobnet-windows-amd64.exe"):
            reportar("Baixando Sicoobnet Empresarial")
            urlsicoobnet = "https://office-sicoob-instalador.s3-us-west-2.amazonaws.com/instalador-sicoobnet-windows-amd64.exe"
            download = requests.get(urlsicoobnet, allow_redirects=True)
            open(self.diretorio + "\\instalador-sicoobnet-windows-amd64.exe",
                'wb').write(download.content)
        reportar("Executando instalação")
        executar(self.diretorio + "\\instalador-sicoobnet-windows-amd64.exe")


class Spark(Object_execute):

    def __init__(self, diretorio):
        self.descricao = "Instalação do Spark"
        self.definicao = "spark"
        self.diretorio = diretorio

    def thread_configurar(self):
        installprograma(self.diretorio, self.definicao)
        appdata = os.getenv('APPDATA')
        if not os.path.exists(appdata + '\\Spark'):
            os.mkdir(appdata + '\\Spark')
        filesparkconf = appdata + '\\Spark\\spark.properties'
        with open(filesparkconf, "w") as sparkconf:
            sparkconf.write(filestringspark)
        sparkconf.close()


class Adobeair(Object_execute):

    def __init__(self, diretorio):
        self.descricao = "Instalação do Adobe Air"
        self.definicao = "adobeair"
        self.diretorio = diretorio

    def thread_configurar(self):
        createdirarcom(self.diretorio)
        reportar("Baixando Adobe Air")
        if not os.path.isfile(self.diretorio + "\\adobeair.exe"):
            file_id = '13fUuPTnwpzIoydnefw9bcdX2h5KbJb0N'
            destination = self.diretorio + '\\adobeair.exe'
            download_file_from_google_drive(file_id, destination)
            reportar("Download finalizado")
        reportar("Executando instalação")
        executar(self.diretorio + "\\adobeair")


class Java(Object_execute):

    def __init__(self, diretorio):
        self.descricao = "Instalação do Java"
        self.definicao = "javaruntime"
        self.diretorio = diretorio

    def thread_configurar(self):
        installprograma(self.diretorio, 'javaruntime --x86SteamSteam')


class Teamviewer(Object_execute):

    def __init__(self, diretorio):
        self.descricao = "Instalação do Teamviewer"
        self.definicao = "teamviewer"
        self.diretorio = diretorio

    def thread_configurar(self):
        installprograma(self.diretorio, self.definicao)


class Anydesk(Object_execute):

    def __init__(self, diretorio):
        self.descricao = "Instalação do Anydesk"
        self.definicao = "anydesk.install"
        self.diretorio = diretorio

    def thread_configurar(self):
        installprograma(self.diretorio, self.definicao)


class Googlechrome(Object_execute):

    def __init__(self, diretorio):
        self.descricao = "Instalação do Google Chrome"
        self.definicao = "googlechrome"
        self.diretorio = diretorio

    def thread_configurar(self):
        installprograma(self.diretorio, self.definicao)


class Firefox(Object_execute):

    def __init__(self, diretorio):
        self.descricao = "Instalação do Firefox"
        self.definicao = "firefox"
        self.diretorio = diretorio

    def thread_configurar(self):
        installprograma(self.diretorio, self.definicao)
