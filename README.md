# Projeto de Clustering com K-means
**Contexto** <br>
Você foi contratado por uma empresa de e-commerce que está buscando entender
melhor o comportamento de seus clientes para personalizar as suas campanhas de
marketing. Para isso, a empresa disponibilizou uma base de dados em csv contendo
dados sobre clientes, produtos e transações da loja realizadas entre os anos de 2010 e
2011.
<br><br>


**Objetivo** <br>
Com base nesses dados, você precisa agrupar os clientes em clusters com base em
seu comportamento de compra. Isso irá permitir identificar padrões e características em
comum entre os clientes, como:
- Clientes que compram os mesmos produtos;
- Clientes que possuem a mesma frequência de compras;
- Clientes que gastam mais dinheiro em suas compras.

A partir desses clusters, gere insights para que a empresa possa segmentar melhor a
sua base de clientes e personalizar as suas campanhas de marketing, direcionando
promoções e ofertas aos clientes com base no comportamento de compras.
<br><br>

**Dados** <br>
Os dados que iremos trabalhar em cima foram disponibilizado pela empresa em formato ***csv***, que consiste em dados tabulares que em cada linha do arquivo representa um registro e os valores são separados por linhas. Os dados foram separados da seguinte forma:

*Link kaggle:* https://www.kaggle.com/datasets/carrie1/ecommerce-data
<br>

- Colunas:

 **InvoiceNo** - Identificacao da transação<br>
 **StockCode** - Código de estoque do produto<br>
 **Description** - Descrição do produto<br>
 **Quantity** - Quantidade de produto por transação<br>
 **InvoiceDate** - Data de transação<br>
 **UnitPrice** - Preço unitário<br>
 **CustomerID** - Identificação do cliente<br>
 **Country** - Pais de origem da transação<br>

**Metodo**<br>
Nesse projeto iremos utilizar a metodologia do *Crisp-DM*, como base para o desenvolvimento, que consiste em dividir o projeto em seis etapas e como objetivo  desenvolver modelos a partir da análise de informações e dados de um negócio para prever futuras falhas e soluções.

<br>

## Estrutura do Projeto

- `data/`: Diretório para arquivos de dados.
- `notebooks/`: Diretório para notebooks Jupyter (se necessário).
- `src/`: Diretório para os módulos de código fonte.
    - `data_collection.py`: Módulo para coleta dos dados.
    - `data_preparation.py`: Módulo para preparação dos dados.
    - `model_modelling.py`: Módulo para modelagem dos dados.
    - `model_normalize.py`: Módulo para normalizacao dos dados.
    - `model_evaluation.py`: Módulo para avaliação do modelo.
    - `visualization.py`: Módulo para visualização dos clusters.
- `main.py`: Script principal para executar o pipeline.
- `.gitignore`: Arquivo para excluir arquivos desnecessários do Git.
- `requirements.txt`: Arquivo para listar dependências do projeto.
- `README.md`: Documentação do projeto.

## Configuração do Ambiente

1. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

2. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Executando o Projeto

1. Coloque o arquivo de dados no diretório `data/`.
2. Execute o script principal:
    ```sh
    python main.py
    ```

## Personalização

Ajuste o caminho do arquivo de dados conforme necessário no arquivo `main.py`.
