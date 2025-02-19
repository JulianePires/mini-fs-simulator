class Diretorio:
    def __init__(self, nome):
        self.nome = nome
        self.arquivos = []
        
    def __repr__(self):
        return f"Diretorio(nome={self.nome}, arquivos={self.arquivos})"
    
    def adicionar_arquivo(self, arquivo):
        self.arquivos.append(arquivo)
        print(f"Arquivo '{arquivo.nome}' adicionado ao diretório '{self.nome}'.")
        
    def remover_arquivo(self, arquivo):
        if arquivo in self.arquivos:
            self.arquivos.remove(arquivo)
            print(f"Arquivo '{arquivo.nome}' removido do diretório '{self.nome}'.")
        else:
            print(f"Arquivo '{arquivo.nome}' não encontrado no diretório '{self.nome}'.")
            
    def __eq__(self, other):
        return self.nome == other.nome
    
    def renomear(self, novo_nome):
        self.nome = novo_nome
        print(f"Diretório renomeado para '{novo_nome}'.")
        
    def listar_arquivos(self):
        print(f"Arquivos no diretório '{self.nome}':")
        for arquivo in self.arquivos:
            print(arquivo)
            
    def __len__(self):
        return len(self.arquivos)