# ============================================================
# Módulo 1 - A classe No (o "tijolo" da lista encadeada)
# ============================================================

class No:
    # A palavra 'class' serve para iniciar a definição de um novo molde de objeto.
    # 'No' é o nome que escolhemos para essa estrutura (o nosso "tijolo").

    def __init__(self, dado):
        # 'def' indica que estamos criando uma função dentro da classe.
        # '__init__' (dois underscores de cada lado) é o nome padrão do Python
        # para a função construtora, executada automaticamente ao criar o objeto.
        # 'self' representa o nó específico que está sendo criado naquele instante.
        # 'dado' é o valor ou objeto que vamos enviar para dentro desse nó.

        self.dado = dado
        # 'self.dado' cria uma caixinha interna no nó para guardar a informação recebida.
        # '= dado' joga o valor que passamos no argumento para dentro dessa caixinha.

        self.proximo = None
        # 'self.proximo' cria um atributo que servirá de ponteiro para o próximo nó.
        # '= None' define que, inicialmente, este nó não aponta para nenhum outro (está isolado).


# ============================================================
# Módulo 2 - A classe ListaEncadeada (a "corrente" de nós)
# ============================================================

class ListaEncadeada:
    # 'class' define um novo molde de objeto.
    # 'ListaEncadeada' gerencia a nossa corrente de nós.

    def __init__(self):
        # Método construtor, executado automaticamente ao criar a lista.

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
        # Cria um novo 'No' usando o molde do Módulo 1, guardando o 'dado' dentro dele.

        if self.esta_vazia():
            # Condicional: verifica se a lista está vazia no momento da inserção.

            self.cabeca = novo_no
            # Se estiver vazia, o novo nó se torna o primeiro elemento (a cabeça) da lista.
        else:
            # Caso a lista já possua elementos, precisamos caminhar até encontrar o último.

            atual = self.cabeca
            # Cria uma variável temporária 'atual' que começa apontando para o primeiro nó.

            while atual.proximo is not None:
                # Laço de repetição: continua andando enquanto o nó atual tiver um próximo.

                atual = atual.proximo
                # Move o ponteiro 'atual' para a frente, avançando para o próximo vagão do trem.

            atual.proximo = novo_no
            # Quando o laço termina, 'atual' é o último nó.
            # Fazemos o 'proximo' dele apontar para o novo nó criado.

    def exibir(self):
        # Método para mostrar na tela todos os dados guardados na lista, do primeiro ao último.

        if self.esta_vazia():
            # Se a lista não tiver nenhum elemento, avisamos o usuário.

            print("A lista está vazia.")
            return
            # 'return' encerra a função aqui, sem executar o resto.

        atual = self.cabeca
        # Começamos a caminhada pelo primeiro nó da lista.

        while atual is not None:
            # Repete enquanto ainda houver um nó para visitar.

            print(atual.dado)
            # Mostra o dado guardado no nó atual.

            atual = atual.proximo
            # Avança para o próximo nó. Quando chegar ao fim, 'atual' vira None e o laço para.


# ============================================================
# Módulo 3 - A classe Fila (primeiro a entrar, primeiro a sair)
# ============================================================

