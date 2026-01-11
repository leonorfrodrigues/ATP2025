# Projeto – Gestão de Clínica Hospitalar  
**Descrição da Estrutura e Funcionamento do Código**

## Introdução

Este documento descreve a **estrutura interna e o funcionamento do código** desenvolvido no âmbito do projeto *Gestão de Clínica Hospitalar*.  
O objetivo deste texto é explicar a organização do projeto, os módulos que o compõem, as bibliotecas utilizadas e os principais parâmetros e estruturas de dados.

## Setup
### Bibliotecas utilizadas:
- **matplotlib**: utilizada na geração de gráficos estatísticos;
- **FreeSimpleGUI**: utilizada na criação da interface gráfica;
- **json**: utilizada para a leitura e escrita de dados de forma mais legível;
- **random**: utilizada na simulação para vários valores serem aleatórios a cada execução (A simulação recorre a valores aleatórios na geração de doentes, médicos e tempos, pelo que diferentes execuções podem produzir resultados distintos);
- **numpy**: utilizada para cálculos numéricos e estatísticos.

### Estrutura do projeto:
O projeto encontra-se organizado da seguinte forma:

- **Constantes**(`constantes.py`):
  Este ficheiro define valores globais utilizados em todo o projeto, nomeadamente:

  * Lista de especialidades médicas;
  * Cores das pulseiras atribuídas aos doentes.

  Estas constantes garantem consistência e facilitam a manutenção do código.

- **Doentes**(`doentes.py`):
  Este módulo é responsável pela criação de um doente/paciente, representado sob a forma de um dicionário contendo:

  * Nome;
  * Id;
  * Sexo;
  * Idade;
  * Especialidade;
  * Cor da pulseira.

  A especialidade e a pulseira são atribuídas sem critério clínico complexo. No entanto, existe uma condição importante: se o doente tiver idade inferior a 18 anos, é automaticamente encaminhado para a especialidade de **Pediatria**.

- **Médicos**(`médicos.py`):
  Este módulo define a estrutura de um médico(`cria_medicos`)e as operações associadas, incluindo:

  * Especialidade- neste parâmetro foi imposto que houvesse pelo menos um médico de cada especialidade;
  * Estado (livre ou ocupado);
  * Doente atualmente em consulta;
  * Tempo total de ocupação.

  Permite calcular estatísticas individuais e globais sobre a utilização dos médicos.

- **Lista de espera**(`lista_espera.py`):
  Este ficheiro gere a fila de espera da clínica, implementando:

  * Inserção de doentes na fila (`acrescentar_doente_fe`);
  * Remoção de doentes da fila (`retirar_doente_fe`);
  * Tamanho das filas de espera (`tamanho_le`)
  * Cumprimento da prioridade associada à cor da pulseira do doente implementada nas funções mencionadas acima.

- **Analisa simulação**(`analisa_simulacao.py`):
  Este ficheiro contém uma função responsável por carregar uma simulação previamente executada e guardada num ficheiro **JSON** pelo utilizador. São recuperadas todas as variáveis necessárias para:

  * Reproduzir a simulação;
  * Executar cálculos estatísticos;
  * Gerar os gráficos associados ao funcionamento da clínica.


- **Estatísticas**(`estatisticas.py`):
  Este ficheiro contém funções que permitem analisar o desempenho da clínica, incluindo:

  - *Maior tempo de espera* – mostra o maior tempo de espera registado e a informação (id, nome e especialidade) do/s doente/s correspondente/s;
  - *Maior tempo de permanência* – mostra o maior tempo total na clínica e a informação (id, nome e especialidade) do/s doente/s correspondente/s;
  - *Número de pessoas suspeitas* – doentes com valores de tempo suspeitos;
  - *Análise do doente com maior tempo de espera* – análise individual do doente com maior tempo de espera, com conclusões específicas;
  - *Especialidades sob pressão* – especialidades com maior sobrecarga, tendo em conta a ocupação do médico e o elevado tempo de espera;
  - *Percentagem de ocupação dos médicos* – mostra o quão ocupado esteve cada médico ao longo do dia, especificando a especialidade respetiva;
  - *Tempos médios por pulseira* – permite avaliar o cumprimento das prioridades através da análise dos tempos de espera médios por cada cor de pulseira;
  - *Percentagem de inversão da prioridade* – falhas no atendimento prioritário por doentes com menor prioridade apresentaram tempos de espera inferiores, o que se explica por fatores como chegadas espaçadas e indisponibilidade momentânea dos médicos;
  - *Deteção de períodos críticos* – identificação de momentos de elevada pressão

