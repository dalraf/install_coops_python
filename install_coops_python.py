#!/usr/bin/env python
import PySimpleGUI as sg
from principal import Principal
import time
import threading

listaexecutar = []
indexecutar = -1

principal = Principal()

# Funcao que gera o a GUI

def runsequencial(lista, window, values):
    for objeto in lista:
        objeto.configurar(window, values)



def Menu():
    sg.theme('LightBlue')
    sg.SetOptions(text_justification='right')
    listainstalacao = []
    listaconfiguracao = []

    for programa in principal.programas.lista:
        listainstalacao.append(programa.gui())

    for configuracao in principal.configuracoes.lista:
        listaconfiguracao.append(configuracao.gui())

    layout = [[sg.Frame('Instalação:', listainstalacao, font='Any 12', title_color='black'), sg.Frame('Configuração:',
                                                                                                      listaconfiguracao, font='Any 12', title_color='black')], [sg.Button('Executar'), sg.Button('Cancelar'),]]
    window = sg.Window('Arcom Install', font=("Helvetica", 12)).Layout(layout)

    while True:
        event, values = window.read()

        for objeto in principal.programas.lista + principal.configuracoes.lista:
            if event == objeto.definicao:
                objeto.change_gui(window, values)
            if event == objeto.verify_thread_descricao:
                objeto.verify_thread(window, values)
            if event == 'Executar' and values[objeto.definicao] == True:
                if not objeto in listaexecutar:
                    listaexecutar.append(objeto)
            elif values[objeto.definicao] == False:
                if objeto in listaexecutar:
                    listaexecutar.remove(objeto)
        
        if event == 'Executar':
            execucao = threading.Thread(target=runsequencial, args=(listaexecutar, window, values))
            execucao.start()

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break

    window.close()


if __name__ == '__main__':
    Menu()
