#!/usr/bin/env python
import PySimpleGUI as sg
import subprocess
import requests
import os
import shutil

diretorioarcomdefault = "c:\\Arcom"

programas = {
            "Adobe Reader":"adobereader", 
            "Java" : "javaruntime --x86SteamSteam", 
            "Spark": "spark", 
            "Teamviewer": "teamviewer",
            "Anydesk": "anydesk.install", 
            "Google Chrome": "googlechrome" , 
            "Firefox": "firefox"
            }


#executa instalacao de programas
def installprograma(programa):
    subprocess.call("c:\\ProgramData\\chocolatey\choco.exe install -y " + programa, shell=True)

#Cria Diretorio Arcom
def createdirarcom(diretorioarcom):
    if not os.path.exists(diretorioarcom):
        os.mkdir(diretorioarcom)


# Baixa arquivos do google drives
def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

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


#Funcões que são executadas de acordo com o retorno do valor do GUI
def executarscripts(values):

    diretorioarcom = values['diretorioarcom']

    if values['chocoinstall']:
        print("Executando chocolatey")
        subprocess.call('@"%SystemRoot%\System32\WindowsPowerShell\\v1.0\\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString(\'https://chocolatey.org/install.ps1\'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"', shell=True)
        subprocess.call("c:\\ProgramData\\chocolatey\choco.exe config set cacheLocation " + diretorioarcom, shell=True)


    for descricao, comando in programas.items():
        if values[comando]:
            print("Instalando " + descricao )
            installprograma(comando)
            

    if values['programsinstall']:
        print("Executando instalacao de todos os programas")
        for descricao, comando in programas.items():
                installprograma(comando)
    
    if values['sisbrinstall']:
        createdirarcom(diretorioarcom)
        print("Baixando sisbr 2.0")
        if not os.path.isfile(diretorioarcom + "\\sisbr2.0.exe"):
            file_id = '13E-X5fZZrj2FMZDIcLWJ94c9DgTqUA3f'
            destination = diretorioarcom + '\\sisbr2.0.exe'
            download_file_from_google_drive(file_id, destination)
            print("Download finalizado")
        print("Executando instalacao")
        subprocess.call(diretorioarcom + "\\sisbr2.0.exe")
    
    if values['citrixcleanup']:
        print("Removendo registro")
        subprocess.call("reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\MSLicensing /f")
    
    if values['sicoobnetinstall']:
        createdirarcom(diretorioarcom)
        if not os.path.isfile(diretorioarcom + "\\instalador-sicoobnet-windows-amd64.exe"):
            print("Baixando Sicoobnet Empresarial")
            urlsicoobnet = "https://office-sicoob-instalador.s3-us-west-2.amazonaws.com/instalador-sicoobnet-windows-amd64.exe"
            download = requests.get(urlsicoobnet, allow_redirects=True)
            open(diretorioarcom + "\\instalador-sicoobnet-windows-amd64.exe", 'wb').write(download.content)
        subprocess.call(diretorioarcom + "\\instalador-sicoobnet-windows-amd64.exe")
    
    if values['limpezageral']:
        if os.path.exists(diretorioarcom):
            shutil.rmtree(diretorioarcom)


#Funcao que gera o a GUI
def Menu():
    sg.theme('LightBlue')
    sg.SetOptions(text_justification='right')
    listainstalacao = []

    for descricao, comando in programas.items():
        listainstalacao.append([sg.Checkbox('Instalar ' + descricao, key=comando, size=(24, 1))])

    cabecalho = [
            [sg.Text('Diretório Arcom:'),sg.Input(diretorioarcomdefault,key='diretorioarcom', background_color = 'light gray', border_width = 1, justification='left', size=(12, 1))],
            [sg.Checkbox('Instalar Chocolatey', key='chocoinstall', size=(24, 1))],
            ]

    rodape = [
            [sg.Checkbox('Instalar programas padrão', key='programsinstall', size=(24, 1))],
            [sg.Checkbox('Instalar Sisbr 2.0', key='sisbrinstall', size=(24, 1))],
            [sg.Checkbox('Remover registro do Citrix', key='citrixcleanup', size=(24, 1))],
            [sg.Checkbox('Instalar SicoobNet empresarial', key='sicoobnetinstall', size=(24, 1))],
            [sg.Checkbox('Limpeza do diretório Arcom', key='limpezageral', size=(24, 1))],
            ]
    
    flags = cabecalho + listainstalacao + rodape

    layout = [[sg.Frame('Opções:', flags, font='Any 12', title_color='black')], [
        sg.Button('Executar'), sg.Button('Cancelar')]]

    window = sg.Window('Arcom Install', font=("Helvetica", 12)).Layout(layout)

    while True:
        event, values = window.read()
        if event == 'Executar':
            executarscripts(values)

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break

if __name__ == '__main__':
    Menu()
