# Projeto Oficina Mecânica Sustentável

Disciplina Estrutura de Dados, Fatec Rio Claro.

## 1. Concepção do projeto

Este projeto desenvolve, em Python, um mini sistema de gestão para uma oficina mecânica. Ele integra os conceitos de Estrutura de Dados ao tripé da sustentabilidade, nas dimensões ambiental, econômica e social.

O sistema gerencia o ciclo completo de um atendimento. O veículo chega e entra na espera, com prioridade para guincho. Quando um box fica livre, o próximo é chamado e a ordem de serviço é aberta. O mecânico faz o diagnóstico numa árvore de componentes, as peças com defeito entram na OS, e no fechamento o sistema baixa as peças do estoque pelo lote mais antigo, registra o pagamento e anota o que cada veículo consumiu.

Todas as estruturas de dados foram implementadas em classes próprias. Não usamos `list` nem `dict` do Python para guardar os dados do problema. A única biblioteca usada é `datetime`, para datas e horários.

## 2. Como executar

```
python main.py
```

O arquivo roda os testes de cada módulo em sequência e termina com a simulação completa de um atendimento.

## 3. Organização do código

O código está separado em duas partes. De um lado ficam as estruturas de dados genéricas, que não sabem nada sobre oficina. Do outro ficam as regras da oficina, que usam essas estruturas.

**Estruturas genéricas**

| Módulo | Classe | Comportamento |
|---|---|---|
| 1 | `No` | Guarda um dado e o ponteiro para o próximo nó |
| 2 | `ListaEncadeada` | Inserção no fim, remoção em qualquer posição, percurso |
| 3 | `Fila` | Primeiro a entrar, primeiro a sair (FIFO) |
| 8 | `Pilha` | Último a entrar, primeiro a sair (LIFO) |

**Regras da oficina**

| Módulo | Classes | Responsabilidade |
|---|---|---|
| 4 | `Atendimento`, `ControleAtendimento` | Espera dos veículos e ocupação dos boxes |
| 5 | `CadastroClientes` | Clientes e seus veículos |
| 6 | `NoArvore`, `ArvoreDiagnostico` | Árvore de componentes e diagnóstico |
| 7 | `Lote`, `Produto`, `Perda`, `Estoque` | Estoque com lotes, validade e descarte |
| 9 | `ItemPeca`, `Servico`, `OrdemServico`, `ControleOS` | Ordens de serviço |
| 10 | `Pagamento` | Dados de cada pagamento |
| 11 | `RegistroConsumo`, `Caixa` | Fechamento da OS, baixa no estoque e consumo |
| 12 | `criar_arvore_componentes`, `simular_atendimento_completo` | Simulação do fluxo completo |

## 4. Árvore de componentes

A árvore é N-ária, ou seja, cada nó pode ter de 0 a N filhos. Ela não é binária nem de busca. Os filhos de cada nó ficam numa lista encadeada, com os ponteiros `primeiro_filho` e `proximo_irmao`. A árvore é pré-definida pela função `criar_arvore_componentes()`.

```
Veículo
├── Motor
│   ├── Sistema de ignição
│   │   ├── Vela (VL01)
│   │   └── Bobina (BB01)
│   └── Correia dentada (CD01)
├── Freios
│   ├── Pastilha dianteira (PF01)
│   └── Disco dianteiro (DD01)
└── Suspensão
    ├── Amortecedor (AM01)
    └── Bandeja (BD01)
```

Cada nó guarda o nome do componente, o código da peça quando for uma peça e o estado, que pode ser "OK" ou "Com defeito". A exibição usa percurso em profundidade, em pré-ordem, com recuo para mostrar a hierarquia.

Os códigos das peças são os mesmos do estoque. Assim, uma peça marcada com defeito na árvore aponta direto para o produto que será baixado no fechamento da OS.

## 5. Combinações de estruturas

### 5.1 Atendimento com prioridade: Fila + Fila + Fila

