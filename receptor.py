import random as rd
import string
import pickle
from public_key import Public_key
from private_key import Private_key

class Receptor:
    # inicializa um vetor de primos
    def __init__(self):
        self.primes =  [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,\
                        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,]\
                        # 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, \
                        # 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, \
                        # 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, \
                        # 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, \
                        # 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 2431, 433, \
                        # 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, \
                        # 509, 521, 523, 541, 547] 
    
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

    # seleciona dois primos próximos aleatoriamente
    def select_primes(self):
        index = rd.randint(10,len(self.primes)-1)
        self.p1 = self.primes[index]
        self.p2 = self.primes[index + 1]

    # salva numa variável local o n
    def set_n(self):
        self.n = self.p1*self.p2

    # calcula phi
    def _phi(self):
        return (self.p1-1)*(self.p2-1)

    # salva numa variável local o phi(n)
    def set_phi(self):
        self.phi = self._phi()

    # salva numa variável local o e   (parte da chave publica)
    def set_e(self):
        self.e = self.primes[0]
        self.index_e = 0
        i = 1
        while(self.phi%self.e==0):
            self.index_e += 1
            self.e = self.primes[i]
            i+=1
            if(self.e>=self.phi):
                self.select_primes()
    
    #função de cálculo do inverso modular (a*x = 1mod(m))
    def mod_inverse(self, a, m) : 
        a = a % m
        for x in range(1, m) : 
            if ((a * x) % m == 1) : 
                return x 
        return 1

    # salva numa variável local o d
    def set_d(self):
        self.d = self.mod_inverse(self.e, self.phi)

    # gera as chaves a partir das funções anteriores e as salva em disco
    # uma na pasta pública e outra na privada
    def generate_keys(self):
        self.select_primes()
        self.set_n()
        self.set_phi()
        self.set_e()
        self.set_d()

        self.public_key = Public_key(self.e, self.n)
        self.private_key = Private_key(self.d, self.n)

        with open('C:/Users/paulo/UFMA/Cripto/Trab_2/public/public_key.pickle', 'wb') as f:
            pickle.dump(self.public_key,f, pickle.HIGHEST_PROTOCOL)
        with open('C:/Users/paulo/UFMA/Cripto/Trab_2/receptor/private_key.pickle', 'wb') as f2:
            pickle.dump(self.private_key, f2, pickle.HIGHEST_PROTOCOL)

    # carrega a chave privada
    def load_key(self):
        private_key = pickle.load(open('receptor/private_key.pickle', 'rb'))
        self.d = private_key.get_d()
        self.n = private_key.get_n()

    # realiza a descriptografia
    def depcryp(self):

        encryp_text = self.open_arq('public/encrypted_text.txt')
        decrypted_text = ''
        decrypted_letters = []
    
        for c in encryp_text:
            decrypted_letters.append((ord(c)**self.d)%self.n)
        
        for l in decrypted_letters:
            decrypted_text += chr(l)

        self.save_arq('receptor/decrypted_text.txt', decrypted_text)
