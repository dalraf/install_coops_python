#!/usr/bin/env python
import PySimpleGUI as sg
from executors import Executor


executor = Executor("c:\\Arcom")

#Alterar campos do domínio
def mudarestadocamposdominio(window,estado):
    window[executor.adicionaraodominio.dominio.definicao].update(disabled = not estado)
    window[executor.adicionaraodominio.usuario.definicao].update(disabled = not estado)
    window[executor.adicionaraodominio.senha.definicao].update(disabled = not estado)



#Função que é executada de acordo com o retorno do valor do GUI
def executarscripts(values,executor):


    executor = Executor(values[executor.diretorioarcom.definicao])


    for program in executor.allprograms.lista:
        if values[program.definicao]:
            program.configurar()
    
    for configuracao in executor.allcconfiguracao.lista:
        if values[configuracao.definicao]:
            configuracao.configurar()
       
    if values[executor.adicionaraodominio.definicao]:
        executor.adicionaraodominio.configurar(values[executor.adicionaraodominio.dominio.definicao], \
                                                values[executor.adicionaraodominio.usuario.definicao], \
                                                values[executor.adicionaraodominio.senha.definicao]
                                                )





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
            [sg.Checkbox(executor.adicionaraodominio.descricao, key=executor.adicionaraodominio.definicao, size=(24, 1), enable_events=True)],
            [sg.Text(executor.adicionaraodominio.dominio.descricao, justification='left', size=(9, 1)),sg.Input('',key=executor.adicionaraodominio.dominio.definicao, background_color = 'white', border_width = 1, justification='left', size=(15, 1) , disabled=True)],
            [sg.Text(executor.adicionaraodominio.usuario.descricao, justification='left', size=(9, 1)),sg.Input('',key=executor.adicionaraodominio.usuario.definicao, background_color = 'white', border_width = 1, justification='left', size=(15, 1), disabled=True)],
            [sg.Text(executor.adicionaraodominio.senha.descricao, justification='left', size=(9, 1)),sg.Input('',key=executor.adicionaraodominio.senha.definicao, password_char='*', background_color = 'white', border_width = 1, justification='left', size=(15, 1), disabled=True)],
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

        if event == executor.adicionaraodominio.definicao:
            mudarestadocamposdominio(window,values[executor.adicionaraodominio.definicao])

        if event == 'Executar':
            executarscripts(values,executor)

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break
    
    window.close()

if __name__ == '__main__':
    Menu()
