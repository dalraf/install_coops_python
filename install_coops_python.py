#!/usr/bin/env python
import PySimpleGUI as sg
import subprocess
import requests
import os
import shutil
import zipfile
from executors import Executor
from vars import *

executor = Executor("c:\\Arcom")



#Função que é executada de acordo com o retorno do valor do GUI
def executarscripts(values,executor):


    executor = Executor(values[executor.diretorioarcom.definicao])

    for program in executor.allprograms.lista:
        if values[program.definicao]:
            program.configurar()
    
    if values[varsisbrinstall]:
        createdirarcom(diretorioarcom)
        print("Baixando sisbr 2.0")
        if not os.path.isfile(diretorioarcom + "\\sisbr2.0.exe"):
            file_id = '13E-X5fZZrj2FMZDIcLWJ94c9DgTqUA3f'
            destination = diretorioarcom + '\\sisbr2.0.exe'
            download_file_from_google_drive(file_id, destination)
            print("Download finalizado")
        print("Executando instalacao")
        subprocess.call(diretorioarcom + "\\sisbr2.0.exe")

    if values[varcitrixinstall]:
        createdirarcom(diretorioarcom)
        diretoriocitrix = diretorioarcom + "\\Citrix"
        criardiretorio(diretoriocitrix)
        print("Baixando citrix 10")
        if not os.path.isfile(diretorioarcom + "\\Citrix10.zip"):
            file_id = '19o1eGqGL6xR1B9b3VYunea4zzYe3Heb9'
            destination = diretorioarcom + '\\Citrix10.zip'
            download_file_from_google_drive(file_id, destination)
            print("Download finalizado")
        print("Executando descompacação")
        with zipfile.ZipFile(diretorioarcom + '\\Citrix10.zip', 'r') as citrixzip:
            citrixzip.extractall(diretoriocitrix)
        subprocess.call('msiexec /i "' + diretoriocitrix + '\\Citrix10\\Versao 10.1\\PN_10_1.msi"')
    
    if values[varcitrixcleanup]:
        print("Removendo registro")
        subprocess.call("reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\MSLicensing /f")
    
    if values[varsicoobnetinstall]:
        createdirarcom(diretorioarcom)
        if not os.path.isfile(diretorioarcom + "\\instalador-sicoobnet-windows-amd64.exe"):
            print("Baixando Sicoobnet Empresarial")
            urlsicoobnet = "https://office-sicoob-instalador.s3-us-west-2.amazonaws.com/instalador-sicoobnet-windows-amd64.exe"
            download = requests.get(urlsicoobnet, allow_redirects=True)
            open(diretorioarcom + "\\instalador-sicoobnet-windows-amd64.exe", 'wb').write(download.content)
        subprocess.call(diretorioarcom + "\\instalador-sicoobnet-windows-amd64.exe")
    
    if values[varadicionarodominio]:
        addtodomain(values[vardominio],values[varusuario],values[varsenha])
    
    if values[varlimpezageral]:
        if os.path.exists(diretorioarcom):
            shutil.rmtree(diretorioarcom)

    if values[varreniciar]:
        subprocess.call("shutdown /t0 /r")


#Funcao que gera o a GUI
def Menu():
    sg.theme('LightBlue')
    sg.SetOptions(text_justification='right')
    listainstalacao = []

    for program in executor.allprograms.lista:
        listainstalacao.append([sg.Checkbox(program.descricao , key=program.definicao, size=(24, 1))])


    instalacao = [
            [sg.Checkbox(executor.allprograms.descricao, key=executor.allprograms.descricao, size=(24, 1))],
            [sg.Checkbox('Instalar Sisbr 2.0', key=varsisbrinstall, size=(24, 1))],
            [sg.Checkbox('Instalar Citrix 10', key=varcitrixinstall, size=(24, 1))],
            [sg.Checkbox('Instalar SicoobNet empresarial', key=varsicoobnetinstall, size=(24, 1))],
            ]
    dominio = [
            [sg.Checkbox('Adicionar ao domínio', key=varadicionarodominio, size=(24, 1), enable_events=True)],
            [sg.Text('Domínio: '),sg.Input('',key=vardominio, background_color = 'white', border_width = 1, justification='left', size=(12, 1) , disabled=True)],
            [sg.Text('Usuário:  '),sg.Input('',key=varusuario, background_color = 'white', border_width = 1, justification='left', size=(12, 1), disabled=True)],
            [sg.Text('Senha:    '),sg.Input('',key=varsenha, password_char='*', background_color = 'white', border_width = 1, justification='left', size=(12, 1), disabled=True)],
            ]
    configuracao = [
            [sg.Text(executor.diretorioarcom.descricao),sg.Input(executor.diretorioarcom.diretorio,key=executor.diretorioarcom.definicao, background_color = 'white', border_width = 1, justification='left', size=(12, 1))],
            [sg.Checkbox('Remover registro do Citrix', key=varcitrixcleanup, size=(24, 1))],
            [sg.Checkbox('Limpeza do diretório Arcom', key=varlimpezageral, size=(24, 1))],
            [sg.Checkbox('Reniciar cpu após execuçào', key=varreniciar, size=(24, 1))],
            [sg.Frame('Domínio:', dominio , font='Any 12', title_color='black')],
             ]

    layout = [[sg.Frame('Instalação:', listainstalacao + instalacao , font='Any 12', title_color='black'),sg.Frame('Configuração:',configuracao , font='Any 12', title_color='black')]
              ,[sg.Button('Executar'), sg.Button('Cancelar')]]

    window = sg.Window('Arcom Install', font=("Helvetica", 12)).Layout(layout)

    while True:
        event, values = window.read()

        if event == 'adicionaraodominio':
            mudarestadocamposdominio(window,values['adicionaraodominio'])

        if event == 'Executar':
            executarscripts(values,executor)

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break
    
    window.close()

if __name__ == '__main__':
    Menu()
