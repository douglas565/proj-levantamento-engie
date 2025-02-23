# 🚀 Sistema de Preenchimento de Planilhas Automático

Este projeto é uma aplicação desktop desenvolvida em Python para facilitar o preenchimento de planilhas Excel com base em dados de outras planilhas. Ele utiliza a biblioteca `tkinter` para a interface gráfica e `openpyxl` para manipulação de arquivos Excel. Ideal para quem precisa automatizar o preenchimento de dados de forma rápida e eficiente.

---

## 🛠️ Funcionalidades

- **Preenchimento Automático**: Preenche automaticamente campos como coordenadas, bairro, distância entre postes, altura, projeção e recuo com base no ID RAAG.
- **Navegação Intuitiva**: Use as setas do teclado (`←` e `→`) para alternar entre as abas.
- **Salvamento Automático**: Ao chegar ao último campo da última aba, os dados são salvos automaticamente.
- **Validação de Campos**: Verifica se os campos obrigatórios foram preenchidos antes de salvar.
- **Filtro de Vias**: Busca e filtra vias e IDs RAAG na seção lateral.
- **Edição e Exclusão**: Permite editar e excluir registros existentes diretamente na interface.

---

## 📦 Como Usar

### Pré-requisitos
- Python 3.x instalado.
- Bibliotecas necessárias: `tkinter`, `openpyxl`.

### Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git


Navegue até o diretório do projeto:

bash
Copy
cd nome-do-repositorio
Instale as dependências:

bash
Copy
pip install openpyxl
Executando o Projeto
Execute o script Python:

bash
Copy
python main.py
Siga as instruções na interface gráfica:

Preencha os campos obrigatórios.

Use as setas do teclado (← e →) para alternar entre as abas.

Pressione Enter para avançar entre os campos.

Ao chegar ao último campo da última aba, os dados serão salvos automaticamente.

---


## 🗂️ Estrutura do Projeto

### Explicação dos Arquivos
- **`main.py`**: Contém o código principal da aplicação.
- **`dados_preenchidos.xlsx`**: Planilha gerada automaticamente com os dados preenchidos.
- **`Cadastro RAAG.xlsx`**: Planilha de entrada com dados de coordenadas, bairro, distância entre postes, altura, projeção e recuo.
- **`Classificação.xlsx`**: Planilha de entrada com dados de classificação das vias.
- **`config.json`**: Arquivo de configuração gerado automaticamente para armazenar o nome da última planilha usada.
- **`app.log`**: Arquivo de log gerado automaticamente para registrar eventos do sistema.
- **`README.md`**: Este arquivo, que descreve o projeto.
---

## 📋 Requisitos
Planilhas de Entrada:

Cadastro RAAG.xlsx: Deve conter os dados de coordenadas, bairro, distância entre postes, altura, projeção e recuo.

Classificação.xlsx: Deve conter os dados de classificação das vias.

Planilha de Saída:

dados_preenchidos.xlsx: Gerada automaticamente pelo programa.

## 📄 Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

---

## 📞 Contato
Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:

Nome: Douglas Ramos Charqueiro

E-mail: douglasramos16@outlook.com

GitHub: douglas565



