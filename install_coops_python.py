#!/usr/bin/env python
import PySimpleGUI as sg
from principal import Principal


principal = Principal("c:\\Arcom")

# Alterar campos do domínio


def mudarestadocamposdominio(window, estado):
    window[principal.configuracoes.adicionaraodominio.dominio.definicao].update(
        disabled=not estado)
    window[principal.configuracoes.adicionaraodominio.usuario.definicao].update(
        disabled=not estado)
    window[principal.configuracoes.adicionaraodominio.senha.definicao].update(
        disabled=not estado)


# Função que é executada de acordo com o retorno do valor do GUI
def executarscripts(values, principal):

    principal = Principal(values[principal.diretorioarcom.definicao])

    for programa in principal.programas.lista():
        if values[programa.definicao]:
            programa.configurar()

    if values[principal.configuracoes.adicionaraodominio.definicao]:
        principal.configuracoes.adicionaraodominio.configurar(values[principal.configuracoes.adicionaraodominio.dominio.definicao],
                                                              values[principal.configuracoes.adicionaraodominio.usuario.definicao],
                                                              values[principal.configuracoes.adicionaraodominio.senha.definicao]
                                                              )

    for configuracao in principal.configuracoes.lista():
        if values[configuracao.definicao]:
            configuracao.configurar()


# Funcao que gera o a GUI
def Menu():
    sg.theme('LightBlue')
    sg.SetOptions(text_justification='right')
    listainstalacao = []
    listaconfiguracao = []

    for programa in principal.programas.lista():
        listainstalacao.append(
            [sg.Checkbox(programa.descricao, key=programa.definicao, size=(24, 1))])

    for configuracao in principal.configuracoes.lista():
        listaconfiguracao.append(
            [sg.Checkbox(configuracao.descricao, key=configuracao.definicao, size=(24, 1))])

    instalacao = [
        [sg.Checkbox(principal.programas.descricao,
                     key=principal.programas.descricao, size=(24, 1))],
    ]

    dominio = [
        [sg.Checkbox(principal.configuracoes.adicionaraodominio.descricao,
                     key=principal.configuracoes.adicionaraodominio.definicao, size=(24, 1), enable_events=True)],
        [sg.Text(principal.configuracoes.adicionaraodominio.dominio.descricao, justification='left', size=(9, 1)), sg.Input(
            '', key=principal.configuracoes.adicionaraodominio.dominio.definicao, background_color='white', border_width=1, justification='left', size=(15, 1), disabled=True)],
        [sg.Text(principal.configuracoes.adicionaraodominio.usuario.descricao, justification='left', size=(9, 1)), sg.Input(
            '', key=principal.configuracoes.adicionaraodominio.usuario.definicao, background_color='white', border_width=1, justification='left', size=(15, 1), disabled=True)],
        [sg.Text(principal.configuracoes.adicionaraodominio.senha.descricao, justification='left', size=(9, 1)), sg.Input(
            '', key=principal.configuracoes.adicionaraodominio.senha.definicao, password_char='*', background_color='white', border_width=1, justification='left', size=(15, 1), disabled=True)],
    ]
    configuracao = [
        [sg.Text(principal.diretorioarcom.descricao), sg.Input(principal.diretorioarcom.diretorio,
                                                               key=principal.diretorioarcom.definicao, background_color='white', border_width=1, justification='left', size=(12, 1))],
        [sg.Frame('Domínio:', dominio, font='Any 12', title_color='black')],
    ]

    layout = [[sg.Frame('Instalação:', listainstalacao + instalacao, font='Any 12', title_color='black'), sg.Frame('Configuração:',
                                                                                                                   listaconfiguracao + configuracao, font='Any 12', title_color='black')], [sg.Button('Executar'), sg.Button('Cancelar')]]

    window = sg.Window('Arcom Install', font=("Helvetica", 12)).Layout(layout)

    while True:
        event, values = window.read()

        if event == principal.configuracoes.adicionaraodominio.definicao:
            mudarestadocamposdominio(
                window, values[principal.configuracoes.adicionaraodominio.definicao])

        if event == 'Executar':
            executarscripts(values, principal)

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break

    window.close()


if __name__ == '__main__':
    Menu()