**Classes e métodos.** `ControleAtendimento` tem três objetos `Fila`, que são `fila_guincho`, `fila_idoso` e `fila_normal`. As filas trabalham juntas nos métodos `registrar_chegada`, `proximo_da_vez`, `chamar_proximo` e `liberar_box`.

**Por que é adequada.** Cada fila mantém a ordem de chegada entre os veículos do mesmo tipo, como pede o enunciado. O próximo atendido vem da fila de guincho. Se ela estiver vazia, vem da fila de idosos, e depois da fila normal. Quando um box fica livre, `liberar_box` chama o próximo automaticamente.

**Desvantagem de usar uma estrutura só.** Numa fila única, um veículo de guincho precisaria ser inserido no meio, à frente dos demais. Isso exige percorrer a fila a cada chegada, com custo O(n), e descaracteriza a fila. Com uma fila por prioridade, chegar e ser chamado custam O(1).

### 5.2 Clientes e veículos: Lista + Lista

**Classes e métodos.** `CadastroClientes` tem uma `ListaEncadeada` de clientes, e cada cliente tem a sua própria `ListaEncadeada` de veículos. As duas listas trabalham juntas em `buscar_por_placa`, `cadastrar_veiculo` e `remover_veiculo`.

**Por que é adequada.** Um cliente pode ter quantos veículos quiser, sem limite pré-definido. A lista cresce conforme novos veículos são cadastrados. Na busca por placa, o sistema percorre a lista de clientes e, dentro de cada um, a lista de veículos.

**Desvantagem de usar uma estrutura só.** Numa lista única de veículos, cada veículo precisaria repetir os dados do dono. Isso duplica informação e permite inconsistências, como o mesmo CPF com telefones diferentes.

### 5.3 Estoque com vários lotes: Lista de produtos, cada um com uma Fila de lotes

**Classes e métodos.** `Estoque` tem uma `ListaEncadeada` de `Produto`, e cada `Produto` tem uma `Fila` de `Lote`. As estruturas trabalham juntas em `buscar_produto`, `entrada_lote`, `retirar`, `descartar_vencidos` e `ajustar_quantidade`.

**Por que é adequada.** Um mesmo produto pode ter lotes comprados em datas e preços diferentes. A fila garante que a saída sempre consuma primeiro o lote mais antigo, como pede o enunciado. Em `descartar_vencidos`, cada lote sai da fila uma vez. Os vencidos são registrados como perda e os válidos voltam para o fim, o que mantém a ordem original.

**Desvantagem de usar uma estrutura só.** Se todos os lotes de todos os produtos ficassem numa única fila, para tirar óleo seria preciso passar por pastilhas e parafusos até achar o lote de óleo mais antigo. Com uma fila por produto, o lote certo está sempre no início.

**Alternativa considerada.** Ordenar os lotes pela validade, consumindo primeiro o que vence antes. Optamos pela ordem de compra porque é a regra do enunciado e porque muitos produtos, como parafusos, não têm validade.

### 5.4 Árvore de componentes: Árvore + Lista

**Classes e métodos.** Em `NoArvore`, os filhos de cada nó formam uma lista encadeada pelos ponteiros `primeiro_filho` e `proximo_irmao`. O método `pecas_com_defeito` percorre a árvore em pré-ordem e devolve uma `ListaEncadeada` com as peças marcadas com defeito.

**Por que é adequada.** A lista de filhos permite que cada nó tenha qualquer quantidade de filhos. A lista de defeitos é o elo entre o diagnóstico e a ordem de serviço.

**Desvantagem de usar uma estrutura só.** Uma árvore binária limitaria cada componente a dois filhos, e o enunciado exige de 0 a N.

### 5.5 Ordem de serviço: Lista de peças + Lista de serviços + Pilha de desmontagem

**Classes e métodos.** Cada `OrdemServico` tem duas `ListaEncadeada`, uma de `ItemPeca` e outra de `Servico`, e uma `Pilha` de desmontagem. Os métodos envolvidos são `adicionar_peca`, `remover_peca`, `adicionar_servico`, `remover_servico`, `adicionar_pecas_com_defeito`, `desmontar`, `remontar` e `fechar`. `ControleOS` guarda as OS abertas e fechadas em listas.

