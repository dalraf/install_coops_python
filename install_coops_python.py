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
    
    for configuracao in executor.allconfiguration.lista:
        if values[configuracao.definicao]:
            configuracao.configurar()
       
    if values[varadicionarodominio]:
        addtodomain(values[vardominio],values[varusuario],values[varsenha])




#Funcao que gera o a GUI
def Menu():
    sg.theme('LightBlue')
    sg.SetOptions(text_justification='right')
    listainstalacao = []
    listaconfiguracao = []

    for program in executor.allprograms.lista:
        listainstalacao.append([sg.Checkbox(program.descricao , key=program.definicao, size=(24, 1))])

    for configuracao in executor.allcconfiguracao.lista:
        listaconfiguracao.append([sg.Checkbox(configuracao.descricao , key=configuracao.definicao, size=(24, 1))])

    instalacao = [
            [sg.Checkbox(executor.allprograms.descricao, key=executor.allprograms.descricao, size=(24, 1))],
            ]

    dominio = [
            [sg.Checkbox('Adicionar ao domínio', key=varadicionarodominio, size=(24, 1), enable_events=True)],
            [sg.Text('Domínio: '),sg.Input('',key=vardominio, background_color = 'white', border_width = 1, justification='left', size=(12, 1) , disabled=True)],
            [sg.Text('Usuário:  '),sg.Input('',key=varusuario, background_color = 'white', border_width = 1, justification='left', size=(12, 1), disabled=True)],
            [sg.Text('Senha:    '),sg.Input('',key=varsenha, password_char='*', background_color = 'white', border_width = 1, justification='left', size=(12, 1), disabled=True)],
            ]
    configuracao = [
            [sg.Text(executor.diretorioarcom.descricao),sg.Input(executor.diretorioarcom.diretorio,key=executor.diretorioarcom.definicao, background_color = 'white', border_width = 1, justification='left', size=(12, 1))],
            [sg.Frame('Domínio:', dominio , font='Any 12', title_color='black')],
             ]

    layout = [[sg.Frame('Instalação:', listainstalacao + instalacao , font='Any 12', title_color='black'),sg.Frame('Configuração:', listaconfiguracao + configuracao , font='Any 12', title_color='black')]
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
