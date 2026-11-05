
class Componente:
    def __init__(self, codice: str, nome: str, peso_kg: float) -> None:
        self.codice = codice
        self.nome = nome
        self.peso_kg = peso_kg
        

class Robot:
    def __init__(self, codice: str, modello: str, applicazione: str, peso_massimo_componenti_kg: float, stato: str) -> None:
        self.codice = codice
        self.modello = modello
        self.applicazione = applicazione
        self.peso_massimo_componenti_kg = peso_massimo_componenti_kg
        self.stato = stato
        self.componenti: list[Componente]
        
    def aggiungi_componente(componente: Componente)-> None :
        if componente.codice in componenti:
            raise ValueError("componente gia presente")
        else:
            componenti.insert(componente)
    
    def peso_componenti()-> float:
        for i in componenti:
            return i.peso_kg
        
    def cerca_componente(codice: str)-> Componente:
        for i in componenti:
            if i.codice == codice:
                return i
            else:
                raise ValueError("componente non esiste")
    
    def rimuovi_componente (codice: str)-> Componente:
        for i in componenti:
            if i.codice == componenti.codice:
                return i
                componenti.remove(i)
            else:
                raise ValueError("componente non esiste")
            
    
    def componenti_sotto_peso (peso_massimo: float):
         for i in componenti:
            if i.peso_kg <= peso_massimo:
                componenti.remove(i)
def __main__():
    componente = Componente(a, b,123)
    pint(f"{componente}")
    

    