**Por que é adequada.** Peças e serviços entram e saem em qualquer posição conforme o diagnóstico avança ou o cliente não autoriza um serviço, e a lista permite isso. A remontagem acontece na ordem inversa da desmontagem, que é exatamente o comportamento da pilha. O método `fechar` só aceita fechar a OS quando a pilha está vazia, ou seja, quando a remontagem foi concluída.

**Desvantagem de usar uma estrutura só.** Uma lista no lugar da pilha não garantiria a ordem inversa. Seria preciso controlar à mão qual componente foi desmontado por último.

### 5.6 Fechamento da OS: OS + Estoque + Caixa

**Classes e métodos.** O método `Caixa.fechar_e_pagar` percorre a lista de peças da OS, busca cada peça na lista de produtos do `Estoque` e consome a fila de lotes daquele produto. No mesmo passo, cria um `RegistroConsumo` para cada peça, fecha a OS e registra o `Pagamento`. O `Caixa` guarda pagamentos e consumos em listas, e `consumo_por_placa` mostra o que cada veículo consumiu.

**Por que é adequada.** O método `estoque_suficiente` confere todas as peças antes de baixar qualquer uma. Assim o estoque não fica pela metade se faltar alguma peça. A baixa acontece no fechamento, e não na inclusão da peça, para que o cliente possa desistir de uma peça sem que o estoque precise ser corrigido.

**Desvantagem de usar uma estrutura só.** Guardar pagamento e consumo dentro da própria OS misturaria responsabilidades e dificultaria consultar o consumo de um veículo em várias OS.

## 6. Complexidade das principais operações

| Operação | Complexidade |
|---|---|
| Enfileirar e desenfileirar na fila | O(1) |
| Empilhar e desempilhar na pilha | O(1) |
| Inserir no fim da lista encadeada | O(n) |
| Buscar cliente por CPF | O(c), com c clientes |
| Buscar veículo por placa | O(c + v), com v veículos no total |
| Buscar produto no estoque | O(p), com p produtos |
| Descartar lotes vencidos | O(p + l), com l lotes no total |
| Buscar componente na árvore | O(k), com k nós |

## 7. Sustentabilidade

**Ambiental.** Cada produto do estoque guarda o destino correto de descarte. O óleo lubrificante usado, por exemplo, vai para rerrefino, conforme a Resolução CONAMA 362/2005. Lotes vencidos são registrados como perda junto com esse destino.

**Social.** Além da prioridade para guincho pedida no enunciado, a oficina tem uma fila preferencial para clientes idosos, com base no Estatuto da Pessoa Idosa, Lei 10.741/2003.

**Econômica.** Consumir primeiro o lote mais antigo reduz as perdas por vencimento. O alerta de estoque mínimo evita falta de peças, e o ajuste de inventário corrige diferenças entre o sistema e a contagem física.

## 8. Desenvolvimento incremental

**Sábado, 24/10.** Criação do repositório no GitHub e do README inicial com a concepção do projeto.

**Segunda-feira, 26/10.** Estudo do enunciado e planejamento das classes, sem commit.

**Terça-feira, 27/10.** Módulos 1 a 3, com as classes `No`, `ListaEncadeada` e `Fila`, incluindo o método `espiar`.

**Quarta-feira, 28/10.** Módulo 4, controle de atendimento com filas de guincho, idosos e normal. Módulo 5, cadastro de clientes e veículos. Módulo 6, primeira versão da árvore N-ária de diagnóstico. Módulo 7, estoque com lista de produtos e fila de lotes, descarte de vencidos e ajuste de inventário. Reformulação do Módulo 6 como árvore de componentes, com código e estado de cada peça. Módulo 8, pilha. Módulo 9, ordem de serviço. Módulos 10 e 11, pagamento e controle do consumo. Módulo 12, simulação completa. Versão final deste README.