class Fila:
    # 'Fila' organiza os nós por ordem de chegada (FIFO: First In, First Out).

    def __init__(self):
        # Construtor executado automaticamente ao criar uma nova fila.

        self.inicio = None
        # 'self.inicio' aponta para o primeiro da fila, que é o próximo a ser atendido.

        self.fim = None
        # 'self.fim' aponta para o último da fila, onde os novos chegam.

        self.tamanho = 0
        # 'self.tamanho' conta quantos elementos estão esperando na fila.

    def esta_vazia(self):
        # Verifica se não há ninguém na fila.

        return self.inicio is None
        # Retorna True se não houver ninguém no início da fila.

    def enfileirar(self, dado):
        # Coloca um novo dado no FIM da fila.

        novo_no = No(dado)
        # Cria um novo nó com o mesmo molde da Etapa 1.

        if self.esta_vazia():
            # Se a fila estiver vazia, o novo nó é ao mesmo tempo o primeiro e o último.

            self.inicio = novo_no
            self.fim = novo_no
        else:
            # Se já houver gente, o último atual passa a apontar para o novo nó.

            self.fim.proximo = novo_no
            # Liga o antigo último ao novo nó.

            self.fim = novo_no
            # Atualiza o ponteiro 'fim' para o novo último da fila.

        self.tamanho = self.tamanho + 1
        # Aumenta o contador em 1.

    def desenfileirar(self):
        # Retira e devolve o dado do INÍCIO da fila, ou seja, quem chegou primeiro.

        if self.esta_vazia():
            # Se não há ninguém, não há o que retirar.

            return None

        no_que_sai = self.inicio
        # Guarda o primeiro nó numa variável antes de desligá-lo da fila.

        self.inicio = no_que_sai.proximo
        # O segundo da fila passa a ser o primeiro.

        if self.inicio is None:
            # Se a fila ficou vazia, o 'fim' também precisa voltar a ser None.

            self.fim = None

        self.tamanho = self.tamanho - 1
        # Diminui o contador em 1.

        return no_que_sai.dado
        # Devolve o dado de quem saiu da fila.

    def espiar(self):
        # Mostra quem é o próximo da fila, sem retirá-lo. 
         # Passo 2. Tratar a fila vazia.
        if self.esta_vazia():
            # Se não há ninguém na fila, não há quem mostrar.

            return None

        # Passo 3. Devolver o dado do início.
        return self.inicio.dado
        # 'self.inicio' é o nó do primeiro da fila.
        # '.dado' abre esse nó e pega o que está guardado dentro dele.

# ============================================================
# Área de testes
# Fica sempre no FINAL do arquivo, depois de todas as classes.
# ============================================================

if __name__ == "__main__":
    # 'if __name__ == "__main__":' garante que os testes só rodem
    # quando executamos este arquivo diretamente (e não quando ele é importado).

    print("Projeto Oficina Mecânica iniciado com sucesso!")
    # Mensagem inicial, agora dentro do bloco de testes.

    # ---------- Teste do Módulo 1 ----------
    print("\n===== MÓDULO 1: NÓ =====")

    no_teste = No("Carro 1")
    # Cria um nó real na memória guardando o texto "Carro 1".

    print(f"Testando Nó - Dado salvo: {no_teste.dado}")
    # Exibe na tela o valor que ficou guardado na caixinha 'dado'.

    print(f"Testando Nó - Próximo: {no_teste.proximo}")
    # Mostra que a caixinha 'proximo' realmente começou vazia (None).

    # ---------- Teste do Módulo 2 ----------
    print("\n===== MÓDULO 2: LISTA ENCADEADA =====")

    lista = ListaEncadeada()
    # Cria uma lista encadeada nova, que começa vazia.

    print(f"Testando Lista - Está vazia? {lista.esta_vazia()}")
    # Deve mostrar True, pois ainda não adicionamos nada.

    lista.adicionar("Carro 1")
    lista.adicionar("Carro 2")
    lista.adicionar("Carro 3")
    # Adiciona três carros, um depois do outro, no final da lista.

    print(f"Testando Lista - Está vazia? {lista.esta_vazia()}")
    # Agora deve mostrar False.

    print("Testando Lista - Conteúdo:")
    lista.exibir()
    # Mostra os três carros na ordem em que foram adicionados.

    # ---------- Teste do Módulo 3 ----------
    print("\n===== MÓDULO 3: FILA =====")

    fila = Fila()

    fila = Fila()
    fila.enfileirar("Carro A")
    fila.enfileirar("Carro B")
    fila.enfileirar("Carro C")
    print(f"Testando Fila - Tamanho: {fila.tamanho}")
    print(f"Atendido: {fila.desenfileirar()}")
    print(f"Atendido: {fila.desenfileirar()}")
    print(f"Testando Fila - Tamanho: {fila.tamanho}")
    print(f"Testando Fila - Próximo da fila: {fila.espiar()}")
    print(f"Testando Fila - Tamanho continua: {fila.tamanho}")