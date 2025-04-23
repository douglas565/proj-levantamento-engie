# 🚀 Sistema de Gestão de Iluminação Pública

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Openpyxl](https://img.shields.io/badge/Openpyxl-3.0.9-green)
![Licença](https://img.shields.io/badge/Licença-MIT-orange)

Este projeto é uma aplicação desktop desenvolvida em Python para facilitar o preenchimento de planilhas Excel com base em dados de outras planilhas. Ele utiliza a biblioteca `tkinter` para a interface gráfica e `openpyxl` para manipulação de arquivos Excel. Ideal para quem precisa automatizar o preenchimento de dados de forma rápida e eficiente.

---

## 🌟 Funcionalidades

### 🛠️ Núcleo do Sistema

- **Preenchimento Automático Inteligente**
  - Coordenadas geográficas (Latitude/Longitude)
  - Classificação técnica de vias
  - Dados de bairros e distritos
  - Parâmetros técnicos (altura, projeção, recuo)

### 📊 Gestão de Dados

- **CRUD Completo**
  - Criação, leitura, atualização e exclusão de registros
  - Validação de dados em tempo real
  - Histórico de operações (app.log)

### 🔄 Integração

- **Importação/Exportação**
  - Compatível com planilhas Excel (.xlsx)
  - Exportação em CSV padronizado para integração com GIS
  - Sistema de cache para melhor desempenho

### 🖥️ Interface Avançada

- **Três Abas Organizadas**
  - Dados Gerais
  - Larguras e Ciclovia
  - Postes e Interferências
- **Navegação por Teclado**
  - `← →` para trocar abas
  - `Enter` para avançar campos
  - `Delete` para remover registros

---

## 🖥️ Como Utilizar

### Pré-requisitos
```bash
Python 3.8+
pip install openpyxl
```
Instalação e Execução
```bash
git clone https://github.com/seu-usuario/gestao-iluminacao-publica.git
```

## 📂 Estrutura do Projeto

| Arquivo/Pasta           | Descrição                                  |
|-------------------------|--------------------------------------------|
| `main.py`               | Código-fonte principal da aplicação        |
| `dados_preenchidos.xlsx`| Planilha de saída com dados processados    |
| `Cadastro RAAG.xlsx`    | Base de dados geográficos de referência    |
| `Classificação.xlsx`    | Classificação técnica das vias públicas    |
| `coordenadas_excel.csv` | Arquivo de exportação padronizado          |
| `config.json`           | Configurações persistentes do usuário      |
| `app.log`               | Registro de atividades e erros do sistema  |


## ⚙️ Requisitos para prenchimento automatico
 **Planilhas**   
  - Cadastro RAAG
  - Classificação
  - id_ippuc_coordenadas


## 📜 Licença
Este projeto está licenciado sob a Licença MIT.


## ✉️ Contato
Douglas Ramos Charqueiro

Email: douglasramos16@outlook.com

GitHub: douglas565
