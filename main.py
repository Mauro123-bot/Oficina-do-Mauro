print("Projeto Oficina Mecânica iniciado com sucesso!")

class No:
    # A palavra 'class' serve para iniciar a definição de um novo molde de objeto.
    # 'No' é o nome que escolhemos para essa estrutura (o nosso "tijolo").

    def __init__(self, dado):
        # 'def' indica que estamos criando uma função dentro da classe.
        # '_init_' é o nome padrão do Python para a função construtora.
        # 'self' representa o nó específico que está sendo criado naquele instante.
        # 'dado' é o valor ou objeto que vamos enviar para dentro desse nó.

        self.dado = dado
        # 'self.dado' cria uma caixinha interna no nó para guardar a informação recebida.
        # '= dado' joga o valor que passamos no argumento para dentro dessa caixinha.

        self.proximo = None
         # self.proximo cria um atributo que servirá de ponteiro para o próximo nó.
         # = None define que, inicialmente, este nó não aponta para nenhum outro (está isolado).

if __name__ == "__main__":
     # if _name_ == "_main_": garante que o teste só rode ao executar este arquivo direto.

     no_teste = No("Carro 1")
     # no_teste = No("Carro 1") cria um nó real na memória guardando o texto "Carro 1".

     print(f"Testando Nó - Dado salvo: {no_teste.dado}")
     # print(...) exibe na tela o valor que ficou guardado na caixinha 'dado'.

     print(f"Testando Nó - Próximo: {no_teste.proximo}")
     # print(...) mostra que a caixinha 'proximo' realmente começou vazia (None).

# Módulo 2
class ListaEncadeada:
# 'class' define um novo molde de objeto; 'ListaEncadeada' gerencia a nossa corrente de nós.
    
    def __init__(self):
    # Método construtor executado automaticamente ao instanciar a lista.
    #       
        self.cabeca = None
        # 'self.cabeca' cria o ponteiro principal que aponta para o primeiro nó da lista.
        # '= None' define que a lista nasce vazia, sem nenhum elemento conectado.
        
    def esta_vazia(self):
        # Função para verificar se a lista não possui elementos cadastrados.
        
        return self.cabeca is None
        # Retorna 'True' se o ponteiro da cabeça for None (vazia), ou 'False' caso contrário.

    def adicionar(self, dado):
        # Método para inserir um novo dado (ex: um cliente ou veículo) no final da lista.
        
        novo_no = No(dado)
        # Cria um novo 'No' utilizando o molde que fizemos na Etapa 1, guardando o 'dado' dentro dele.
        
        if self.esta_vazia():
            # Condicional: verifica se a lista está vazia no momento da inserção.
            
            self.cabeca = novo_no
            # Se estiver vazia, o novo nó se torna o primeiro elemento (a cabeça) da lista.
        else:
            # Caso a lista já possua elementos, precisamos caminhar até encontrar o último.
            
            atual = self.cabeca
            # Cria uma variável temporária 'atual' que começa apontando para o primeiro nó.
            
            while atual.proximo is not None:
                # Laço de repetição: continua andando enquanto o nó atual tiver um próximo apontando para alguém.
                
                atual = atual.proximo
                # Move o ponteiro 'atual' para a frente, avançando para o próximo vagão do trem.
                
            atual.proximo = novo_no
            # Quando o laço termina, 'atual' é o último nó; fazemos o 'proximo' dele apontar para o novo nó criado.
        
           