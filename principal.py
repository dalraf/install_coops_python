from instalacao import (
    Spark,
    Adobeair,
    Java,
    Caixainstall,
    Teamviewer,
    Anydesk,
    Googlechrome,
    Firefox,
    Sisbrinstall,
    Citrixinstall,
    Sicoobnetinstall,
    Adobereader,
)
from configuracao import (
    Adicionaraodominio,
    Citrixcleanup,
    OpenvpnStart,
    OpenvpnStop,
    Reniciar,
)


class Programas:
    def __init__(self):
        self.lista = []
        self.lista.append(Spark())
        self.lista.append(Adobeair())
        self.lista.append(Adobereader())
        self.lista.append(Java())
        self.lista.append(Caixainstall())
        self.lista.append(Teamviewer())
        self.lista.append(Anydesk())
        self.lista.append(Googlechrome())
        self.lista.append(Firefox())
        self.lista.append(Sisbrinstall())
        self.lista.append(Citrixinstall())
        self.lista.append(Sicoobnetinstall())


class Configuracoes:
    def __init__(self):
        self.lista = []
        self.lista.append(Adicionaraodominio())
        self.lista.append(Citrixcleanup())
        self.lista.append(OpenvpnStart())
        self.lista.append(OpenvpnStop())
        self.lista.append(Reniciar())

    def configurar(self):
        for configuracao in self.lista:
            configuracao.configurar()


class Principal:
    def __init__(self):
        self.programas = Programas()
        self.configuracoes = Configuracoes()