- **Gráficos**(`graficos.py`):
  Responsável pela geração dos gráficos que representam visualmente os resultados da simulação, tais como:

  - *Tempo médio de espera por especialidade* – compara tempos médios de espera entre especialidades;
  - *Distribuição do tempo de permanência* – mostra o tempo total dos doentes na clínica por intervalos de 2h;
  - *Número de doentes por especialidade* – analisa a procura por cada especialidade por parte dos doentes;
  - *Atendimento imediato vs em espera* – compara doentes atendidos de imediato com os que esperaram;
  - *Atendimento imediato por especialidade* – eficiência de atendimento imediato por especialidade;
  - *Afluência* – evolução das chegadas ao longo do tempo, determinando o pico de afluência;
  - *Pulseiras por especialidade* – distribuição de prioridades por especialidade;
  - *Tempo médio de espera por pulseira* – avalia o respeito da prioridade mostrando quando tempo cada doente com a respetiva pulseira esperou;
  - *Distribuição do sexo dos doentes* – análise demográfica que determina o sexo dos doentes;
  - *Distribuição etária dos doentes* – análise etária dos doentes;
  - *Evolução das filas de espera por especialidade* – crescimento e redução das filas de espera ao longo do tempo.

  Neste ficheiro também contém funções que auxiliam à execução dos gráficos tais como:
  * Pacientes por pulseira- classifica os doentes segundo o critério da cor da pulseira;
  * Pacientes por especialidade- classifica os doentes de acordo com a especialidade.
 
- **Clinica**(`clinic_alunos_oficial.py`):

  Este é o ficheiro principal do projeto. É responsável por executar a simulação da clínica, incluindo:

  * Criação e gestão das filas de espera;
  * Gestão das entradas e saídas da fila (utilizando as funções `enqueue` e `dequeue`);
  * Atribuição de médicos aos doentes;
  * Atribuição de id's aos doentes aquando da sua chegada;
  * Registo dos eventos de chegada e saída;
  * Armazenamento da simulação após o seu término.

  Os parâmetros iniciais da simulação podem ser alterados pelo utilizador. No final da execução, o ficheiro retorna a lista `doentes_atendidos_info`, que contém informação detalhada sobre cada doente, nomeadamente:

  * Nome do doente;
  * Id atribuído;
  * Especialidade atribuída;
  * Cor da pulseira;
  * Tempo de chegada;
  * Tempo do ínicio de consulta;
  * Tempo de saída;
  * Tempo de espera;
  * Tempo de permanência na clínica;
  * Ficou em espera, onde retorna um booleano.

  Neste ficheiro são importados os módulos **Constantes**, **Médicos**, **Doentes** e **Lista de Espera**, permitindo simular uma clínica hospitalar em funcionamento realista.

- **Interface**(`interface.py`):
  Este módulo implementa a interface gráfica da aplicação, permitindo ao utilizador:

  * Alterar os parâmetros da simulação;
  * Executar novas simulações;
  * Carregar simulações guardadas;
  * Visualizar gráficos e estatísticas;
  * Visualização da lista de espera de cada especialidade em função das pulseiras.

