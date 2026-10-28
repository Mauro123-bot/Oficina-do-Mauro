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

    def remover(self, dado):
        # Remove da lista o primeiro nó que guarda o 'dado' informado.
        # Devolve True se conseguiu remover, ou False se o dado não estava na lista.

        if self.esta_vazia():
            # Lista vazia, não há o que remover.

            return False

        if self.cabeca.dado == dado:
            # Caso especial: o dado está logo no primeiro nó.

            self.cabeca = self.cabeca.proximo
            # A cabeça passa a ser o segundo nó. O primeiro fica desligado da lista.

            return True

        anterior = self.cabeca
        # 'anterior' guarda o nó de trás, porque é ele que precisa ser religado.

        atual = self.cabeca.proximo
        # 'atual' é o nó que estamos examinando.

        while atual is not None:
            # Percorre a lista até o fim.

            if atual.dado == dado:
                # Achamos o nó a remover.

                anterior.proximo = atual.proximo
                # O nó de trás "pula" o atual e passa a apontar para o seguinte.
                # Assim o nó atual sai da corrente.

                return True

            anterior = atual
            atual = atual.proximo
            # Os dois ponteiros andam um passo para a frente.

        return False
        # Chegamos ao fim sem encontrar o dado.



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
# Módulo 5 - Controle de Clientes e Veículos
# Combinação de estruturas: Lista de clientes, cada um com uma Lista de veículos.
# ============================================================

class Veiculo:
    # Guarda os dados de um veículo.

    def __init__(self, placa, modelo, marca, ano):
        # Construtor do veículo.

        self.placa = placa
        # Placa, por exemplo "ABC1D23".

        self.modelo = modelo
        # Modelo, por exemplo "Onix".

        self.marca = marca
        # Marca, por exemplo "Chevrolet".

        self.ano = ano
        # Ano de fabricação, por exemplo 2020.

    def __str__(self):
        # Define como o veículo aparece num print().

        return f"{self.placa} - {self.marca} {self.modelo} {self.ano}"


class Cliente:
    # Guarda os dados de um cliente e a lista dos seus veículos.

    def __init__(self, nome, cpf, telefone):
        # Construtor do cliente.

        self.nome = nome
        # Nome completo do cliente.

        self.cpf = cpf
        # CPF, usado para buscar o cliente.

        self.telefone = telefone
        # Telefone de contato.

        self.veiculos = ListaEncadeada()
        # Cada cliente tem a SUA PRÓPRIA lista de veículos.
        # Como é uma lista encadeada, não há limite de quantos veículos ele pode ter.

    def adicionar_veiculo(self, veiculo):
        # Coloca um veículo na lista deste cliente.

        self.veiculos.adicionar(veiculo)

    def __str__(self):
        # Define como o cliente aparece num print().

        return f"{self.nome} | CPF {self.cpf} | Tel {self.telefone}"


