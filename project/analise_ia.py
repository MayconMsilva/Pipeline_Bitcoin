# analise_ia.py
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
import os

load_dotenv()


def gerar_analise_cripto(dados_tabela: str, prompt: str = "Com base nos dados abaixo, gere uma análise do mercado do Bitcoin.") -> str:
    agent = Agent(
        model=Groq(id="llama-3.3-70b-versatile"),
        description="Você é o agente de criptomoedas e entende análise técnica com base em séries temporais.",
        tools=[DuckDuckGoTools()],
        show_tool_calls=False,
        markdown=True
    )

    prompt_final = f"""{prompt}

### Dados históricos:
{dados_tabela}

Baseado nesses dados, descreva:
- Tendência de alta ou baixa.
- Possíveis momentos de pico ou queda.
- Recomendações gerais para o investidor."""

    response = agent.run(prompt_final)
    return response.content
