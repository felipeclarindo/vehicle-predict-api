🌍 [Read in English](README.md)

# Vehicles Predict Api

Api Rest desenvolvida em `flask` para realizar previsões baseado em um modelo de Machine Learning.

## Tecnologias utilizadas

- `scikit-learn` - Biblioteca principal para criação e treinamento do modelo preditivo, incluindo pré-processamento de dados e avaliação do desempenho.
- `pandas` - Usado para manipulação e análise de dados, facilitando o tratamento dos dados de entrada e saída do modelo.
- `flask` - Desenvolvimento da API do projeto, permitindo a comunicação entre o modelo de predição e os usuários.
- `joblib` - Salvar e carregar o modelo de Machine Learning de forma eficiente, garantindo rapidez na inferência.
- `Python` - Linguagem utilizada para o desenvolvimento
- `flask-cors` - Configuração do CORS da API.

## Objetivos

Este modelo de Machine Learning foi desenvolvido para prever a quantidade de veículos em diferentes contextos, com base nos dados disponíveis. A API permite enviar novas informações e receber previsões precisas que podem ser aplicadas para melhorar o planejamento e a gestão de tráfego, logística e infraestrutura. Abaixo estão alguns dos insights que este modelo oferece:

1.  Previsão do Volume de Veículos: Com os dados fornecidos, o modelo estima o número de veículos para um determinado cenário, fornecendo uma base de referência útil para análise de tráfego.

2.  Identificação de Padrões: O modelo captura tendências e sazonalidades no fluxo de veículos, o que é útil para identificar horários e períodos de maior e menor movimento.

3.  Impacto de Variáveis Específicas: Ao usar um modelo Random Forest, é possível determinar quais variáveis têm maior influência na quantidade de veículos, como dias da semana, condições climáticas ou eventos especiais.

4.  Avaliação de Precisão do Modelo: Métricas como o Mean Squared Error (MSE) e o R2 Score são calculadas para entender a precisão das previsões:
    - O MSE quantifica a diferença média ao quadrado entre os valores previstos e reais, oferecendo uma medida do erro médio de previsão.
    - O R2 Score indica a proporção da variação nos dados explicada pelo modelo, ajudando a avaliar o quão bem ele representa a realidade.

Esses resultados podem ser aplicados para melhorar a tomada de decisões em gestão de tráfego, planejamento urbano e otimização logística, fornecendo previsões práticas que apoiam decisões fundamentadas.

## Passos para instalação e execução

1. Clone o repositório:

```bash
git clone https://github.com/felipeclarindo/vehicle-predict-api.git
```

2. Entre no diretório:

```bash
cd vehicle-predict-api
```

3. Crie o `Ambiente Virtual`:

```bash
python -m venv .venv
```

4. Ative o `Ambiente Virtual` executando o arquivo `.bat` em `.venv/Scripts/activate.bat`.

5. Instale as dependências:

```bash
pip install -r ./requirements.txt
```

6. Rode as celular jupyter do arquivo [model_training.ipynb](./src/model_training.ipynb).

7. Inicie a api

```bash
python ./src/api/api.py
```

8. Após rodar, acesse a api em:

- `http://localhost:3000/api` -Informações sobre a api.
- `http://localhost:3000/api/docs` - Documentação da api.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Autor

**Felipe Clarindo**

- [LinkedIn](https://www.linkedin.com/in/felipeclarindo)
- [Instagram](https://www.instagram.com/lipethecoder)
- [GitHub](https://github.com/felipeclarindo)

## Licença

Este projeto está licenciado sob a [GNU Affero License](https://www.gnu.org/licenses/agpl-3.0.html).
