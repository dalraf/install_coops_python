import os
import zipfile
import requests
from object_execute import Object_execute

class Caixainstall(Object_execute):

    def define_param(self):
        self.descricao = "Instalação do Caixa"
        self.definicao = "caixainstall"

    def thread_configurar(self):
        self.createdirarcom(self.diretorio)
        self.reportar("Baixando o Caixa")
        if not os.path.isfile(self.diretorio + "\\Setup.jar"):
            file_id = '1M5SFb5f6z459xNLw7COboxXpH-PrBmqq'
            destination = self.diretorio + '\\Setup.jar'
            self.download_file_from_google_drive(file_id, destination)
            self.reportar("Download finalizado")
        self.reportar("Executando instalação")
        self.executar('java -jar ' + self.diretorio + "\\Setup.jar")
        self.executar('move ' + self.userdesktop + ' Caixa.lnk ' + self.allusersdesktop)


class Sisbrinstall(Object_execute):

    def define_param(self):
        self.descricao = "Instalação do Sisbr 2.0"
        self.definicao = "sisbr20install"

    def thread_configurar(self):
        self.createdirarcom(self.diretorio)
        self.reportar("Baixando sisbr 2.0")
        if not os.path.isfile(self.diretorio + "\\sisbr2.0.exe"):
            file_id = '13E-X5fZZrj2FMZDIcLWJ94c9DgTqUA3f'
            destination = self.diretorio + '\\sisbr2.0.exe'
            self.download_file_from_google_drive(file_id, destination)
            self.reportar("Download finalizado")
        self.reportar("Executando instalação")
        self.executar(self.diretorio + "\\sisbr2.0.exe")
        self.executar('move ' + self.userdesktop + ' Sisbr 2.0.lnk ' + self.allusersdesktop)


class Citrixinstall(Object_execute):

    def define_param(self):
        self.descricao = "Instalação do Citrix 10"
        self.definicao = "citrix10"

    def thread_configurar(self):
        self.createdirarcom(self.diretorio)
        self.diretoriocitrix = self.diretorio + "\\Citrix"
        self.criardiretorio(self.diretoriocitrix)
        self.reportar("Baixando citrix 10")
        if not os.path.isfile(self.diretorio + "\\Citrix10.zip"):
            file_id = '19o1eGqGL6xR1B9b3VYunea4zzYe3Heb9'
            destination = self.diretorio + '\\Citrix10.zip'
            self.download_file_from_google_drive(file_id, destination)
            self.reportar("Download finalizado")
        self.reportar("Executando descompactação")
        with zipfile.ZipFile(self.diretorio + '\\Citrix10.zip', 'r') as citrixzip:
            citrixzip.extractall(self.diretoriocitrix)
        self.reportar("Executando instalação")
        self.executar('msiexec /i "' + self.diretoriocitrix +
                 '\\Citrix10\\Versao 10.1\\PN_10_1.msi"')


class Sicoobnetinstall(Object_execute):

    def define_param(self):
        self.descricao = "Instalação do SicoobNet"
        self.definicao = "sicoobnet"

    def thread_configurar(self):
        self.createdirarcom(self.diretorio)
        if not os.path.isfile(self.diretorio + "\\instalador-sicoobnet-windows-amd64.exe"):
            self.reportar("Baixando Sicoobnet Empresarial")
            urlsicoobnet = "https://office-sicoob-instalador.s3-us-west-2.amazonaws.com/instalador-sicoobnet-windows-amd64.exe"
            download = requests.get(urlsicoobnet, allow_redirects=True)
            open(self.diretorio + "\\instalador-sicoobnet-windows-amd64.exe",
                 'wb').write(download.content)
        self.reportar("Executando instalação")
        self.executar(self.diretorio + "\\instalador-sicoobnet-windows-amd64.exe")


class Spark(Object_execute):

    def define_param(self):
        self.descricao = "Instalação do Spark"
        self.definicao = "spark"

    def thread_configurar(self):
        self.installprograma(self.diretorio, self.definicao)
        appdata = os.getenv('APPDATA')
        if not os.path.exists(appdata + '\\Spark'):
            os.mkdir(appdata + '\\Spark')
        filesparkconf = appdata + '\\Spark\\spark.properties'
        with open(filesparkconf, "w") as sparkconf:
            sparkconf.write(self.filestringspark)
        sparkconf.close()


class Adobeair(Object_execute):

    def define_param(self):
        self.descricao = "Instalação do Adobe Air"
        self.definicao = "adobeair"

    def thread_configurar(self):
        self.createdirarcom(self.diretorio)
        self.reportar("Baixando Adobe Air")
        if not os.path.isfile(self.diretorio + "\\adobeair.exe"):
            file_id = '13fUuPTnwpzIoydnefw9bcdX2h5KbJb0N'
            destination = self.diretorio + '\\adobeair.exe'
            self.download_file_from_google_drive(file_id, destination)
            self.reportar("Download finalizado")
        self.reportar("Executando instalação")
        self.executar(self.diretorio + "\\adobeair")


class Java(Object_execute):

    def define_param(self):
        self.descricao = "Instalação do Java"
        self.definicao = "javaruntime"

    def thread_configurar(self):
        self.installprograma(self.diretorio, 'javaruntime --x86SteamSteam')


class Teamviewer(Object_execute):

    def define_param(self):
        self.descricao = "Instalação do Teamviewer"
        self.definicao = "teamviewer"

    def thread_configurar(self):
        self.installprograma(self.diretorio, self.definicao)


class Anydesk(Object_execute):

    def define_param(self):
        self.descricao = "Instalação do Anydesk"
        self.definicao = "anydesk.install"

    def thread_configurar(self):
        self.installprograma(self.diretorio, self.definicao)


class Googlechrome(Object_execute):

    def define_param(self):
        self.descricao = "Instalação do Google Chrome"
        self.definicao = "googlechrome"

    def thread_configurar(self):
        self.installprograma(self.diretorio, self.definicao)


class Firefox(Object_execute):

    def define_param(self):
        self.descricao = "Instalação do Firefox"
        self.definicao = "firefox"

    def thread_configurar(self):
        self.installprograma(self.diretorio, self.definicao)
