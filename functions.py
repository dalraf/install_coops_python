
import subprocess
import requests
import os
import shutil
import zipfile
import time
import threading
from loguru import logger
from log import error_log
from vars import *


logger.add("INSTALL_COOPS.log")


class Thread_execute():

    def thread_configurar(self):
        pass

    def configurar(self):
        processo = threading.Thread(target=self.thread_configurar, args=())
        processo.start()


def reportar(msg):
    logger.debug(msg)
    error_log.addlog(msg)


def executar(command):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    process = subprocess.Popen(command, startupinfo=startupinfo, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, stdin=subprocess.DEVNULL, shell=True)
    result, error = process.communicate()
    exitCode = process.wait()
    errortext = error.decode("cp1252")
    if exitCode > 0:
        if(str(error) == ""):
            error = result
        reportar("Code: " + str(exitCode) + " - Message: " + errortext)
    reportar(errortext)



# Função para adicionar no domínio
def addtodomain(dominio, usuario, senha):
    executar(
        f'@"%SystemRoot%\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command \"$domain = "{dominio}"; $password = "{senha}" | ConvertTo-SecureString -asPlainText -Force; $username = \'{usuario}@$domain\';$credential = New-Object System.Management.Automation.PSCredential($username,$password);Add-Computer -DomainName $domain -Credential $credential\"')


# Executa instalacao de programas
def installprograma(diretorioarcom, programa):
    if not os.path.isfile(chocolateypath):
        reportar("Executando chocolatey")
        executar(
            '@"%SystemRoot%\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString(\'https://chocolatey.org/install.ps1\'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"')
    executar(chocolateypath + " config set cacheLocation " + diretorioarcom)
    executar(chocolateypath + " install -y " + programa)


def criardiretorio(diretorio):
    if not os.path.exists(diretorio):
        os.mkdir(diretorio)

# Cria Diretorio Arcom


def createdirarcom(diretorioarcom):
    criardiretorio(diretorioarcom)

# Baixa arquivos do google drives


def download_file_from_google_drive(id, destination):

    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
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

    response = session.get(URL, params={'id': id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)