class CadastroClientes:
    # Regras da oficina para cadastrar, buscar e remover clientes e veículos.

    def __init__(self):
        # Construtor do cadastro.

        self.clientes = ListaEncadeada()
        # Lista principal com todos os clientes da oficina.

    def buscar_por_cpf(self, cpf):
        # Procura um cliente pelo CPF. Devolve o cliente, ou None se não achar.

        atual = self.clientes.cabeca
        # Começa pelo primeiro cliente da lista.

        while atual is not None:
            # Percorre todos os clientes.

            if atual.dado.cpf == cpf:
                # 'atual.dado' é o objeto Cliente guardado no nó.

                return atual.dado
                # Achou. Devolve o cliente.

            atual = atual.proximo
            # Passa para o próximo cliente.

        return None
        # Percorreu tudo e não achou.

    def buscar_por_placa(self, placa):
        # Procura um veículo pela placa, percorrendo AS DUAS listas.
        # Devolve dois valores, o cliente dono e o veículo, ou None, None se não achar.

        atual_cliente = self.clientes.cabeca
        # Começa pelo primeiro cliente.

        while atual_cliente is not None:
            # Laço de fora: anda pela lista de clientes.

            cliente = atual_cliente.dado
            atual_veiculo = cliente.veiculos.cabeca
            # Para cada cliente, começa pelo primeiro veículo dele.

            while atual_veiculo is not None:
                # Laço de dentro: anda pela lista de veículos desse cliente.

                if atual_veiculo.dado.placa == placa:
                    return cliente, atual_veiculo.dado
                    # Achou. Devolve o dono e o veículo.

                atual_veiculo = atual_veiculo.proximo
                # Próximo veículo do mesmo cliente.

            atual_cliente = atual_cliente.proximo
            # Terminou os veículos deste cliente. Passa para o próximo cliente.

        return None, None
        # Percorreu todos os clientes e veículos e não achou a placa.

    def cadastrar_cliente(self, nome, cpf, telefone):
        # Cadastra um novo cliente, desde que o CPF ainda não exista.

        if self.buscar_por_cpf(cpf) is not None:
            # Evita cadastrar o mesmo CPF duas vezes.

            print(f"[AVISO] CPF {cpf} já cadastrado.")
            return None

        cliente = Cliente(nome, cpf, telefone)
        self.clientes.adicionar(cliente)
        # Cria o cliente e o coloca no final da lista.

        print(f"[CADASTRO] Cliente cadastrado: {cliente}")
        return cliente

    def cadastrar_veiculo(self, cpf, placa, modelo, marca, ano):
        # Cadastra um veículo para um cliente que já existe.

        cliente = self.buscar_por_cpf(cpf)
        # Primeiro, encontra o dono pelo CPF.

        if cliente is None:
            print(f"[AVISO] Cliente com CPF {cpf} não encontrado.")
            return None

        dono, veiculo_existente = self.buscar_por_placa(placa)
        # Verifica se essa placa já está cadastrada em algum cliente.

        if veiculo_existente is not None:
            print(f"[AVISO] Placa {placa} já cadastrada para {dono.nome}.")
            return None

        veiculo = Veiculo(placa, modelo, marca, ano)
        cliente.adicionar_veiculo(veiculo)
        # Cria o veículo e o coloca na lista do cliente.

        print(f"[CADASTRO] Veículo {veiculo} cadastrado para {cliente.nome}.")
        return veiculo

    def remover_cliente(self, cpf):
        # Remove um cliente e, junto com ele, toda a sua lista de veículos.

        cliente = self.buscar_por_cpf(cpf)

        if cliente is None:
            print(f"[AVISO] Cliente com CPF {cpf} não encontrado.")
            return False

        self.clientes.remover(cliente)
        # Usa o método 'remover' da ListaEncadeada genérica.

        print(f"[REMOÇÃO] Cliente {cliente.nome} removido.")
        return True

    def remover_veiculo(self, placa):
        # Remove um veículo da lista do seu dono.

        dono, veiculo = self.buscar_por_placa(placa)

        if veiculo is None:
            print(f"[AVISO] Placa {placa} não encontrada.")
            return False

        dono.veiculos.remover(veiculo)
        # Remove o veículo da lista de veículos do dono.

        print(f"[REMOÇÃO] Veículo {placa} removido de {dono.nome}.")
        return True

    def exibir(self):
        # Mostra todos os clientes e, abaixo de cada um, os seus veículos.

        if self.clientes.esta_vazia():
            print("Nenhum cliente cadastrado.")
            return

        atual_cliente = self.clientes.cabeca

        while atual_cliente is not None:
            cliente = atual_cliente.dado
            print(cliente)
            # Mostra o cliente.

            if cliente.veiculos.esta_vazia():
                print("    (sem veículos)")

            atual_veiculo = cliente.veiculos.cabeca

            while atual_veiculo is not None:
                print(f"    {atual_veiculo.dado}")
                # Mostra cada veículo com recuo, para ficar abaixo do dono.

                atual_veiculo = atual_veiculo.proximo

            atual_cliente = atual_cliente.proximo


