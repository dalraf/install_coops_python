#!/usr/bin/env python
import PySimpleGUI as sg
from principal import Principal
import time
import threading

principal = Principal()

# Funcao que gera o a GUI


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
            objeto.change_gui(window, values)
            objeto.verify_thread(window, values)
            if event == 'Executar' and values[objeto.definicao]:
                objeto.configurar(window, values)

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break

    window.close()


if __name__ == '__main__':
    Menu()