### Descrição dos parâmetros:
#### `clinic_alunos_oficial.py`
  **Parâmetros principais da simulação**
  - *NUM_MEDICOS* - Número total de médicos disponíveis na simulação. É gerado aleatoriamente entre o número de especialidades existentes e um valor inteiro >5 escolhido pelo utilizador;
  - *TAXA_CHEGADA* - Taxa média de chegada de doentes (doentes por minutos). Por exemplo:'15/60' significa que chegam, em média, 15 doentes por hora (60min);
  - *TEMPO_MEDIO_CONSULTA* - Duração média de uma consulta (em minutos);
  - *TEMPO_SIMULACAO* - Tempo total da simulação, em minutos. Por exemplo: 8 * 60min;
  - *DISTRIBUICAO_TEMPO_CONSULTA* - Distribuição estatística usada para gerar a duração das consulta(exponential, normal, uniform).

  NOTA: todos os parâmetros podem ser alterados através da interface, ao executar uma nova simulação

  **Parâmetros do EVENTO: Chegada - representa a chegada de um doente à clínica**
  - *tempo* - momento (em minutos) em que o doente chega à clínica (float);
  - *tipo* - "chegada" (string);
  - *doente* - dicionário com os dados do doente (dict).

  **Parâmetros do EVENTO: Saída - representa a saída de um doente à clínica**
  - *tempo* - momento (em minutos) em que o doente chega à clínica (float);
  - *tipo* - "saída" (string);
  - *doente* - dicionário com os dados do doente cuja consulta terminou (dict).

#### `doentes.py`
  **Doente**
  - *nome* - nome do doente (string); 
  - *id* - identificador único de cada doente (string);
  - *sexo* - sexo do doente (string);
  - *especialidade* - especialidade na qual o doente quer ser atendido (string);
  - *tempo_chegada* - momento de entrada do doente na clínica (float);
  - *tempo_inicio_consulta* - inicio do atendimento (float);
  - *tempo_saida* - saída do doente da clínica (float);
  - *pulseira* - parâmetro principal de prioridade nas filas de espera (string).

#### `médicos.py`
  **Médicos**
  - *NUM_MEDICOS* - número total de médicos (int);
  - *especialidade* - especialidade do médico (string);
  - *ocupado* - estado de ocupação do médico (bool);
  - *total_tempo_ocupado* - total de tempo em que o médico está em consulta(float);
  - *inicio_ultima_consulta* - momento em que começou a consulta(float).

#### `lista_espera.py`
  **Filas de espera**
  - *filas_espera* - filas por especialidade(dict);
  - *tamanho_le()* - comprimento da fila;
  - *ha_doentes()* - verificação de doentes na fila de espera;

#### `estatisticas.py`
  **Parâmetros estatísticos**
  - *tempo_espera* - tempo que doente esperou desde que entrou na clínica até ser atendido (float);
  - *tempo_permanencia* - tempo total de um doente na clínica (float);
  - *historico_ocupacao* - ocupação dos médicos ao longo do tempo(list);
  - *historico_filas* - evolução das filas(list).

#### `constantes.py`
  **CONSTANTES**
  - *ESPECIALIDADES* - lista de especialidades escolhidas pelos criadores, constantes durante a simulação (list);
  - *PULSEIRA* - lista da cor das pulseiras escolhidas pelos criadores, constantes durante a simulação (list).

#### `clinica_alunos_oficial1.py` e `analisa_simulação.py`
 **Guardar e carregar simulação**
  - a simulação pode ser guardada num ficheiro JSON e posteriormente carregada para ser analisada. Este ficheiro contém:
      - parâmetros utilizados;
      - lista de doentes atendidos;
      - estado final de ocupação dos médicos;
      - histórico das filas de espera por especialidade;
      - histórico de ocupação dos médicos

### Conclusão:

A separação do projeto em múltiplos ficheiros permite uma organização clara, estruturada e de fácil manutenção. Cada componente desempenha um papel específico na simulação, contribuindo para uma representação realista do funcionamento de uma clínica hospitalar.

### Autores:  
Catarina Pereira Costa (A111924)  
Hugo Pescadinha Lomba (A110406)  
Leonor Ferreira Rodrigues (A111548)