import hashlib
import itertools
import string
import time

class Criptografia:
    def criptografa_senha(self, password):
        # Gera o hash da senha usando SHA-256
        hash_object = hashlib.sha256(password.encode())
        return hash_object.hexdigest()
    
    def forca_bruta(self, senha_para_quebrar, tamanho_maximo=8):
        caracteres = string.ascii_letters + string.digits  # Letras e números
        tempo_inicio = time.time()
        tentativas = 0

        for tamanho in range(1, tamanho_maximo + 1):
            for combinacao in itertools.product(caracteres, repeat=tamanho):
                tentativas += 1
                candidato = ''.join(combinacao)
                print(f'Tentando senha: {candidato}', end='\r')
                if self.criptografa_senha(candidato) == senha_para_quebrar:
                    tempo_gasto = time.time() - tempo_inicio
                    print(f'Senha encontrada: {candidato}, tentativas: {tentativas}, tempo gasto: {tempo_gasto}')
                    return

        print(f'Senha não encontrada, tentativas: {tentativas}, tempo gasto: {time.time() - tempo_inicio}')
        return
