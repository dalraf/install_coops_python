
import subprocess
import requests
import os
import shutil
import zipfile
from vars import *

#Alterar campos do domínio
def mudarestadocamposdominio(window,estado):
    window['dominio'].update(disabled = not estado)
    window['usuario'].update(disabled = not estado)
    window['senha'].update(disabled = not estado)

#Função para adicionar no domínio
def addtodomain(dominio,usuario,senha):
    subprocess.call(f'@"%SystemRoot%\System32\WindowsPowerShell\\v1.0\\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command \"$domain = "{dominio}"; $password = "{senha}" | ConvertTo-SecureString -asPlainText -Force; $username = \'{usuario}@$domain\';$credential = New-Object System.Management.Automation.PSCredential($username,$password);Add-Computer -DomainName $domain -Credential $credential\"', shell=True)
 

#Executa instalacao de programas
def installprograma(diretorioarcom, programa):
    if not os.path.isfile(chocolateypath):
        print("Executando chocolatey")
        subprocess.call('@"%SystemRoot%\System32\WindowsPowerShell\\v1.0\\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString(\'https://chocolatey.org/install.ps1\'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"', shell=True)
    subprocess.call(chocolateypath + " config set cacheLocation " + diretorioarcom, shell=True)
    subprocess.call(chocolateypath + " install -y " + programa, shell=True)

def criardiretorio(diretorio):
    if not os.path.exists(diretorio):
        os.mkdir(diretorio)    

#Cria Diretorio Arcom
def createdirarcom(diretorioarcom):
    criardiretorio(diretorioarcom)

#Baixa arquivos do google drives
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
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

