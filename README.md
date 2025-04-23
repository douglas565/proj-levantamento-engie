# 🚀 Sistema de Gestão de Iluminação Pública

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Openpyxl](https://img.shields.io/badge/Openpyxl-3.0.9-green)
![Licença](https://img.shields.io/badge/Licença-MIT-orange)

Aplicação desktop para automatizar o preenchimento e gestão de dados de iluminação pública, desenvolvida para a ENGIE Soluções.

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
cd gestao-iluminacao-publica
python main.py
Fluxo de Trabalho
Preencha os campos obrigatórios (IDs RAAG/IPPUC)

Dados complementares são autocompletados

Navegue entre abas com ← → do teclado

Use Enter para avançar entre campos

Exporte dados para CSV com 1 clique

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
# Exemplo de saída no CSV
ID_RAAG;ID_IPPUC;LATITUDE;LONGITUDE
66455;3456;-25.5924702193806;-49.3349638091506
Dependências Especiais
Biblioteca	Versão	Função
Openpyxl	3.0.9	Manipulação avançada de Excel
Tkinter	0.1.0	Interface gráfica (GUI)


## 📜 Licença
Este projeto está licenciado sob a Licença MIT.


## ✉️ Contato
Douglas Ramos Charqueiro
Email: douglasramos16@outlook.com
GitHub: douglas565
