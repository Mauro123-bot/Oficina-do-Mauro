from datetime import datetime
# Traz do Python a ferramenta que registra a data e a hora de chegada dos veículos.

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

        if self.esta_vazia():
            # Se não há ninguém na fila, não há quem mostrar.

            return None

        return self.inicio.dado
        # 'self.inicio' é o nó do primeiro da fila.
        # '.dado' abre esse nó e pega o que está guardado dentro dele.


# ============================================================
# Módulo 4 - Controle de Atendimento (Entrada na oficina)
# Regras da oficina usando a nossa Fila genérica do Módulo 3.
# ============================================================

class Atendimento:
    # Guarda os dados de um veículo que chegou à oficina e aguarda um box.

    def __init__(self, placa, nome_cliente, queixa, guincho=False, idoso=False):
        # Construtor. 'guincho=False' e 'idoso=False' são valores padrão,
        # usados quando não informamos nada na hora de criar o atendimento.

        self.placa = placa
        # Placa do veículo, por exemplo "ABC1D23".

        self.nome_cliente = nome_cliente
        # Nome de quem trouxe o veículo.

        self.queixa = queixa
        # Problema relatado pelo cliente, por exemplo "barulho no freio".

        self.guincho = guincho
        # True se o veículo chegou de guincho. Pelo enunciado, tem prioridade máxima.

        self.idoso = idoso
        # True se o cliente tem 60 anos ou mais. Prioridade social da oficina,
        # baseada no Estatuto da Pessoa Idosa (Lei 10.741/2003).

        self.data_hora_chegada = datetime.now()
        # Registra automaticamente a data e a hora exatas da chegada.

    def __str__(self):
        # Método especial do Python. Define como o atendimento aparece num print().

        momento = self.data_hora_chegada.strftime("%d/%m/%Y %H:%M")
        # Transforma a data e a hora num texto no formato dia/mês/ano hora:minuto.

        return f"{self.placa} | {self.nome_cliente} | {self.queixa} | chegada {momento}"
        # Devolve uma linha de texto com os dados principais do atendimento.


