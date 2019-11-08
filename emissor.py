import pickle
import public_key
import private_key

class Emissor:
    def __init__(self):
        pass

    # abre o arquivo desejado
    def open_arq(self, path):
        try:
            arq = open(path, 'r', encoding='utf8')
            texto = arq.read()
            arq.close()
            return texto
        except:
            print("erro na leitura do arquivo")
            quit()
    
    # Salva o arquivo desejado
    def save_arq(self, path, text):
        arq = open(path,'w', encoding='utf8')
        arq.write(text)
        arq.close()

    # salva a mensagem do texto claro em uma variável local
    def set_message(self, path):
        self.message = self.open_arq(path)

    # gera uma lista local com as representações numéricas de cada caractere do texto
    def transform_message(self):
        self.base_10_message = []
        for l in self.message:
            self.base_10_message.append(ord(l))

    # lê a chave pública
    def read_public_key(self, path='public/public_key.pickle'):
        self.public_key = pickle.load(open(path,'rb'))

    # realiza a criptografia
    def encryp(self):
        self.C = []
        e = self.public_key.get_e()
        n = self.public_key.get_n()
        
        for M in self.base_10_message:
            self.C.append((M**e)%n)
        
        encrypted_text = ''
        for item in self.C:
            encrypted_text += chr(item)
        
        self.save_arq('public/encrypted_text.txt',encrypted_text)

