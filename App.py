import requests
import json
import hashlib

# Função de desencriptação:
#   Primeiro verifico os caracters especiais, adiciono na string decifrada que será retornada;
#   Segundo eu chamo a função decryptor que fará a desencriptação de cada letra e retorna.

def decrypt(n,text):
    decryptedText = ''
    for x in text:
        if(special_characters.__contains__(x)):
            decryptedText += x
        else:
            decryptedText += decryptor(n,x)
    return decryptedText

def decryptor(n,c):
    i = alphabet.index(c)
    count = i - n
    if(count<0):
        count = 26 + count
        return alphabet[count]
    else:
        return alphabet[count]

# Função de resumo encriptado:
#   Utilizo a biblioteca hashlib que faz o trabalho inteiro;
#   Na versão python 3.0 é necessário fazer o encode do texto que será encriptado.
def decrypt_resume(text):
    resume = hashlib.sha1(text.encode('utf-8')).hexdigest()
    return resume

if __name__ == "__main__":
    special_characters = [' ','.',',','!','*','+','-','/','@','#','$','%','&',';','0','1','2','3','4','5','6','7','8','9']
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    #Requisição para receber o arquivo json
    payload = {'token':'seu_token'}
    response = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?', params=payload)

    #Transformando o arquivo json para um dicionário python
    answer = response.content
    dic = json.loads(answer)

    #Chamada das funções e preenchimento dos campos decifrado e resumo
    n = dic['numero_casas']
    encryptedText = dic['cifrado']
    dic['decifrado'] = decrypt(n, dic['cifrado'])
    dic['resumo_criptografico'] = decrypt_resume(dic['decifrado'])
    
    #Preparação do arquivo multpart/form-data
    with open('answer.json', 'w', encoding='UTF-8') as arq:
        json.dump(dic, arq)
    
    answer = {'answer': open('answer.json')}

    #Envio do arquivo e print do valor atingido no desafio
    response = requests.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?', params=payload, files=answer)
    print(response.text) #100%