class ControleAtendimento:
    # Gerencia a espera dos veículos e a ocupação dos boxes (elevadores).
    # Combinação de estruturas: três Filas trabalhando juntas na mesma operação.

    def __init__(self, total_boxes):
        # Construtor. 'total_boxes' é o número de elevadores da oficina.

        self.total_boxes = total_boxes
        # Guarda quantos boxes a oficina tem no total.

        self.boxes_ocupados = 0
        # Conta quantos boxes estão em uso. A oficina abre com todos livres.

        self.fila_guincho = Fila()
        # Fila 1: veículos trazidos por guincho. São atendidos antes de todos.

        self.fila_idoso = Fila()
        # Fila 2: clientes idosos. São atendidos depois do guincho e antes dos demais.

        self.fila_normal = Fila()
        # Fila 3: demais clientes, por ordem de chegada.

    def tem_box_livre(self):
        # Verifica se existe pelo menos um box desocupado.

        return self.boxes_ocupados < self.total_boxes
        # True se o número de boxes ocupados for menor que o total.

    def registrar_chegada(self, placa, nome_cliente, queixa, guincho=False, idoso=False):
        # Registra a chegada de um veículo e o coloca na fila certa.

        atendimento = Atendimento(placa, nome_cliente, queixa, guincho, idoso)
        # Cria o registro do atendimento com os dados recebidos.

        if guincho:
            # Se veio de guincho, vai para a fila de maior prioridade.

            self.fila_guincho.enfileirar(atendimento)
            print(f"[CHEGADA] {placa} entrou na fila de GUINCHO.")

        elif idoso:
            # Se não veio de guincho, mas o cliente é idoso, vai para a fila de idosos.

            self.fila_idoso.enfileirar(atendimento)
            print(f"[CHEGADA] {placa} entrou na fila PREFERENCIAL (idoso).")

        else:
            # Nos demais casos, vai para a fila normal.

            self.fila_normal.enfileirar(atendimento)
            print(f"[CHEGADA] {placa} entrou na fila NORMAL.")

        if self.tem_box_livre():
            # Se houver box livre no momento da chegada, o veículo já é chamado.

            self.chamar_proximo()

    def proximo_da_vez(self):
        # Mostra quem será o próximo atendido, sem tirá-lo da fila.
        # Aqui usamos o método 'espiar' criado no Módulo 3.

        if not self.fila_guincho.esta_vazia():
            return self.fila_guincho.espiar()
            # Se houver alguém de guincho, ele é o próximo.

        if not self.fila_idoso.esta_vazia():
            return self.fila_idoso.espiar()
            # Senão, se houver idoso esperando, ele é o próximo.

        return self.fila_normal.espiar()
        # Senão, é o primeiro da fila normal. Se ela estiver vazia, devolve None.

    def chamar_proximo(self):
        # Retira o próximo veículo da fila certa e o coloca num box livre.

        if not self.tem_box_livre():
            # Se todos os boxes estiverem ocupados, ninguém pode ser chamado.

            print("[AVISO] Todos os boxes estão ocupados.")
            return None

        if not self.fila_guincho.esta_vazia():
            atendimento = self.fila_guincho.desenfileirar()
            # Prioridade 1: fila de guincho.

        elif not self.fila_idoso.esta_vazia():
            atendimento = self.fila_idoso.desenfileirar()
            # Prioridade 2: fila de idosos.

        elif not self.fila_normal.esta_vazia():
            atendimento = self.fila_normal.desenfileirar()
            # Prioridade 3: fila normal.

        else:
            # Se as três filas estiverem vazias, não há quem chamar.

            print("[AVISO] Nenhum veículo aguardando.")
            return None

        self.boxes_ocupados = self.boxes_ocupados + 1
        # Um box a mais passa a estar ocupado.

        print(f"[BOX] Chamado: {atendimento}")
        print(f"      Boxes ocupados: {self.boxes_ocupados}/{self.total_boxes}")
        # Mostra quem foi chamado e como ficou a ocupação da oficina.

        return atendimento
        # Devolve o atendimento chamado. Na Etapa da OS, ele será usado para abrir a ordem.

    def liberar_box(self):
        # Libera um box quando o serviço termina e chama o próximo automaticamente.

        if self.boxes_ocupados == 0:
            # Não há box ocupado para liberar.

            print("[AVISO] Nenhum box está ocupado.")
            return None

        self.boxes_ocupados = self.boxes_ocupados - 1
        # Um box volta a ficar livre.

        print(f"[BOX] Um box foi liberado. Boxes ocupados: {self.boxes_ocupados}/{self.total_boxes}")

        return self.chamar_proximo()
        # Enunciado, item c. Quando um box fica livre, o sistema indica o próximo.

    def total_em_espera(self):
        # Soma quantos veículos aguardam nas três filas.

        return self.fila_guincho.tamanho + self.fila_idoso.tamanho + self.fila_normal.tamanho


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
    fila.enfileirar("Carro A")
    fila.enfileirar("Carro B")
    fila.enfileirar("Carro C")
    print(f"Testando Fila - Tamanho: {fila.tamanho}")
    print(f"Atendido: {fila.desenfileirar()}")
    print(f"Atendido: {fila.desenfileirar()}")
    print(f"Testando Fila - Tamanho: {fila.tamanho}")
    print(f"Testando Fila - Próximo da fila: {fila.espiar()}")
    print(f"Testando Fila - Tamanho continua: {fila.tamanho}")

    # ---------- Teste do Módulo 4 ----------
    print("\n===== MÓDULO 4: CONTROLE DE ATENDIMENTO =====")

    oficina = ControleAtendimento(total_boxes=2)
    # Cria a oficina com 2 boxes.

    oficina.registrar_chegada("ABC1D23", "Ana", "troca de óleo")
    oficina.registrar_chegada("DEF4G56", "Bruno", "barulho no freio")
    # Os dois primeiros encontram box livre e entram direto.

    oficina.registrar_chegada("GHI7J89", "Carlos", "revisão")
    oficina.registrar_chegada("JKL0M12", "Dona Maria", "luz do painel acesa", idoso=True)
    oficina.registrar_chegada("MNO3P45", "Pedro", "motor não liga", guincho=True)
    # Os boxes estão cheios. Esses três ficam esperando, cada um na sua fila.

    print(f"Veículos em espera: {oficina.total_em_espera()}")
    print(f"Próximo da vez: {oficina.proximo_da_vez()}")
    # Deve mostrar o carro do guincho, mesmo tendo chegado por último.

    oficina.liberar_box()
    # Entra o guincho.

    oficina.liberar_box()
    # Entra a Dona Maria, idosa.

    oficina.liberar_box()
    # Entra o Carlos, da fila normal.

    oficina.liberar_box()
    # Ninguém mais esperando. O box fica livre.
