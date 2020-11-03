class Tarkvara:
    """
    Baasklass erinevate OS-ide installeerijate jaoks
    """

    def __init__(self, baaskataloog):
        self.baaskataloog = baaskataloog

    def installeeri(self):
        """
        Šabloonmeetod, mis installeerib tarkvara 
        """
        if not self.kataloog_sobib(self.baaskataloog):
            self.baaskataloog = "varukataloog"
        self.valmista_kataloog(self.baaskataloog + "\\bin")
        self.installeeri_failid(self.baaskataloog + "\\bin", ["proge.exe", "proge.bat"])
        self.valmista_kataloog(self.baaskataloog + "\\dat")
        self.installeeri_failid(self.baaskataloog + "\\dat", ["mudelid.dat", "andmed.dat"])
        
    def kataloog_sobib(self, kataloog):
        """Primitiivne operatsioon, mis kontrollib, kas kataloog sobib"""
        raise NotImplementedError

    def valmista_kataloog(self, kataloog):
        """Primitiivne operatsioon, mis valmistab kataloogi"""
        raise NotImplementedError
   
    def installeeri_failid(self, kataloog, failid):
        """Primitiivne operatsioon, mis installeerib failid kataloogi"""
        raise NotImplementedError


class WindowsTarkvara(Tarkvara):
    """
    Installeerija Windowsile
    Defineerib primitiivsed operatsioonid.
    Šabloonmeetod installeeri() võetakse ülemklassist, seda muuta pole vaja.
    """

    def kataloog_sobib(self, kataloog):
        print("Kontrollin kataloogi " + kataloog + " sobivust Windowsile")
        return len(kataloog) < 8

    def valmista_kataloog(self, kataloog):
        print("Valmistan kataloogi " + kataloog + " Windowsile")
        
    def installeeri_failid(self, kataloog, failid):
        for fail in failid:
            print("Tekitan Windowsis faili " + kataloog + "\\" + fail)
            

class UnixTarkvara(Tarkvara):
    """
    Installeerija Unixile
    Defineerib primitiivsed operatsioonid.
    Šabloonmeetod installeeri() võetakse ülemklassist, seda muuta pole vaja.
    """

    def kataloog_sobib(self, kataloog):
        print("Kontrollin kataloogi " + kataloog + " sobivust Unixile")
        return len(kataloog) > 2

    def valmista_kataloog(self, kataloog):
        print("Valmistan kataloogi " + kataloog + " Unixile")
        
    def installeeri_failid(self, kataloog, failid):
        for fail in failid:
            print("Tekitan Unixis faili " + kataloog + "\\" + fail)


def demonstreeri():
    print("Demonstreerime WindowsTarkvara")
    tw = WindowsTarkvara("usr\\kataloog")
    tw.installeeri()
    print("\nDemonstreerime UnixTarkvara")
    tu = UnixTarkvara("usr\\kataloog")
    tu.installeeri()


if __name__ == "__main__":
    demonstreeri()

    
