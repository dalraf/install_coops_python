#!/usr/bin/env python
import PySimpleGUI as sg
import subprocess
import requests
import os


diretorioarcom = "c:\\arcom"

#Cria Diretorio Arcom
def createdirarcom():
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
    if values[0]:
        print("Executando chocolatey")
        subprocess.call('C:\Windows\System32\powershell.exe Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString("https://chocolatey.org/install.ps1"))', shell=True)
    if values[1]:
        print("Executando Instalacao")
        programas = ["adobereader", "javaruntime --x86SteamSteam", "spark", "teamviewer", "anydesk.install", "googlechrome" , "firefox"]
        for programa in programas:
            subprocess.call("choco install -y " + programa, shell=True)
    if values[2]:
        createdirarcom()
        print("Baixando sisbr 2.0")
        if not os.path.isfile(diretorioarcom + "\\sisbr2.0.exe"):
            file_id = '13E-X5fZZrj2FMZDIcLWJ94c9DgTqUA3f'
            destination = diretorioarcom + '\\sisbr2.0.exe'
            download_file_from_google_drive(file_id, destination)
            print("Download finalizado")
        print("Executando instalacao")
        subprocess.call(diretorioarcom + "\\sisbr2.0.exe")
    if values[3]:
        print("Removendo registro")
        subprocess.call("reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\MSLicensing /f")
    if values[4]:
        createdirarcom()
        if not os.path.isfile(diretorioarcom + "\\instalador-sicoobnet-windows-amd64.exe"):
            print("Baixando Sicoobnet Empresarial")
            urlsicoobnet = "https://office-sicoob-instalador.s3-us-west-2.amazonaws.com/instalador-sicoobnet-windows-amd64.exe"
            download = requests.get(urlsicoobnet, allow_redirects=True)
            open(diretorioarcom + "\\instalador-sicoobnet-windows-amd64.exe", 'wb').write(download.content)
        subprocess.call(diretorioarcom + "\\instalador-sicoobnet-windows-amd64.exe")

#Funcao que gera o a GUI
def Menu():
    sg.theme('LightBlue')
    sg.SetOptions(text_justification='right')

    flags = [
            [sg.Checkbox('Instalar Chocolatey', size=(24, 1))],
            [sg.Checkbox('Instalar programas padrão', size=(24, 1))],
            [sg.Checkbox('Instalar sisbr 2.0', size=(24, 1))],
            [sg.Checkbox('Remover registro do Citrix', size=(24, 1))],
            [sg.Checkbox('Instalar SicoobNet empresarial', size=(24, 1))],
            ]

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
