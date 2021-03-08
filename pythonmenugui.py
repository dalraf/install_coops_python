#!/usr/bin/env python
import PySimpleGUI as sg
import subprocess

def executarscripts(values):
    if values[0]:
        print("Executando chocolatey")
        subprocess.call('C:\Windows\System32\powershell.exe Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString("https://chocolatey.org/install.ps1"))', shell=True)
    if values[1]:
        print("Executando Instalacao")
        programas = ["adobereader", "javaruntime --x86SteamSteam", "spark", "teamviewer", "anydesk.install", "googlechrome" , "firefox"]
        for programa in programas:
            subprocess.call("choco install -y " + programa, shell=True)


def Menu():
    sg.theme('LightBlue')
    sg.SetOptions(text_justification='right')

    flags = [[sg.Checkbox('Instalar Chocolatey', size=(24, 1))],
             [sg.Checkbox('Instalar programas padrão', size=(24, 1))]]

    layout = [[sg.Frame('Opções:', flags, font='Any 12', title_color='black')], [
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
