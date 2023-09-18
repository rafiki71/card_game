from enum import Enum
import random


class Kartenfarbe(Enum):
    HERZ = "Herz"
    KARO = "Karo"
    PIK = "Pik"
    KREUZ = "Kreuz"


class Karte:
    def __init__(self, farbe: Kartenfarbe, wert: str):
        self.farbe = farbe
        self.wert = wert
    
    def to_dict(self):
        return {
            "farbe": self.farbe.value,
            "wert": self.wert
        }

    def __repr__(self):
        return f"{self.wert} von {self.farbe.value}"


class Deck:
    def __init__(self):
        self.karten = self._initialisiere_deck()

    def _initialisiere_deck(self):
        werte = ["7", "8", "9", "10", "Bube", "Dame", "König", "Ass"]
        return [Karte(farbe, wert) for farbe in Kartenfarbe for wert in werte]

    def mischen(self):
        random.shuffle(self.karten)

    def karte_ziehen(self):
        return self.karten.pop()

    def karten_entfernen(self, anzahl: int):
        return [self.karten.pop() for _ in range(anzahl)]

    def __len__(self):
        return len(self.karten)

    def __repr__(self):
        return str(self.karten)


class Spieler:
    def __init__(self, name: int):
        self.name = name
        self.hand = []
        self.status = None  # Kann später durch "Präsident", "Pieper" usw. ersetzt werden

    def karten_ausspielen(self, karten: [Karte]):
        if not karten:
            return None

        # Prüfen, ob alle Karten den gleichen Wert haben
        erstes_karten_wert = karten[0].wert
        if not all(karte.wert == erstes_karten_wert for karte in karten):
            return None

        # Prüfen, ob alle Karten in der Hand des Spielers sind
        if not all(karte in self.hand for karte in karten):
            return None

        # Karten aus der Hand des Spielers entfernen
        for karte in karten:
            self.hand.remove(karte)

        return karten


    def karten_erhalten(self, karten: list):
        self.hand.extend(karten)

    def karten_abgeben(self, anzahl: int):
        abgegebene_karten = self.hand[:anzahl]
        self.hand = self.hand[anzahl:]
        return abgegebene_karten

    def __repr__(self):
        return f"Spieler {self.spieler_id} mit {len(self.hand)} Karten"