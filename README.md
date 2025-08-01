<<<<<<< HEAD
# Pipeline_Bitcoin
=======
<<<<<<< HEAD
# Pipeline_Bitcoin
=======
# Pipeline de Cotação e Análise de Bitcoin

Este projeto realiza a coleta automática do preço do Bitcoin via API, armazena os dados localmente, exibe um dashboard interativo e utiliza inteligência artificial para gerar análises automáticas do mercado.

## Funcionalidades

- **Coleta automática de dados**: Busca o valor do Bitcoin periodicamente na API da Coinbase.
- **Armazenamento local**: Salva os dados em um banco de dados leve (`TinyDB`).
- **Dashboard interativo**: Visualização dos dados históricos, métricas e gráficos em tempo real com Streamlit.
- **Análise com IA**: Geração de análises automáticas do mercado usando LLMs (Groq) e ferramentas de busca.

## Estrutura dos Arquivos

```
project/
├── request_api.py      # Coleta, transforma e armazena os dados do Bitcoin
├── db.json             # Banco de dados local TinyDB com os registros coletados
├── dashboard.py        # Dashboard interativo com Streamlit e análise de IA
├── analise_ia.py       # Função para análise automática dos dados com LLM
├── agent.py            # Exemplo de uso do agente de IA para análise detalhada
```

## Como executar

1. **Instale as dependências**  
   Recomenda-se o uso de um ambiente virtual.
   ```sh
   pip install requests tinydb streamlit pandas plotly agno duckduckgo-search python-dotenv
   ```

2. **Configure as variáveis de ambiente**  
   Crie um arquivo `.env` na pasta `project` com sua chave da API Groq:
   ```
   GROQ_API_KEY=seu_token_groq_aqui
   ```

3. **Inicie a coleta de dados**  
   Execute o script de coleta:
   ```sh
   python project/request_api.py
   ```
   Os dados serão salvos em `project/db.json` a cada 15 segundos.

4. **Abra o dashboard**  
   Em outro terminal, execute:
   ```sh
   streamlit run project/dashboard.py
   ```
   Acesse o endereço exibido no terminal para visualizar o dashboard.

## Detalhes dos Componentes

- **request_api.py**: Realiza o ciclo ETL (Extrair, Transformar, Carregar) dos dados do Bitcoin.
- **db.json**: Armazena os registros históricos coletados.
- **dashboard.py**: Mostra gráficos, métricas e permite acionar a análise de IA.
- **analise_ia.py**: Usa um modelo LLM (Groq) para analisar os últimos dados coletados.
- **agent.py**: Exemplo de uso do agente de IA para análises customizadas.

## Observações

- Para a análise de IA funcionar, é necessário ter uma chave válida da API Groq.
- O dashboard permite visualizar os dados brutos e gerar análises automáticas sob demanda.
- A coleta de dados é feita a cada 15 segundos, mas pode ser ajustada conforme necessário.
>>>>>>> 57a0408 (Commit do projeto)
>>>>>>> 8d5c41f (Commit do projeto Pipeline)
