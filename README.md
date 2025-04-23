# 🚀 Sistema de Gestão de Iluminação Pública

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Openpyxl](https://img.shields.io/badge/Openpyxl-3.0.9-green)
![Licença](https://img.shields.io/badge/Licença-MIT-orange)

Este projeto é uma aplicação desktop desenvolvida em Python para facilitar o preenchimento de planilhas Excel com base em dados de outras planilhas. Ele utiliza a biblioteca `tkinter` para a interface gráfica e `openpyxl` para manipulação de arquivos Excel. Ideal para quem precisa automatizar o preenchimento de dados de forma rápida e eficiente.

---

## 🛠️ Funcionalidades Principais

### ✨ Recursos Essenciais
- **Preenchimento Automático** de coordenadas, bairro, distâncias e outros campos via ID RAAG/IPPUC
- **Validação Inteligente** de campos obrigatórios e formatos
- **Interface Intuitiva** com 3 abas organizadas por categorias
- **Navegação por Teclado** (← → para trocar abas, Enter para avançar campos)

### 📤 Novos Recursos de Exportação
- **Exportação para CSV** com colunas específicas:
  - ID RAAG | ID IPPUC | LATITUDE | LONGITUDE
  - Delimitador `;` para compatibilidade com Excel (PT-BR)
  - Cabeçalho formatado para fácil identificação

### 🔄 Gestão de Dados
- Busca e filtro de vias/IDs RAAG na sidebar
- Edição e exclusão de registros existentes
- Logs detalhados de operações (`app.log`)
- Criação automática de nova planilha na primeira execução

---

## 🖥️ Como Utilizar

### Pré-requisitos
```bash
Python 3.8+
pip install openpyxl
Instalação e Execução
bash
git clone https://github.com/seu-usuario/gestao-iluminacao-publica.git
```

## 🗂️ Estrutura de Arquivos
Arquivo/Pasta	Descrição
main.py	Código-fonte principal
dados_preenchidos.xlsx	Planilha principal de saída
Cadastro RAAG.xlsx	Base de dados geográficos
Classificação.xlsx	Classificação técnica das vias
coordenadas_excel.csv	Exportação padronizada para integrações
config.json	Configurações persistentes do usuário


## ⚙️ Configuração Avançada
Formatos de Exportação CSV
python


## 📜 Licença
Este projeto está licenciado sob a Licença MIT.


## ✉️ Contato
Douglas Ramos Charqueiro
Email: douglasramos16@outlook.com
GitHub: douglas565
