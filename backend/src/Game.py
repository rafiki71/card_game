# Game.py
from enum import Enum
from src.UtilClasses import Kartenfarbe, Karte, Deck, Spieler
# Hier können die Klassen Karte, Deck und Spieler eingefügt oder importiert werden, falls sie in separaten Dateien sind.

class Spielstatus(Enum):
    ANFANG = 1
    IM_GANG = 2
    ENDE = 3

class Game:
    def __init__(self):
        self.spieler = []
        self.deck = Deck()
        self.status = Spielstatus.ANFANG
        self.ausgelegte_karten = []
        self.aktueller_spieler_index = None

    def spieler_hinzufuegen(self, spieler: Spieler):
        if spieler.name in [spieler.name for spieler in self.spieler]:
            return True, "Spieler ist bereits im Spiel."
        
        if self.status != Spielstatus.ANFANG:
            return False, "Spiel ist bereits gestartet. Keine weiteren Spieler können hinzugefügt werden."
        
        if len(self.spieler) >= 4:
            return False, "Spiel ist bereits voll."
        
        self.spieler.append(spieler)
        return True, ""
            

    def karten_verteilen(self):
        self.deck.mischen()
        karten_pro_spieler = len(self.deck) // len(self.spieler)
        for spieler in self.spieler:
            spieler.karten_erhalten([self.deck.karte_ziehen() for _ in range(karten_pro_spieler)])
        self.ausgelegte_karten = []

        if len(self.deck) % len(self.spieler) != 0:
            spezielle_karten = [Karte(Kartenfarbe.HERZ, "7"), Karte(Kartenfarbe.KARO, "7")]
            for karte in spezielle_karten:
                if karte in self.deck.karten:
                    self.deck.karten.remove(karte)

    def finde_startspieler(self):
        for index, spieler in enumerate(self.spieler):
            if Karte(Kartenfarbe.KARO, "7") in spieler.hand:
                return index
            elif Karte(Kartenfarbe.PIK, "7") in spieler.hand:
                return index
        return 0

    def starte_spiel(self):
        if self.status != Spielstatus.ANFANG:
            return False, "Spiel ist bereits gestartet."
        
        self.karten_verteilen()
        self.aktueller_spieler_index = self.finde_startspieler()
        self.status = Spielstatus.IM_GANG
        return True, ""

    def karten_von_spieler_ausspielen(self, spieler_index, karten):
        if spieler_index != self.aktueller_spieler_index:
            return False  # Nicht der Zug des Spielers

        aktueller_spieler = self.spieler[spieler_index]
        gespielte_karten = aktueller_spieler.karten_ausspielen(karten)

        if gespielte_karten:
            self.ausgelegte_karten.extend(gespielte_karten)
            # Überprüfen, ob der Spieler gewonnen hat oder andere Spiellogiken

        # Den nächsten Spieler bestimmen
        self.aktueller_spieler_index = (self.aktueller_spieler_index + 1) % len(self.spieler)
        return True

    # Weitere Spielmethoden können hier hinzugefügt werden.

