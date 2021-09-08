import os
import zipfile
import requests
from object_execute import Object_execute


class Caixainstall(Object_execute):
    def define_param(self):
        self.descricao = "Instalação do Caixa"
        self.definicao = "caixainstall"

    def thread_configurar(self):
        self.java = Java()
        self.java.window = self.window
        self.java.values = self.values
        self.java.reportar = self.reportar
        self.java.thread_configurar()
        self.reportar("Baixando o Caixa")
        if not os.path.isfile(self.diretorioarcom + "\\Setup.jar"):
            file_id = "1M5SFb5f6z459xNLw7COboxXpH-PrBmqq"
            destination = self.diretorioarcom + "\\Setup.jar"
            self.download_file_from_google_drive(file_id, destination)
            self.reportar("Download finalizado")
        self.reportar("Executando instalação do Caixa")
        self.executar("java -jar " + self.diretorioarcom + "\\Setup.jar")
        self.executar(
            "move " + self.userdesktop + "\\Caixa.lnk " + self.allusersdesktop
        )


class Sisbrinstall(Object_execute):
    def define_param(self):
        self.descricao = "Instalação do Sisbr 2.0"
        self.definicao = "sisbr20install"

    def thread_configurar(self):
        self.adobeair = Adobeair()
        self.adobeair.window = self.window
        self.adobeair.values = self.values
        self.adobeair.reportar = self.reportar
        self.adobeair.thread_configurar()
        self.reportar("Baixando sisbr 2.0")
        if not os.path.isfile(self.diretorioarcom + "\\sisbr2.0.exe"):
            file_id = "13E-X5fZZrj2FMZDIcLWJ94c9DgTqUA3f"
            destination = self.diretorioarcom + "\\sisbr2.0.exe"
            self.download_file_from_google_drive(file_id, destination)
            self.reportar("Download finalizado")
        self.reportar("Executando instalação do Sisbr2.0")
        self.executar(self.diretorioarcom + "\\sisbr2.0.exe")
        self.executar(
            "move " + self.userdesktop + '"\\Sisbr 2.0.lnk" ' + self.allusersdesktop
        )


class Citrixinstall(Object_execute):
    def define_param(self):
        self.descricao = "Instalação do Citrix 10"
        self.definicao = "citrix10"

    def thread_configurar(self):
        self.diretorioarcomcitrix = self.diretorioarcom + "\\Citrix"
        self.criardiretorio(self.diretorioarcomcitrix)
        self.reportar("Baixando citrix 10")
        if not os.path.isfile(self.diretorioarcom + "\\Citrix10.zip"):
            file_id = "19o1eGqGL6xR1B9b3VYunea4zzYe3Heb9"
            destination = self.diretorioarcom + "\\Citrix10.zip"
            self.download_file_from_google_drive(file_id, destination)
            self.reportar("Download finalizado")
        self.reportar("Executando descompactação")
        with zipfile.ZipFile(self.diretorioarcom + "\\Citrix10.zip", "r") as citrixzip:
            citrixzip.extractall(self.diretorioarcomcitrix)
        self.reportar("Executando instalação do Citrix10")
        self.executar(
            'msiexec /i "'
            + self.diretorioarcomcitrix
            + '\\Citrix10\\Versao 10.1\\PN_10_1.msi"'
        )


class Sicoobnetinstall(Object_execute):
    def define_param(self):
        self.descricao = "Instalação do SicoobNet"
        self.definicao = "sicoobnet"

    def thread_configurar(self):
        if not os.path.isfile(
            self.diretorioarcom + "\\instalador-sicoobnet-windows-amd64.exe"
        ):
            self.reportar("Baixando Sicoobnet Empresarial")
            urlsicoobnet = "https://office-sicoob-instalador.s3-us-west-2.amazonaws.com/instalador-sicoobnet-windows-amd64.exe"
            download = requests.get(urlsicoobnet, allow_redirects=True)
            open(
                self.diretorioarcom + "\\instalador-sicoobnet-windows-amd64.exe", "wb"
            ).write(download.content)
        self.reportar("Executando instalação do Sicoobnet")
        self.executar(self.diretorioarcom + "\\instalador-sicoobnet-windows-amd64.exe")


class Spark(Object_execute):
    def define_param(self):
        self.descricao = "Instalação do Spark"
        self.definicao = "spark"

    def thread_configurar(self):
        self.installprograma(self.diretorioarcom, self.definicao)
        appdata = os.getenv("APPDATA")
        if not os.path.exists(appdata + "\\Spark"):
            os.mkdir(appdata + "\\Spark")
        filesparkconf = appdata + "\\Spark\\spark.properties"
        with open(filesparkconf, "w") as sparkconf:
            sparkconf.write(self.filestringspark)
        sparkconf.close()


class Adobeair(Object_execute):
    def define_param(self):
        self.descricao = "Instalação do Adobe Air"
        self.definicao = "adobeair"

    def thread_configurar(self):
        self.reportar("Baixando Adobe Air")
        if not os.path.isfile(self.diretorioarcom + "\\adobeair.exe"):
            file_id = "13fUuPTnwpzIoydnefw9bcdX2h5KbJb0N"
            destination = self.diretorioarcom + "\\adobeair.exe"
            self.download_file_from_google_drive(file_id, destination)
            self.reportar("Download finalizado")
        self.reportar("Executando instalação do Adobeair")
        self.executar(self.diretorioarcom + "\\adobeair")


class Java(Object_execute):
    def define_param(self):
        self.descricao = "Instalação do Java"
        self.definicao = "javaruntime"

    def thread_configurar(self):
        self.installprograma(
            self.diretorioarcom, 'jre8 -PackageParameters "/exclude:64" -y'
        )


class Teamviewer(Object_execute):
    def define_param(self):
        self.descricao = "Instalação do Teamviewer"
        self.definicao = "teamviewer"

    def thread_configurar(self):
        self.installprograma(self.diretorioarcom, self.definicao)


class Anydesk(Object_execute):
    def define_param(self):
        self.descricao = "Instalação do Anydesk"
        self.definicao = "anydesk.install"

    def thread_configurar(self):
        self.installprograma(self.diretorioarcom, self.definicao)


class Googlechrome(Object_execute):
    def define_param(self):
        self.descricao = "Instalação do Google Chrome"
        self.definicao = "googlechrome"

    def thread_configurar(self):
        self.installprograma(self.diretorioarcom, self.definicao)


class Firefox(Object_execute):
    def define_param(self):
        self.descricao = "Instalação do Firefox"
        self.definicao = "firefox"

    def thread_configurar(self):
        self.installprograma(self.diretorioarcom, self.definicao)


class Adobereader(Object_execute):
    def define_param(self):
        self.descricao = "Instalação do Adobe Reader"
        self.definicao = "adobereader"

    def thread_configurar(self):
        self.installprograma(self.diretorioarcom, self.definicao)