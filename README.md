# Tic-Tac-Toe-Jogo-da-Velha
Jogo da Velha em Python com interface web em Flask e HTML.  Possui venv com dependências via requirements.txt. A IA decide jogadas com Minimax e utiliza RandomForestClassifier treinado com dados CSV.


#ESTRUTURA DO PROJETO

    Jogo_da_Velha/
    │
    ├── tic_tac_toe_dataset.csv
    ├── requirements.txt
    ├── game_velha.py
    │
    ├── templates/
        └── index.html


*   Jogo_da_Velha: Pasta Raiz do Projeto
*   game_velha.py: lógica principal do jogo, IA (Algorítimo Minimax + Algorítimo RandomForest) e Flask
*   tic_tac_toe_dataset.csv: Dados para Treinamento da IA
*   requirements.txt: Dependências do projeto **Bibliotécas usadas no Projeto
*   templates/: Pasta com arquivos HTML -> index.html, usados pelo Flask para a Intergração Web


# Resumindo as Principais Funcionalidades e Funcionamento do Projeto - game_velha.py

Este projeto implementa um **Jogo da Velha** em Python, integrando uma interface web simples com uma inteligência artificial capaz de tomar decisões estratégicas. A aplicação foi desenvolvida com foco didático, combinando conceitos de **desenvolvimento web**, **algoritmos clássicos de jogos** e **aprendizado de máquina**.

# Interface Web com Flask

A aplicação utiliza o framework **Flask** para criar a comunicação entre o usuário e a lógica do jogo. A interface gráfica é renderizada a partir de um arquivo HTML.
Esse trecho abaixo é responsável por inicializar o servidor web e disponibilizar a página principal do jogo no navegador, permitindo que o usuário interaja de forma simples e intuitiva.

```
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
```

# Leitura de Dados e Treinamento do Modelo

O projeto carrega um conjunto de dados em formato CSV contendo estados do tabuleiro e jogadas ideais. Esses dados são utilizados para treinar um modelo de **RandomForestClassifier**, por meio das bibliotecas **Pandas** e **Scikit-learn**.
O treinamento permite que o modelo reconheça padrões de jogo, contribuindo para a lógica estratégica da aplicação e demonstrando a integração de técnicas de Machine Learning ao projeto.

```
data = pd.read_csv("tic_tac_toe_dataset.csv")

X = data.iloc[:, 0:9]
y = data["move"]

model = RandomForestClassifier()
model.fit(X, y)
```

# Verificação de Condições de Vitória

A verificação de vitória é realizada por uma função específica que avalia todas as combinações possíveis do tabuleiro.
Essa abordagem centraliza a lógica de validação, tornando o código mais legível, reutilizável e fácil de manter.

```
def verificar_vitoria(tab, player):
    combos = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
```

# Algoritmo Minimax

A principal tomada de decisão da IA é feita utilizando o algoritmo **Minimax**, amplamente empregado em jogos de dois jogadores.
O Minimax simula todas as jogadas possíveis, considerando ações do jogador e da IA, buscando sempre maximizar o resultado da IA e minimizar o do oponente. Isso garante jogadas consideradas matematicamente perfeitas.

```
def minimax(tab, player):
    if verificar_vitoria(tab,1):
        return 1, None
```

### Controle de Dificuldade da Inteligência Artificial

A dificuldade da IA é configurável por meio de uma variável probabilística.
Com isso, a IA realiza jogadas perfeitas na maior parte do tempo, mas ocasionalmente escolhe jogadas aleatórias, simulando erros humanos e tornando a experiência de jogo mais equilibrada e realista.

```
DIFICULDADE = 0.92
```

# Comunicação entre Frontend e Backend

As jogadas do usuário são enviadas ao servidor por meio de requisições **POST** em formato JSON.
O servidor processa a jogada, executa a resposta da IA e retorna o estado atualizado do tabuleiro, juntamente com o resultado da partida (vitória, derrota ou empate).

```
@app.route("/jogar", methods=["POST"])
def jogar():
    tab = request.json["tabuleiro"]
```

# Execução da Aplicação

Por fim, a aplicação é executada localmente utilizando o servidor de desenvolvimento do Flask.
Esse modo facilita testes, validações e ajustes durante o desenvolvimento do projeto.

```
app.run(debug=True)
```



# Instalação do Projeto
## 1. Baixar o Repositório

1.  Acesse o repositório do projeto no GitHub
2.  Clique em **Code** → **Download ZIP**
3.  Após o download, **extraia o arquivo `.zip`** em uma pasta de sua preferência (NO MEU CASO DEIXEI NA: C:\Users\MeuUser\Documents)

## 2. Acessar a Pasta do Projeto

1ª Opção: Abra o terminal (Prompt de Comando, PowerShell ou Terminal Linux/macOS), navegue até a pasta do projeto:

```bash
cd caminho/para/Jogo_da_Velha
```

## 3. Criar e Ativar o Ambiente Virtual (venv)

- É recomendado utilizar um **ambiente virtual(venv)** para isolar as dependências do projeto.

## Criar o ambiente virtual

```bash
python -m venv venv
```

## Ativar o ambiente virtual

No caso de Windows:

```bash
venv\Scripts\activate
```

No caso de Linux/MacOS

```shell
source venv/bin/activate
```

Após a ativação, o terminal indicará que o ambiente virtual está em uso.

### 4. Instalar as Dependências
- Com o ambiente virtual ativo, instale todas as bibliotecas necessárias utilizando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Esse comando instalará automaticamente:

*   Flask
*   Pandas
*   Scikit-learn
*   Demais dependências do projeto

### 5. Verificar os Arquivos Necessários
- Antes de executar o projeto, certifique-se de que os seguintes arquivos estão presentes na pasta raiz:

*   `game_velha.py`
*   `tic_tac_toe_dataset.csv`
*   `requirements.txt`
*   Pasta `templates/` com o arquivo `index.html`

### 6. Executar a Aplicação
- Para iniciar o servidor Flask, execute o arquivo principal:
- Se tudo estiver correto, o terminal exibirá mensagens indicando que o servidor está ativo.

```bash
python game_velha.py
```

### 7. Acessar o Jogo no Navegador
- Abra um navegador web e acesse:
- A interface do **Jogo da Velha** será exibida, permitindo jogar contra a IA diretamente pelo navegador.
```
    http://127.0.0.1:5000
```



# INFORMAÇÕES DO DESENVOLVEDOR

- DESENVOLVEDOR: JULIAN ANTHONY MOREIRA CAMPEÃO
- CONTATO
TELEFONE/WHATSAPP: (41) 99751-9686
E-MAIL: campeaojulian@gmail.com
Para mais informações acesse o meu Linkedin: https://www.linkedin.com/in/julian-campeao-5422b2347/
#