# ============================================================
# Módulo 6 - Árvore de Diagnóstico (árvore N-ária)
# ============================================================

class NoArvore:
    # Cada nó da árvore guarda um componente do veículo.

    def __init__(self, texto, codigo=None):
        # Construtor executado ao criar um novo nó da árvore.

        self.texto = texto
        # 'self.texto' é o nome do componente, por exemplo "Motor" ou "Vela".

        self.codigo = codigo
        # Código da peça. Fica None quando o nó é um sistema, como "Motor".

        self.estado = "OK"
        # Todo componente começa OK. O mecânico marca "Com defeito" no diagnóstico.

        self.primeiro_filho = None
        # Aponta para o primeiro filho deste nó. Começa vazio.

        self.proximo_irmao = None
        # Aponta para o próximo irmão, que é outro filho do mesmo pai.
        # Assim, os filhos de um nó formam uma lista encadeada, sem usar list do Python.

class ArvoreDiagnostico:
    # Árvore N-ária: cada nó pode ter quantos filhos precisar.

    def __init__(self, texto_raiz):
        # Cria a árvore já com a raiz, que é o veículo.

        self.raiz = NoArvore(texto_raiz)
        # 'self.raiz' é o nó do topo. Todos os outros descendem dele.

    def buscar(self, texto, no=None):
        # Procura um nó pelo texto, percorrendo a árvore em pré-ordem.

        if no is None:
            no = self.raiz
            # Na primeira chamada, a busca começa pela raiz.

        if no.texto == texto:
            return no
            # Achou. Devolve o nó encontrado.

        filho = no.primeiro_filho
        # Começa pelo primeiro filho do nó atual.

        while filho is not None:
            # Percorre todos os filhos, um irmão de cada vez.

            encontrado = self.buscar(texto, filho)
            # Chamada recursiva. Procura dentro do galho desse filho.

            if encontrado is not None:
                return encontrado
                # Se achou no galho, devolve sem continuar procurando.

            filho = filho.proximo_irmao
            # Passa para o próximo irmão.

        return None
        # Percorreu tudo e não achou.

    def adicionar(self, texto_pai, texto_filho, codigo=None):
        # Pendura um novo nó embaixo do nó que tem o texto 'texto_pai'.
        # 'codigo' só é informado quando o novo nó é uma peça.

        pai = self.buscar(texto_pai)
        # Primeiro localiza o pai na árvore.

        if pai is None:
            print(f"[AVISO] Não encontrei '{texto_pai}' na árvore.")
            return
            # Sem pai, não há onde pendurar o novo nó.

        novo = NoArvore(texto_filho, codigo)
        # Cria o nó novo.

        if pai.primeiro_filho is None:
            pai.primeiro_filho = novo
            # Se o pai ainda não tem filhos, o novo vira o primeiro.

        else:
            atual = pai.primeiro_filho
            # Senão, anda pelos irmãos até o último.

            while atual.proximo_irmao is not None:
                atual = atual.proximo_irmao

            atual.proximo_irmao = novo
            # O novo entra no fim da fila de irmãos, mantendo a ordem de cadastro.

    def exibir_pre_ordem(self, no=None, nivel=0):
        # Pré-ordem: primeiro mostra o nó, depois os filhos, da esquerda para a direita.

        if no is None:
            no = self.raiz

        if no.codigo is None:
            print("    " * nivel + f"- {no.texto} [{no.estado}]")
        else:
            print("    " * nivel + f"- {no.texto} (cód. {no.codigo}) [{no.estado}]")
        # O recuo cresce com o nível, para mostrar a hierarquia na tela.
        # Peças aparecem com o código. Sistemas aparecem só com o nome.

        filho = no.primeiro_filho

        while filho is not None:
            self.exibir_pre_ordem(filho, nivel + 1)
            # Chamada recursiva. Cada filho é exibido um nível mais para dentro.

            filho = filho.proximo_irmao

    def diagnosticos_possiveis(self, componente):
        # Mostra as partes de um componente, ou seja, os filhos daquele nó.

        no = self.buscar(componente)

        if no is None:
            print(f"[AVISO] Componente '{componente}' não cadastrado.")
            return

        filho = no.primeiro_filho

        if filho is None:
            print(f"'{componente}' é uma peça, não tem subcomponentes.")
            return
            # Nó sem filhos é uma folha, o fim do caminho.

        print(f"Componentes de '{componente}':")

        while filho is not None:
            print(f"    {filho.texto}")
            filho = filho.proximo_irmao

    def marcar_defeito(self, texto):
        # O mecânico marca um componente como defeituoso durante o diagnóstico.

        no = self.buscar(texto)

        if no is None:
            print(f"[AVISO] Componente '{texto}' não encontrado.")
            return

        no.estado = "Com defeito"
        print(f"[DIAGNÓSTICO] {texto} marcado como Com defeito.")

    def pecas_com_defeito(self, no=None, resultado=None):
        # Percorre a árvore em pré-ordem e junta numa ListaEncadeada
        # as peças com defeito. Essa lista vai alimentar a OS depois.

        if no is None:
            no = self.raiz
            resultado = ListaEncadeada()
            # Só na primeira chamada: começa pela raiz e cria a lista vazia.

        if no.estado == "Com defeito" and no.codigo is not None:
            resultado.adicionar(no)
            # Só entram peças, ou seja, nós que têm código.

        filho = no.primeiro_filho
        while filho is not None:
            self.pecas_com_defeito(filho, resultado)
            # Chamada recursiva. A mesma lista é passada para todos os galhos.

            filho = filho.proximo_irmao

        return resultado
   
