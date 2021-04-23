import os
class Config():

    def __init__(self):

        self.diretorioarcom = "c:\\Arcom"

        if not os.path.exists(self.diretorioarcom):
            os.mkdir(self.diretorioarcom)

        self.chocolateypath = "c:\\ProgramData\\chocolatey\\choco.exe"

        self.filestringspark = """passwordSaved=true
        server=arcompbx.gotdns.com
        hostAndPort=false
        DisableHostnameVerification=true
        """
        self.programas = {
            "Adobe Reader": "adobereader",
            "Adobe Air": "adobeair",
            "Java": "javaruntime --x86SteamSteam",
                    "Spark": "spark",
                    "Teamviewer": "teamviewer",
                    "Anydesk": "anydesk.install",
                    "Google Chrome": "googlechrome",
                    "Firefox": "firefox"
        }
        self.allusersdesktop = "c:\\Users\\Public\\Desktop"
        self.userdesktop = "%USERPROFILE%\\Desktop"

    def criardiretorio(self, diretorio):
        if not os.path.exists(diretorio):
            os.mkdir(diretorio)