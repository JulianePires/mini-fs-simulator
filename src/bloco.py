class Bloco:
    def __init__(self, id):
        self.id = id
        self.ocupado = False
    
    def __repr__(self):
        return f"Bloco(id={self.id}, ocupado={self.ocupado})"
    
    def ocupar(self):
        self.ocupado = True
        
    def desocupar(self):
        self.ocupado = False