from src.application.app import personalizacao,boa_pratica,identificacao

if __name__== '__main__':
     inicia = personalizacao()
     boa_pratica = boa_pratica()
     inicia = personalizacao()

     nome, idade = identificacao()
     print(f"NOME : {nome}\nIDADE : {idade} !")
     if idade >= 18 :
          print(f'Matrícula no curso autorizada !')
     else : 
          print(f'Você é menor de idade!\nTraga o seu responsável para asinatura do contrato!')
     
     

    