# ============================================================
# Módulo 7 - Controle de Estoque de Peças
# Combinação: Lista de produtos, cada um contendo uma Fila de lotes
# ============================================================

class Lote:
    # Guarda os dados de uma compra de um produto.

    def __init__(self, quantidade, fornecedor, preco_compra, preco_venda, data_compra, validade):
        self.quantidade = quantidade
        self.fornecedor = fornecedor
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = datetime.strptime(data_compra, "%d/%m/%Y")
        # Converte o texto "dd/mm/aaaa" em data de verdade.

        if validade is None:
            self.validade = None
            # Produtos como parafusos não vencem.
        else:
            self.validade = datetime.strptime(validade, "%d/%m/%Y")

    def esta_vencido(self, hoje):
        # Devolve True se o lote tem validade e ela já passou.

        if self.validade is None:
            return False
        return self.validade < hoje

    def __str__(self):
        # Define como o lote aparece quando usamos print.

        if self.validade is None:
            texto_validade = "sem validade"
        else:
            texto_validade = "validade " + self.validade.strftime("%d/%m/%Y")

        return (f"{self.quantidade} un. | compra {self.data_compra.strftime('%d/%m/%Y')} | "
                f"{self.fornecedor} | custo R$ {self.preco_compra:.2f} | "
                f"venda R$ {self.preco_venda:.2f} | {texto_validade}")


class Produto:
    # Guarda os dados fixos de um produto e a sua fila de lotes.

    def __init__(self, codigo, nome, minimo, descarte):
        self.codigo = codigo
        self.nome = nome
        self.minimo = minimo
        self.descarte = descarte
        # 'descarte' é o destino ambiental correto do produto vencido.

        self.lotes = Fila()
        # Cada produto tem a sua própria fila de lotes.
        # O lote comprado primeiro é o primeiro a sair.

    def total(self):
        # Percorre a fila somando a quantidade de todos os lotes.

        soma = 0
        atual = self.lotes.inicio
        while atual is not None:
            soma = soma + atual.dado.quantidade
            atual = atual.proximo
        return soma


class Perda:
    # Registra um lote descartado por vencimento.

    def __init__(self, produto, lote):
        self.produto = produto
        self.lote = lote


