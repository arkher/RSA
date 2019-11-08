from receptor import Receptor
from emissor import Emissor

def clear(n=300):
    for i in range(n):
        print()    

if __name__ == '__main__':

    print(' (1) - Criptografar | (2) Descriptografar | (3) Sair ')
    escolha = int(input())
    
    rec = Receptor()
    emi = Emissor()
    print('gerando as chaves do receptor...')
    rec.generate_keys()

    while(escolha>0 and escolha<3):
        if(escolha==1):
            print('digite a localização do arquivo com o texto claro.') 
            print('ex.:\n./arq_para_criptografar.txt\n./arq_criptografado.txt')
            path = input()
            emi.set_message(path)
            emi.transform_message()
            emi.read_public_key()
            emi.encryp()
            clear()
            print("Arquivo criptografado gerado na pasta pública")
            
        elif(escolha==2): #apresenta erro se nao tiver um texto criptografado antes
            rec.load_key()
            rec.depcryp()
            
            clear()
            print('arquivo de saída salvo!')
        elif(escolha==3):
            clear()
            quit()
        else:
            clear()
            print('opção inválida')
        
        print(' (1) - Criptografar | (2) Descriptografar | (3) Sair ')
        escolha = int(input())
 