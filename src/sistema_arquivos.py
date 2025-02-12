from bloco import Bloco
from arquivo import Arquivo
from diretorio import Diretorio

class SistemaDeArquivos:
    def __init__(self, tamanho_memoria, tamanho_bloco):
        self.tamanho_memoria = tamanho_memoria
        self.tamanho_bloco = tamanho_bloco
        self.blocos = [Bloco(i) for i in range(tamanho_memoria // tamanho_bloco)]
        self.diretorios = {'/': Diretorio('/')}
        self.fat = {}
        self.fragmentacao = 0
        
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
        diretorio.adicionar_arquivo(novo_arquivo)
        print(f"Arquivo '{nome}' criado com sucesso.")
        self.simular_alocacao()

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
        diretorio.remover_arquivo(arquivo)
        print(f"Arquivo '{nome}' excluído com sucesso.")
        self.simular_alocacao()

    def listar_arquivos(self, dir):
        diretorio = self.diretorios.get(dir)
        if(diretorio is None):
            print("Diretório não encontrado.")
            return
        diretorio.listar_arquivos()

    def criar_diretorio(self, nome):
        if(nome in [d.nome for d in self.diretorios.values()]):
            print("Diretório com esse nome já existe.")
            return
        novo_diretorio = Diretorio(nome)
        self.diretorios[nome] = novo_diretorio
        print(f"Diretório '{nome}' criado com sucesso.")

    def excluir_diretorio(self, nome):
        diretorio = self.diretorios.get(nome)
        if diretorio is None:
            print("Diretório não encontrado.")
            return
        self.diretorios.pop(nome)
        print(f"Diretório '{nome}' excluído com sucesso.")

    def listar_diretorios(self):
        for dir in self.diretorios.values():
            print(f"Diretório: {dir.nome}")

    def simular_alocacao(self):
        for bloco in self.blocos:
            status = "ocupado" if bloco.ocupado else "livre"
            print(f"Bloco {bloco.id}: {status}")
            