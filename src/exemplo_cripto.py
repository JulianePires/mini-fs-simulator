from criptografia import Criptografia

crip = Criptografia()

senha = input("Digite a senha original para criptografar (máx. 8 caracteres): ")
if len(senha) > 8:
    print("Erro: A senha deve ter no máximo 8 caracteres.")
else:
    senha_criptografada = crip.criptografa_senha(senha)
    print("Hash da senha:", senha_criptografada)

    print("\nTentando quebrar a senha...")
    crip.forca_bruta(senha_criptografada, 8)