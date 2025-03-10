from bloco import Bloco
from arquivo import Arquivo
from diretorio import Diretorio
from criptografia import Criptografia

class SistemaDeArquivos:
    def __init__(self, tamanho_memoria, tamanho_bloco):
        self.tamanho_memoria = tamanho_memoria
        self.tamanho_bloco = tamanho_bloco
        self.blocos = [Bloco(i) for i in range(tamanho_memoria // tamanho_bloco)]
        self.diretorios = {'/': Diretorio('/')}
        self.fat = {}
        self.fragmentacao = 0
        self.criptografia = Criptografia()
        
    def calcular_fragmentacao_interna(self):
        self.files = {}
        for diretorio in self.diretorios.values():
            for arquivo in diretorio.arquivos:
                self.files[arquivo.nome] = arquivo
        for file in self.files.values():
            tamanho_arquivo = file.tamanho
            blocos_necessarios = (tamanho_arquivo + self.tamanho_bloco - 1) // self.tamanho_bloco
            fragmentacao_arquivo = (blocos_necessarios * self.tamanho_bloco) - tamanho_arquivo
            self.fragmentacao += fragmentacao_arquivo
        print(f"Fragmentação interna total: {self.fragmentacao} bytes")

    def calcular_fragmentacao_externa(self):
        free_blocos = 0
        largest_free_bloco = 0
        current_free_bloco = 0

        for bloco in self.blocos:
            if bloco is None:
                free_blocos += 1
                current_free_bloco += 1
            else:
                if current_free_bloco > largest_free_bloco:
                    largest_free_bloco = current_free_bloco
                current_free_bloco = 0

        if current_free_bloco > largest_free_bloco:
            largest_free_bloco = current_free_bloco

        external_fragmentation = free_blocos * self.tamanho_bloco - largest_free_bloco * self.tamanho_bloco
        print(f"Fragmentação externa total: {external_fragmentation} bytes")


    def criar_arquivo(self, nome, tamanho, dir):
        diretorio = self.diretorios.get(dir)
        if(diretorio is None):
            print("Diretório não encontrado.")
            return
        if any(arq.nome == nome for arq in diretorio.arquivos):
            print("Arquivo com esse nome já existe.")
            return
        num_blocos = (tamanho + self.tamanho_bloco - 1) // self.tamanho_bloco
        blocos_livres = [bloco for bloco in self.blocos if not bloco.ocupado]
        if len(blocos_livres) < num_blocos:
            print("Memória insuficiente.")
            return
        novo_arquivo = Arquivo(nome, tamanho)
        for i in range(num_blocos):
            bloco = blocos_livres[i]
            bloco.ocupar()
            novo_arquivo.blocos.append(bloco.id)
            self.fat[bloco.id] = novo_arquivo
        try:
            diretorio.adicionar_arquivo(novo_arquivo, self.criptografia)
            print(f"Arquivo '{nome}' criado com sucesso.")
            self.simular_alocacao()
        except Exception as e:
            print(e)    
            

    def excluir_arquivo(self, nome, dir):
        diretorio = self.diretorios.get(dir)
        if(diretorio is None):
            print("Diretório não encontrado.")
            return
        arquivo = next((arq for arq in diretorio.arquivos if arq.nome == nome), None)
        if arquivo is None:
            print("Arquivo não encontrado.")
            return
        for bloco_id in arquivo.blocos:
            bloco = next(bloco for bloco in self.blocos if bloco.id == bloco_id)
            bloco.desocupar()
            del self.fat[bloco_id]
        try:
            diretorio.remover_arquivo(arquivo, self.criptografia)
            print(f"Arquivo '{nome}' excluído com sucesso.")
            self.simular_alocacao()
        except Exception as e:
            print(e)  
       

    def listar_arquivos(self, dir):
        diretorio = self.diretorios.get(dir)
        if(diretorio is None):
            print("Diretório não encontrado.")
            return
        try:
            diretorio.listar_arquivos(self.criptografia)
        except Exception as e:
            print(e)  

    def criar_diretorio(self, nome):
        if(nome in [d.nome for d in self.diretorios.values()]):
            print("Diretório com esse nome já existe.")
            return
        novo_diretorio = Diretorio(nome)
        self.diretorios[nome] = novo_diretorio
        print(f"Diretório '{nome}' criado com sucesso.")

    def excluir_diretorio(self, nome):
        diretorio = self.diretorios.get(nome)
        if diretorio.verifica_protecao_diretorio(self.criptografia):    
            if diretorio is None:
                print("Diretório não encontrado.")
                return
            for arq in diretorio.arquivos:
                self.excluir_arquivo(arq.nome, diretorio.nome)
            self.diretorios.pop(nome)
            print(f"Diretório '{nome}' excluído com sucesso.")
            self.simular_alocacao()
        else:
            print("Acesso negado.")

    def listar_diretorios(self):
        for dir in self.diretorios.values():
            if(dir.senha_hash is None):
                print(dir)
            else:
                print(f"{dir.nome} (protegido)")

    def simular_alocacao(self):
        for bloco in self.blocos:
            status = "ocupado" if bloco.ocupado else "livre"
            print(f"Bloco {bloco.id}: {status}")
            
    def definir_senha_diretorio(self, nome_diretorio, senha):
        diretorio = self.diretorios.get(nome_diretorio)
        if diretorio is None:
            print("Diretório não encontrado.")
            return
        diretorio.definir_senha(senha, self.criptografia)
        
    def definir_senha_arquivo(self, nome_arquivo, nome_diretorio, senha):
        diretorio = self.diretorios.get(nome_diretorio)
        if diretorio is None:
            print("Diretório não encontrado.")
            return
        try:
            diretorio.definir_senha_arquivo(nome_arquivo, senha, self.criptografia)
        except Exception as e:
            print(e)
    
    def acessar_arquivo_protegido(self, nome_arquivo, nome_diretorio, senha):
        diretorio = self.diretorios.get(nome_diretorio)
        if diretorio is None:
            print("Diretório não encontrado.")
            return
        try:
            diretorio.acessar_arquivo(nome_arquivo, senha, self.criptografia)
        except Exception as e:
            print(e)
    
    def acessar_diretorio_protegido(self, nome_diretorio, senha):
        diretorio = self.diretorios.get(nome_diretorio)
        if diretorio is None:
            print("Diretório não encontrado.")
            return
        diretorio.acessar_diretorio(senha, self.criptografia)
        
    def proteger_arquivo(self, nome_arquivo, nome_diretorio, senha):
        diretorio = self.diretorios.get(nome_diretorio)
        print(diretorio)
        if diretorio is None:
            print("Diretório não encontrado.")
            return
        try:
            diretorio.definir_senha_arquivo(nome_arquivo, senha, self.criptografia)
        except Exception as e:
            print(e)
        
    def proteger_diretorio(self, nome_diretorio, senha):
        diretorio = self.diretorios.get(nome_diretorio)
        if diretorio is None:
            print("Diretório não encontrado.")
            return
        diretorio.definir_senha(senha, self.criptografia)
        