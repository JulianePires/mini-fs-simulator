# main.py

import sys
from sistema_arquivos import SistemaDeArquivos

def main():
    tamanho_memoria = int(input("Digite a quantidade máxima de memória: "))
    tamanho_bloco = int(input("Digite o tamanho do bloco: "))
    fs = SistemaDeArquivos(tamanho_memoria, tamanho_bloco)  # 1MB memory with 64KB blocks
    while True:
        print("\nMini Simulador de Sistema de Arquivos")
        print("1. Criar diretório")
        print("2. Deletar diretório")
        print("3. Criar arquivo")
        print("4. Deletar arquivo")
        print("5. Listar diretórios")
        print("6. Listar arquivos")
        print("7. Calcular fragmentação interna")
        print("8. Calcular fragmentação externa")
        print("9. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Digite o nome do diretório: ")
            fs.criar_diretorio(nome)
        elif opcao == "2":
            nome = input("Digite o nome do diretório: ")
            fs.excluir_diretorio(nome)
        elif opcao == "3":
            nome = input("Digite o nome do arquivo: ")
            tamanho = int(input("Digite o tamanho do arquivo: "))
            dir = input("Digite o diretório: ")
            fs.criar_arquivo(nome, tamanho, dir)
        elif opcao == "4":
            nome = input("Digite o nome do arquivo: ")
            dir = input("Digite o diretório: ")
            fs.excluir_arquivo(nome, dir)
        elif opcao == "5":
            fs.listar_diretorios()
        elif opcao == "6":
            dir = input("Digite o diretório: ")
            fs.listar_arquivos(dir)
        elif opcao == "7":
            fs.calcular_fragmentacao_interna()
        elif opcao == "8":
            fs.calcular_fragmentacao_externa()
        elif opcao == "9":
            sys.exit()
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()