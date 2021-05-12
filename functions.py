import subprocess
import requests
import os
import logging
from config import Config


class Functions(Config):
    def __init__(self):
        super().__init__()
        logging.basicConfig(
            filename=self.diretorioarcom + "\\INSTALL_COOPS.log",
            filemode="a",
            format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
            datefmt="%H:%M:%S",
            level=logging.DEBUG,
        )
        self.logger = logging

    # Super classe para funcao de report
    def reportar(self, msg):
        self.logger.debug(msg)

    # Execucao de aplicativos e scripts
    def executar(self, command):
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        process = subprocess.Popen(
            command,
            cwd=self.diretorioarcom,
            startupinfo=startupinfo,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.DEVNULL,
            shell=True,
        )
        result, error = process.communicate()
        exitCode = process.wait()
        errortext = error.decode("cp1252")
        if exitCode > 0:
            if str(error) == "":
                error = result
            self.reportar("Code: " + str(exitCode) + " - Message: " + errortext)
        else:
            self.reportar("Finalizado sem problema")

    # Adicionar no domínio
    def addtodomain(self, dominio, usuario, senha):
        self.executar(
            f'@"%SystemRoot%\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "$domain = "{dominio}"; $password = "{senha}" | ConvertTo-SecureString -asPlainText -Force; $username = \'{usuario}@$domain\';$credential = New-Object System.Management.Automation.PSCredential($username,$password);Add-Computer -DomainName $domain -Credential $credential"'
        )

    # Executa instalacao de programas
    def installprograma(self, diretorioarcom, programa):
        if not os.path.isfile(self.chocolateypath):
            self.reportar("Executando instalação do chocolatey")
            self.executar(
                '@"%SystemRoot%\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString(\'https://chocolatey.org/install.ps1\'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\\chocolatey\\bin"'
            )
        self.executar(
            self.chocolateypath + " config set cacheLocation " + diretorioarcom
        )
        self.reportar("Executando instalação, " + programa)
        self.executar(self.chocolateypath + " install -y " + programa)

    # Baixa arquivos do google drive
    def download_file_from_google_drive(self, id, destination):
        def get_confirm_token(response):
            for key, value in response.cookies.items():
                if key.startswith("download_warning"):
                    return value
            return None

        def save_response_content(response, destination):
            CHUNK_SIZE = 32768

            with open(destination, "wb") as f:
                for chunk in response.iter_content(CHUNK_SIZE):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)

        URL = "https://docs.google.com/uc?export=download"

        session = requests.Session()

        response = session.get(URL, params={"id": id}, stream=True)
        token = get_confirm_token(response)

        if token:
            params = {"id": id, "confirm": token}
            response = session.get(URL, params=params, stream=True)

        save_response_content(response, destination)
