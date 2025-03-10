class Arquivo:
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho
        self.blocos = []
        self.senha_hash = None
    
    def __repr__(self):
        return f"Arquivo(nome={self.nome}, tamanho={self.tamanho} bytes, protegido={self.senha_hash is not None})"
    
    def definir_senha(self, senha, criptografia):
        if len(senha) != 8:
            print("A senha deve ter exatamente 8 caracteres.")
        else:
            self.senha_hash = criptografia.criptografa_senha(senha)
    
    def acessar(self, senha, criptografia):
        if self.senha_hash is None or criptografia.criptografa_senha(senha) == self.senha_hash:
            print(self)
        else:
            print("Senha incorreta.")
        
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