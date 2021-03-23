from vars import *
from functions import *


class Dominio():
    def __init__(self):
        self.descricao = "Domínio:"
        self.definicao = 'dominio'
        self.valor = ""

class Usuario():
    def __init__(self):
        self.descricao = "Usuario:"
        self.definicao = 'usuario'
        self.valor = ""

class Senha():
    def __init__(self):
        self.descricao = "Senha:"
        self.definicao = 'senha'
        self.valor = ""

class Adicionaraodominio():
    def __init__(self,diretorio):
        self.dominio = Dominio()
        self.usuario = Usuario()
        self.senha = Senha()
        self.descricao = "Adicionar ao domínio"
        self.definicao = "addtodomain"
    
    def configurar(self,dominio,usuario,senha):
        self.dominio.valor = dominio
        self.usuario.valor = usuario
        self.senha.valor = senha
        print("Adicionando ao domínio")
        addtodomain(self.dominio.valor,self.usuario.valor,self.senha.valor)


class Citrixcleanup():
    
    def __init__(self,diretorio):
        self.descricao = "Limpar registro do Citrix"
        self.definicao = "citrixcleanup"
    
    def configurar(self):
        print("Removendo registro")
        subprocess.call("reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\MSLicensing /f")

class Limpezageral():
    
    def __init__(self,diretorio):
        self.descricao = "Limpar diretório Arcom"
        self.definicao = "limpezageral"
        self.diretorio = diretorio
    
    def configurar(self):
        if os.path.exists(self.diretorio):
            shutil.rmtree(self.diretorio)

class Reniciar():
    
    def __init__(self,diretorio):
        self.descricao = "Reniciar cpu após execução"
        self.definicao = "reniciar"
        self.diretorio = diretorio
    
    def configurar(self):
        subprocess.call("shutdown /t 0 /r")

class OpenvpnStart():
    
    def __init__(self,diretorio):
        self.descricao = "Ativar openvpn"
        self.definicao = "openvpnstart"
        self.diretorio = diretorio
    
    def configurar(self):
        subprocess.call("sc config openvpnservice start=auto")
        subprocess.call("net start openvpnservice")

class OpenvpnStop():
    
    def __init__(self,diretorio):
        self.descricao = "Desativar openvpn"
        self.definicao = "openvpnstop"
        self.diretorio = diretorio
    
    def configurar(self):
        subprocess.call("sc config openvpnservice start=demand")
        subprocess.call("net stop openvpnservice")
    
        

