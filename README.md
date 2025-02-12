# Mini Simulador de Sistema de Arquivos

Este é um mini simulador de sistema de arquivos que permite criar e excluir arquivos e diretórios, listar o conteúdo dos diretórios e calcular a fragmentação interna e externa.

## Funcionalidades

- Criar diretórios
- Excluir diretórios
- Criar arquivos
- Excluir arquivos
- Listar diretórios
- Listar arquivos em um diretório
- Calcular fragmentação interna
- Calcular fragmentação externa

## Estrutura do projeto

```
mini-fs-simulator
├── src
│   ├── main.py               # Ponto de entrada da aplicação
│   ├── sistema_arquivos.py   # Gerencia as operações da aplicação
│   ├── diretorio.py          # Objeto Diretório
│   ├── arquivo.py            # Objeto Arquivo
│   └── bloco.py              # Objeto Bloco
├── requirements.txt          # Lista as dependências requeridas no projeto
└── README.md                 # Documentação
```

## Instalação

1. Clonar o repositório:
   ```
   git clone https://github.com/JulianePires/mini-fs-simulator.git
   ```
2. Navegar até o diretório do projeto:
   ```
   cd mini-fs-simulator
   ```
3. Instalar as dependências:
   ```
   pip install -r requirements.txt
   ```

## Uso

1. Executar a aplicação:
   ```
   python src/main.py
   ```
2. Siga as instruções para criar ou excluir arquivos e diretórios, e para listar o conteúdo dos diretórios.

## Comandos de Exemplo

- Criar um diretório: `1`
- Excluir um diretório: `2`
- Criar um arquivo: `3`
- Excluir um arquivo: `4`
- Listar diretórios: `5`
- Listar arquivos em um diretório: `6`
- Calcular fragmentação interna: `7`
- Calcular fragmentação externa: `8`
- Sair: `9`

## Contribuindo

Sinta-se à vontade para enviar issues ou pull requests para melhorias ou correções de bugs.

## Licença

Este projeto está licenciado sob a licença MIT.