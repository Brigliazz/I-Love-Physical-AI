
class Robot
    def __init__(self, codice: str, modello: str, applicazione: str, peso_massimo_componenti_kg: float, stato: str) -> None:
        self.codice = codice
        self.modello = modello
        self.applicazione = applicazione
        self.peso_massimo_componenti_kg = peso_massimo_componenti_kg
        self.stato = stato
        self.componenti: list[Componente]
        
