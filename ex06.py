from fastapi import FastAPI
from fastapi.responses import JSONResponse
import random
import json

app = FastAPI()

temas_json={
  "Engenharia de Software": {
    "1. Conceitos Básicos": {
      "descrição": "Engenharia de Software envolve a aplicação de princípios de engenharia para o desenvolvimento de software de alta qualidade.",
      "subtópicos": {
        "Desenvolvimento Ágil": "Metodologias ágeis como Scrum e Kanban.",
        "Cascata": "Modelo tradicional sequencial de desenvolvimento.",
        "DevOps": "Integração contínua e entrega contínua de software."
      }
    },
    "2. Ciclo de Vida de Software": {
      "descrição": "As fases do desenvolvimento de software, desde o planejamento até a manutenção.",
      "subtópicos": {
        "Análise de Requisitos": "Entendimento e documentação das necessidades do cliente.",
        "Design": "Criação da arquitetura do sistema.",
        "Implementação": "Codificação do software.",
        "Testes": "Verificação da qualidade e funcionalidade do software.",
        "Manutenção": "Atualizações e correções de bugs após o lançamento."
      }
    },
    "3. Modelos de Processos de Software": {
      "descrição": "Modelos para organizar e estruturar o desenvolvimento de software.",
      "subtópicos": {
        "Ágil": "Iterativo e incremental, focado em entregas rápidas.",
        "Cascata": "Modelo sequencial de desenvolvimento.",
        "Iterativo": "Modelo que realiza várias repetições e revisões."
      }
    }
  },
  "Arquitetura de Software": {
    "1. Definição": {
      "descrição": "Arquitetura de software é a estrutura organizacional de um sistema de software.",
      "subtópicos": {
        "Padrões de Arquitetura": "Modelos como MVC, Microserviços e Monolíticos.",
        "Componentes": "Partes de um sistema que interagem entre si.",
        "Camadas de Software": "Estrutura hierárquica de componentes."
      }
    },
    "2. Padrões de Arquitetura": {
      "descrição": "Padrões para resolver problemas comuns no desenvolvimento de software.",
      "subtópicos": {
        "Microserviços": "Divisão do sistema em pequenos serviços independentes.",
        "Monolítico": "Tudo em um único sistema integrado."
      }
    },
    "3. Desafios da Arquitetura de Software": {
      "descrição": "Dificuldades ao projetar e implementar a arquitetura do sistema.",
      "subtópicos": {
        "Escalabilidade": "Ajustar o sistema para crescer de maneira eficiente.",
        "Manutenibilidade": "Facilidade em fazer modificações no futuro."
      }
    }
  },
  "Engenharia de Dados": {
    "1. Definição": {
      "descrição": "Engenharia de dados é o processo de coleta, armazenamento e processamento de grandes volumes de dados.",
      "subtópicos": {
        "ETL (Extração, Transformação e Carga)": "Processo de movimentação e preparação de dados.",
        "Armazenamento de Dados": "Bancos de dados e data lakes para armazenamento de grandes volumes."
      }
    },
    "2. Processamento de Dados": {
      "descrição": "Métodos e ferramentas para manipular e analisar dados.",
      "subtópicos": {
        "Big Data": "Tecnologias que lidam com grandes volumes de dados.",
        "Hadoop": "Framework de código aberto para processamento de Big Data."
      }
    }
  },
  "API": {
    "1. Definição": {
      "descrição": "Uma API (Interface de Programação de Aplicações) permite que diferentes sistemas se comuniquem entre si.",
      "subtópicos": {
        "API REST": "Arquitetura de comunicação baseada em HTTP.",
        "GraphQL": "API que permite consultas flexíveis ao banco de dados."
      }
    },
    "2. Tipos de APIs": {
      "descrição": "Vários tipos de APIs para diferentes necessidades.",
      "subtópicos": {
        "Open API": "API pública que permite acesso externo.",
        "Private API": "API interna, restrita ao uso dentro da organização."
      }
    }
  },
  "Design Web": {
    "1. Definição": {
      "descrição": "Design de websites envolve a criação da estética e funcionalidade das páginas web.",
      "subtópicos": {
        "UI/UX": "Interface de usuário e experiência do usuário.",
        "Responsividade": "Adaptação de layouts para diferentes dispositivos."
      }
    },
    "2. Ferramentas de Design": {
      "descrição": "Ferramentas usadas por designers para criar interfaces e protótipos.",
      "subtópicos": {
        "Figma": "Ferramenta de design colaborativo.",
        "Adobe XD": "Ferramenta de prototipagem de interfaces."
      }
    }
  },
  "UI/UX": {
    "1. Definição": {
      "descrição": "UI/UX são disciplinas que tratam da criação de interfaces eficientes e da experiência do usuário em interações digitais.",
      "subtópicos": {
        "UI (Interface de Usuário)": "Design dos elementos visuais com os quais o usuário interage.",
        "UX (Experiência do Usuário)": "A sensação do usuário ao interagir com o sistema."
      }
    },
    "2. Princípios de Design": {
      "descrição": "Princípios que orientam o design de interfaces e experiências.",
      "subtópicos": {
        "Usabilidade": "Facilidade de uso de um sistema.",
        "Acessibilidade": "Facilidade de uso para pessoas com deficiência."
      }
    }
  },
  "Arquitetura de Banco de Dados": {
    "1. Definição": {
      "descrição": "A arquitetura de banco de dados é a estruturação de dados em um banco de dados, com foco em otimização e integridade.",
      "subtópicos": {
        "Relacional": "Banco de dados estruturado com tabelas e relações.",
        "NoSQL": "Banco de dados sem estrutura fixa, ideal para dados não estruturados."
      }
    },
    "2. Modelagem de Dados": {
      "descrição": "Processo de criar um modelo para a estrutura dos dados no banco de dados.",
      "subtópicos": {
        "Modelo Entidade-Relacionamento (ER)": "Modelo usado para representar dados e suas relações.",
        "Normalização": "Processo de eliminar redundâncias de dados."
      }
    }
  },
  "Redes": {
    "1. Definição": {
      "descrição": "Redes de computadores são sistemas de comunicação que conectam diferentes dispositivos.",
      "subtópicos": {
        "Modelos de Rede": "Modelo OSI e TCP/IP.",
        "Tipos de Rede": "LAN, WAN, MAN."
      }
    },
    "2. Protocolos de Comunicação": {
      "descrição": "Protocolos determinam como os dados são transmitidos nas redes.",
      "subtópicos": {
        "HTTP/HTTPS": "Protocolos para comunicação web.",
        "FTP": "Protocolo para transferência de arquivos."
      }
    }
  },
  "Computação em Nuvem e Segurança": {
    "1. Computação em Nuvem": {
      "descrição": "A computação em nuvem envolve o uso de servidores remotos para armazenar, gerenciar e processar dados.",
      "subtópicos": {
        "Serviços IaaS": "Infraestrutura como Serviço.",
        "PaaS": "Plataforma como Serviço.",
        "SaaS": "Software como Serviço."
      }
    },
    "2. Segurança de TI": {
      "descrição": "A segurança de TI envolve a proteção de sistemas e dados contra ataques.",
      "subtópicos": {
        "Criptografia": "Processo de codificação de dados.",
        "Autenticação": "Processo de verificação de identidade."
      }
    }
  },
  "Hardware": {
    "1. Definição": {
      "descrição": "Hardware é a parte física de um computador ou sistema eletrônico.",
      "subtópicos": {
        "Componentes": "Placa-mãe, processador, memória, etc.",
        "Periféricos": "Dispositivos externos, como teclado e mouse."
      }
    }
  },
  "IoT (Internet das Coisas)": {
    "1. Definição": {
      "descrição": "IoT refere-se à interconexão de dispositivos físicos à internet, permitindo coletar e compartilhar dados.",
      "subtópicos": {
        "Sensores": "Dispositivos que captam dados do ambiente.",
        "Dispositivos Conectados": "Equipamentos que podem enviar e receber dados via internet."
      }
    }
  },
  "Inteligência Artificial": {
    "1. Aprendizado de Máquina": {
      "descrição": "O aprendizado de máquina é um subcampo da IA que se concentra no desenvolvimento de algoritmos que permitem que as máquinas aprendam com os dados e melhorem seu desempenho ao longo do tempo.",
      "tipos": {
        "Supervisionado": "O modelo aprende a partir de um conjunto de dados rotulado.",
        "Não supervisionado": "O modelo encontra padrões nos dados sem rótulos.",
        "Por Reforço": "O modelo aprende por meio de recompensas e punições."
      }
    },
    "2. Redes Neurais Artificiais": {
      "descrição": "São modelos inspirados no funcionamento do cérebro humano, compostos por camadas de neurônios artificiais.",
      "tipos": {
        "CNN": "Redes neurais convolucionais para reconhecimento de imagem.",
        "RNN": "Redes neurais recorrentes para processamento de sequências."
      }
    },
    "3. Processamento de Linguagem Natural": {
      "descrição": "Permite que as máquinas compreendam, interpretem e gerem linguagem humana.",
      "tarefas": {
        "Análise de Sentimento": "Determinação de sentimentos em textos.",
        "Tradução Automática": "Tradução de idiomas."
      }
    }
  }
}

@app.get('/sortear-tema')
def sortear_tema(json_data):
  topicos = list(json_data.keys())
  topico_sorteado = random.choice(topicos)
  return JSONResponse(content={"tema":topico_sorteado})

