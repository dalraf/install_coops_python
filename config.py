import os
class Config():

    def __init__(self):

        self.diretorioarcom = "c:\\Arcom"

        self.criardiretorio(self.diretorioarcom)

        self.javapathsearch = r'"C:\Program Files (x86)\Java\*\bin\java.exe"'

        self.chocolateypath = r"c:\ProgramData\chocolatey\choco.exe"

        self.filestringspark = """passwordSaved=true
        server=arcompbx.gotdns.com
        hostAndPort=false
        DisableHostnameVerification=true
        """
        
        self.allusersdesktop = r"c:\Users\Public\Desktop"
        self.userdesktop = r"%USERPROFILE%\Desktop"

    def criardiretorio(self, diretorio):
        if not os.path.exists(diretorio):
            os.mkdir(diretorio)