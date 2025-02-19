class Arquivo:
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho
        self.blocos = []
    
    def __repr__(self):
        return f"Arquivo(nome={self.nome}, tamanho={self.tamanho} bytes)"
    
    def alocar_blocos(self, blocos):
        self.blocos = blocos
        for bloco in blocos:
            bloco.ocupar()
              
    def desalocar_blocos(self):
        for bloco in self.blocos:
            bloco.desocupar()
        self.blocos = []
    
    def __len__(self):
        return self.tamanho
    
    def __eq__(self, other):
        return self.nome == other.nome
    
    def renomear(self, novo_nome):
        self.nome = novo_nome
        print(f"Arquivo renomeado para '{novo_nome}'.")