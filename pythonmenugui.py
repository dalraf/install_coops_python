#!/usr/bin/env python
import PySimpleGUI as sg


def executarscripts(values):
    if values[0]:
        print("Executando chocolatey")
    if values[1]:
        print("Executando Instalacao")

def Menu():
    sg.SetOptions(text_justification='right')

    flags = [[sg.Checkbox('Instalar Chocolatey', size=(24, 1))],
             [sg.Checkbox('Instalar programas padrão', size=(24, 1))]]

    layout = [[sg.Frame('Intens', flags, font='Any 12', title_color='yellow')], [
        sg.Button('Executar'), sg.Button('Cancelar')]]

    window = sg.Window('Arcom Install', font=("Helvetica", 12)).Layout(layout)
    button, values = window.Read()
    sg.SetOptions(text_justification='left')

    while True:
        event, values = window.read()
        if event == 'Executar':
            executarscripts(values)

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break

if __name__ == '__main__':
    Menu()
