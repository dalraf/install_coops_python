#!/usr/bin/env python
import PySimpleGUI as sg
from principal import Principal
from log import error_log
import time
import threading

error_log.addlog("")

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
                                                                                                      listaconfiguracao, font='Any 12', title_color='black')], [sg.Button('Executar'), sg.Button('Cancelar'), sg.Input(key='log', background_color='white', border_width=1, justification='left', size=(40, 1), disabled=True)]]

    window = sg.Window('Arcom Install', font=("Helvetica", 12)).Layout(layout)

    def update_log():
        while True:
            time.sleep(2)
            if error_log.stop_thread:
                break
            if not error_log.stop_thread:
                window.write_event_value('log', 'log')

    processo_log = threading.Thread(target=update_log, args=())
    processo_log.start()

    while True:
        event, values = window.read()

        if event == 'log':
            window['log'].update(value=error_log.log[-1])

        for objeto in principal.programas.lista + principal.configuracoes.lista:
            if values[objeto.definicao]:
                objeto.change_gui(window, values)
                if event == 'Executar':
                    objeto.configurar(window, values)

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break

    error_log.stop_thread = True
    time.sleep(2)
    window.close()


if __name__ == '__main__':
    Menu()
