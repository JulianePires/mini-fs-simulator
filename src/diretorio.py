class Diretorio:
    def __init__(self, nome):
        self.nome = nome
        self.arquivos = []
        self.senha_hash = None
        
    def __repr__(self):
        return f"Diretorio(nome={self.nome}, arquivos={self.arquivos}, protegido={self.senha_hash is not None})"
    
    def definir_senha(self, senha, criptografia):
        if len(senha) != 8:
            print("A senha deve ter exatamente 8 caracteres.")
        else:
            self.senha_hash = criptografia.criptografa_senha(senha)
    
    def acessar_diretorio(self, senha, criptografia):
        if self.senha_hash is None or criptografia.criptografa_senha(senha) == self.senha_hash:
            print(self)
        else:
            print("Senha incorreta.")
    
    def acessar_arquivo(self, nome_arquivo, senha, criptografia):
        if self.verifica_protecao_diretorio(criptografia):
            arquivo = self.buscar_arquivo(nome_arquivo)
            if arquivo:
                arquivo.acessar(senha, criptografia)
            else:
                print("Erro ao acessar o arquivo.")
        else:
            raise Exception("Acesso negado.")
        
    def definir_senha_arquivo(self, nome_arquivo, senha, criptografia):
        if self.verifica_protecao_diretorio(criptografia):
            arquivo = self.buscar_arquivo(nome_arquivo)
            if arquivo:
                arquivo.definir_senha(senha, criptografia)
            else:
                print("Arquivo não encontrado no diretório informado.")
        else:
            raise Exception("Acesso negado.")
    
    def adicionar_arquivo(self, arquivo, criptografia):
        if self.verifica_protecao_diretorio(criptografia):
            self.arquivos.append(arquivo)
            print(f"Arquivo '{arquivo.nome}' adicionado ao diretório '{self.nome}'.")
        else:
            raise Exception("Acesso negado.")
        
    def remover_arquivo(self, arquivo, criptografia):
        if self.verifica_protecao_diretorio(criptografia):
            if arquivo in self.arquivos:
                self.arquivos.remove(arquivo)
                print(f"Arquivo '{arquivo.nome}' removido do diretório '{self.nome}'.")
            else:
                print(f"Arquivo '{arquivo.nome}' não encontrado no diretório '{self.nome}'.")
        else:
            raise Exception("Acesso negado.")
            
    def __eq__(self, other):
        return self.nome == other.nome
    
    def renomear(self, novo_nome, criptografia):
        if self.verifica_protecao_diretorio(criptografia):
            self.nome = novo_nome
            print(f"Diretório renomeado para '{novo_nome}'.")
        else:
            raise Exception("Acesso negado.")
        
    def listar_arquivos(self, criptografia):
        if self.verifica_protecao_diretorio(criptografia):
            print(f"Arquivos no diretório '{self.nome}':")
            for arquivo in self.arquivos:
                print(arquivo)
        else:
            raise Exception("Acesso negado.")
            
    def __len__(self):
        return len(self.arquivos)
    
    def verifica_protecao_diretorio(self, criptografia):
        if self.senha_hash:
            print("Diretório protegido por senha.")
            print("Digite a senha para acessar os arquivos.")
            senha = input("Senha: ")
            if criptografia.criptografa_senha(senha) != self.senha_hash:
                print("Senha incorreta.")
                return False
        return True
    
    def buscar_arquivo(self, nome_arquivo):
        for arquivo in self.arquivos:
            if arquivo.nome == nome_arquivo:
                return arquivo
        return None