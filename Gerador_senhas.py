# Gerador de senhas utilizando o python

import secrets
import string

def gerar_senha(tamanho):
    caracter = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(caracter) for i in range(tamanho))
    return senha
    
tamanho_senha = 12 # Você pode mudar o tamanho para qualquer uma que queira
nova_senha = gerar_senha(tamanho_senha)
print(f'Sua senha nova é: {nova_senha}')
