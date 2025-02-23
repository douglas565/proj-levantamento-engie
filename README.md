#Software de Gestão de Dados de Infraestrutura Urbana
Bem-vindo ao repositório do Software de Gestão de Dados de Infraestrutura Urbana! Este projeto foi desenvolvido para automatizar e otimizar o processo de levantamento e registro de dados relacionados a vias públicas, postes e suas características associadas. Com foco em eficiência, segurança e usabilidade, o software substitui métodos manuais, reduzindo erros e economizando tempo.

Funcionalidades Principais
Integração com Planilhas Excel:

Armazena dados em planilhas Excel (dados_preenchidos.xlsx e Cadastro RAAG.xlsx).

Cabeçalhos padronizados incluem campos como ID RAAG, Via, Bairro, Classificação e Coordenadas Geográficas.

Preenchimento Automático:

Preenche automaticamente campos como coordenadas, bairro, distância entre postes e classificação de vias com base no ID RAAG ou nome da via.

Validação em Tempo Real:

Valida campos obrigatórios antes do salvamento, garantindo a integridade dos dados.

Interface Responsiva:

Janela redimensionável que pode ser posicionada ao lado de outras ferramentas, como o Google Earth.

Permanece sempre à frente de outras janelas, evitando a necessidade de alternar entre aplicativos.

Preservação de Dados:

Mantém valores anteriores em campos como larguras de pistas e classificação, evitando redigitação em casos de padronização de vias.

Operações em Segundo Plano:

Salvamento e edição de dados são realizados em segundo plano, mantendo a interface gráfica responsiva.

Tecnologias Utilizadas
Linguagem: Python 3.9+

Bibliotecas Principais:

OpenPyXL: Manipulação de planilhas Excel.

Tkinter: Interface gráfica (GUI).

Logging: Registro de operações e erros.

Threading: Execução de operações em segundo plano.

Outras Bibliotecas:

JSON: Armazenamento de configurações.

Cryptography (futuro): Criptografia de dados.

Instalação e Uso
Pré-requisitos
Python 3.9 ou superior instalado.

Bibliotecas necessárias: openpyxl.

Como Executar
Clone este repositório:

bash
Copy
git clone https://github.com/seu-usuario/nome-do-repositorio.git
Navegue até a pasta do projeto:

bash
Copy
cd nome-do-repositorio
Instale as dependências:

bash
Copy
pip install openpyxl
Execute o software:

bash
Copy
python main.py
Estrutura do Projeto
Copy
nome-do-repositorio/
├── main.py                # Código principal do software
├── dados_preenchidos.xlsx  # Planilha de armazenamento de dados
├── Cadastro RAAG.xlsx      # Planilha de referência para coordenadas
├── config.json             # Arquivo de configurações
├── app.log                 # Arquivo de logs
├── README.md               # Este arquivo
└── requirements.txt        # Lista de dependências
Contribuição
Contribuições são bem-vindas! Se você deseja colaborar com o projeto, siga estas etapas:

Faça um fork do repositório.

Crie uma branch para sua feature:

bash
Copy
git checkout -b minha-feature
Commit suas alterações:

bash
Copy
git commit -m "Adicionando nova funcionalidade"
Envie as alterações para o repositório remoto:

bash
Copy
git push origin minha-feature
Abra um Pull Request.

Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

Contato
Se você tiver dúvidas, sugestões ou quiser entrar em contato, sinta-se à vontade para me enviar um e-mail:
📧 douglas.charqueiro@example.com
🔗 LinkedIn: linkedin.com/in/douglas-charqueiro