class Estoque:
    # Regras do estoque da oficina.
    # Usa a ListaEncadeada para os produtos e a Fila de cada produto para os lotes.

    def __init__(self):
        self.produtos = ListaEncadeada()
        # Lista com todos os produtos cadastrados.

        self.perdas = ListaEncadeada()
        # Lista com os lotes descartados por vencimento.

    def buscar_produto(self, codigo):
        # Percorre a lista de produtos até achar o código.
        # Devolve o produto, ou None se ele não existir.

        atual = self.produtos.cabeca
        while atual is not None:
            if atual.dado.codigo == codigo:
                return atual.dado
            atual = atual.proximo
        return None

    def cadastrar_produto(self, codigo, nome, minimo, descarte):
        if self.buscar_produto(codigo) is not None:
            print(f"Aviso: o código {codigo} já está cadastrado. Produto não incluído.")
            return

        self.produtos.adicionar(Produto(codigo, nome, minimo, descarte))
        print(f"Produto {codigo} - {nome} cadastrado.")

    def entrada_lote(self, codigo, quantidade, fornecedor, preco_compra, preco_venda,
                     data_compra, validade=None):
        # 'validade=None' permite cadastrar produtos sem validade, como parafusos.

        produto = self.buscar_produto(codigo)
        if produto is None:
            print(f"Aviso: produto {codigo} não cadastrado.")
            return

        lote = Lote(quantidade, fornecedor, preco_compra, preco_venda, data_compra, validade)
        produto.lotes.enfileirar(lote)
        # O novo lote entra no fim da fila do produto.

        print(f"Lote de {quantidade} un. de {codigo} registrado.")

    def descartar_vencidos(self, data_hoje):
        hoje = datetime.strptime(data_hoje, "%d/%m/%Y")

        atual = self.produtos.cabeca
        while atual is not None:
            produto = atual.dado
            quantidade_de_lotes = produto.lotes.tamanho

            for i in range(quantidade_de_lotes):
                # Cada lote sai da fila uma vez.
                # Se estiver vencido, vira perda. Se não, volta para o fim da fila.
                # Como todos dão uma volta completa, a ordem original se mantém.

                lote = produto.lotes.desenfileirar()

                if lote.esta_vencido(hoje):
                    self.perdas.adicionar(Perda(produto, lote))
                    print(f"Descartado: {lote.quantidade} un. de {produto.codigo}, "
                          f"vencido em {lote.validade.strftime('%d/%m/%Y')}. "
                          f"Destino: {produto.descarte}.")
                else:
                    produto.lotes.enfileirar(lote)

            atual = atual.proximo

    def _consumir(self, produto, quantidade):
        # Tira a quantidade pedida dos lotes mais antigos.
        # Devolve o valor de venda das unidades retiradas.

        falta = quantidade
        valor = 0

        while falta > 0:
            lote = produto.lotes.espiar()
            # Olha o lote mais antigo, sem tirá-lo da fila.

            if lote.quantidade <= falta:
                # O lote acaba inteiro e sai da fila.
                falta = falta - lote.quantidade
                valor = valor + lote.quantidade * lote.preco_venda
                produto.lotes.desenfileirar()
            else:
                # O lote cobre o que falta e continua na fila.
                lote.quantidade = lote.quantidade - falta
                valor = valor + falta * lote.preco_venda
                falta = 0

        return valor

    def verificar_minimo(self, produto):
        if produto.total() < produto.minimo:
            print(f"ALERTA: {produto.codigo} está com {produto.total()} un., "
                  f"abaixo do mínimo de {produto.minimo}. Repor estoque.")

    def retirar(self, codigo, quantidade):
        # Usado na baixa de peças da OS. Devolve o valor de venda das peças.

        produto = self.buscar_produto(codigo)
        if produto is None:
            print(f"Aviso: produto {codigo} não cadastrado.")
            return 0

        if quantidade > produto.total():
            print(f"Aviso: só há {produto.total()} un. de {codigo}. "
                  f"Retirada de {quantidade} não realizada.")
            return 0

        valor = self._consumir(produto, quantidade)
        print(f"Retiradas {quantidade} un. de {codigo}. Valor de venda: R$ {valor:.2f}")
        self.verificar_minimo(produto)
        return valor

    def ajustar_quantidade(self, codigo, quantidade_contada):
        # Ajuste de inventário: corrige o estoque pela contagem física.

        produto = self.buscar_produto(codigo)
        if produto is None:
            print(f"Aviso: produto {codigo} não cadastrado.")
            return

        diferenca = quantidade_contada - produto.total()

        if diferenca == 0:
            print(f"Ajuste de {codigo}: contagem confere com o sistema.")
        elif diferenca < 0:
            # Faltam itens: tira a diferença dos lotes mais antigos.
            self._consumir(produto, -diferenca)
            print(f"Ajuste de {codigo}: {-diferenca} un. a menos. Total agora: {produto.total()}.")
        else:
            # Sobram itens: soma a diferença no lote mais recente.
            if produto.lotes.esta_vazia():
                print(f"Aviso: {codigo} não tem lotes. Use entrada_lote para registrar a compra.")
                return
            produto.lotes.fim.dado.quantidade = produto.lotes.fim.dado.quantidade + diferenca
            print(f"Ajuste de {codigo}: {diferenca} un. a mais. Total agora: {produto.total()}.")

        self.verificar_minimo(produto)

    def exibir(self):
        atual = self.produtos.cabeca
        while atual is not None:
            produto = atual.dado
            print(f"{produto.codigo} - {produto.nome}: {produto.total()} un. "
                  f"(mínimo {produto.minimo})")

            no_lote = produto.lotes.inicio
            while no_lote is not None:
                print("    lote:", no_lote.dado)
                no_lote = no_lote.proximo

            atual = atual.proximo

    def exibir_perdas(self):
        if self.perdas.esta_vazia():
            print("Nenhuma perda registrada.")
            return

        atual = self.perdas.cabeca
        while atual is not None:
            perda = atual.dado
            print(f"{perda.produto.codigo} - {perda.produto.nome}: "
                  f"{perda.lote.quantidade} un., "
                  f"vencido em {perda.lote.validade.strftime('%d/%m/%Y')}. "
                  f"Destino: {perda.produto.descarte}")
            atual = atual.proximo





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

    # ---------- Teste do Módulo 5 ----------
    print("\n===== MÓDULO 5: CLIENTES E VEÍCULOS =====")

    cadastro = CadastroClientes()
    # Cria o cadastro da oficina, começando vazio.

    cadastro.cadastrar_cliente("Ana Souza", "111.111.111-11", "(19) 99999-1111")
    cadastro.cadastrar_cliente("Bruno Lima", "222.222.222-22", "(19) 99999-2222")
    cadastro.cadastrar_cliente("Ana Repetida", "111.111.111-11", "(19) 90000-0000")
    # O terceiro deve dar aviso, porque o CPF já existe.

    cadastro.cadastrar_veiculo("111.111.111-11", "ABC1D23", "Onix", "Chevrolet", 2020)
    cadastro.cadastrar_veiculo("111.111.111-11", "XYZ9K87", "HB20", "Hyundai", 2018)
    cadastro.cadastrar_veiculo("222.222.222-22", "DEF4G56", "Gol", "Volkswagen", 2015)
    # A Ana tem dois veículos. O Bruno tem um.

    print("\nClientes cadastrados:")
    cadastro.exibir()

    print("\nBusca por CPF 222.222.222-22:")
    print(cadastro.buscar_por_cpf("222.222.222-22"))

    print("\nBusca pela placa XYZ9K87:")
    dono, veiculo = cadastro.buscar_por_placa("XYZ9K87")
    print(f"Veículo {veiculo} pertence a {dono.nome}")
    # A busca percorre a lista de clientes e, dentro de cada um, a lista de veículos.

    print()
    cadastro.remover_veiculo("ABC1D23")
    cadastro.remover_cliente("222.222.222-22")

    print("\nClientes após as remoções:")
    cadastro.exibir()

        # ---------- Teste do Módulo 6 ----------
    print("\n===== MÓDULO 6: ÁRVORE DE COMPONENTES =====")

    arvore = ArvoreDiagnostico("Veículo")

    arvore.adicionar("Veículo", "Motor")
    arvore.adicionar("Veículo", "Freios")
    arvore.adicionar("Veículo", "Suspensão")
    # Primeiro nível. Os sistemas do veículo.

    arvore.adicionar("Motor", "Sistema de ignição")
    arvore.adicionar("Sistema de ignição", "Vela", "VL01")
    arvore.adicionar("Sistema de ignição", "Bobina", "BB01")
    arvore.adicionar("Motor", "Correia dentada", "CD01")
    arvore.adicionar("Freios", "Pastilha dianteira", "PF01")
    arvore.adicionar("Freios", "Disco dianteiro", "DD01")
    arvore.adicionar("Suspensão", "Amortecedor", "AM01")
    arvore.adicionar("Suspensão", "Bandeja", "BD01")
    # Subconjuntos e peças. Só as peças recebem código.

    arvore.adicionar("Câmbio", "Embreagem", "EM01")
    # Deve dar aviso, porque "Câmbio" não existe na árvore.

    print("\nÁrvore antes do diagnóstico:")
    arvore.exibir_pre_ordem()

    print()
    arvore.marcar_defeito("Pastilha dianteira")
    arvore.marcar_defeito("Vela")
    arvore.marcar_defeito("Turbo")
    # O último deve dar aviso, porque "Turbo" não existe.

    print("\nÁrvore depois do diagnóstico:")
    arvore.exibir_pre_ordem()

    print("\nPeças a trocar:")
    defeitos = arvore.pecas_com_defeito()
    atual = defeitos.cabeca
    while atual is not None:
        print(f"    {atual.dado.texto} (cód. {atual.dado.codigo})")
        atual = atual.proximo

    print()
    arvore.diagnosticos_possiveis("Freios")
    arvore.diagnosticos_possiveis("Vela")
    
    # ---------- Teste do Módulo 7 ----------

    print("\n===== MÓDULO 7: ESTOQUE COM LOTES E DESCARTE =====")

    estoque = Estoque()

    estoque.cadastrar_produto("OL01", "Óleo 5W30 (litro)", 5, "rerrefino, CONAMA 362/2005")
    estoque.cadastrar_produto("PF01", "Pastilha de freio (jogo)", 2, "coleta de resíduo metálico")
    estoque.cadastrar_produto("PA01", "Parafuso de roda", 10, "reciclagem de metal")
    estoque.cadastrar_produto("OL01", "Óleo repetido", 1, "-")
    # O último deve dar aviso, porque o código OL01 já existe.

    estoque.entrada_lote("OL01", 4, "Lubrax", 30.00, 45.00, "10/03/2026", "10/09/2026")
    estoque.entrada_lote("OL01", 10, "Mobil", 32.00, 48.00, "15/09/2026", "15/03/2027")
    estoque.entrada_lote("PF01", 6, "Bosch", 80.00, 130.00, "01/10/2026", "31/12/2030")
    estoque.entrada_lote("PA01", 50, "Ciser", 1.50, 3.00, "05/10/2026")
    # O primeiro lote de óleo já está vencido. O parafuso não tem validade.

    print("\nEstoque inicial:")
    estoque.exibir()

    print()
    estoque.descartar_vencidos("28/10/2026")

    print()
    estoque.retirar("OL01", 4)
    estoque.retirar("PF01", 5)
    # Sobra 1 pastilha, abaixo do mínimo de 2, e dispara o alerta.

    estoque.retirar("PF01", 10)
    # Deve avisar que não há pastilhas suficientes.

    print()
    estoque.ajustar_quantidade("PA01", 47)
    # Na contagem física faltaram 3 parafusos.

    estoque.ajustar_quantidade("OL01", 7)
    # Na contagem física sobrou 1 litro de óleo.

    print("\nEstoque final:")
    estoque.exibir()

    print("\nPerdas registradas:")
    estoque.exibir_perdas()