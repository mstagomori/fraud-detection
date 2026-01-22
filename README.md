# 🕵️‍♂️ Sistema de Detecção de Fraudes com Machine Learning

## 📌 Objetivos do Projeto

- Análise Exploratória de dados de transações bancárias
- Pré-processamento de dados
- Criar Pipeline de pre-processamento e treinamento de modelo de machine learning
- Exportar modelo treinado (pickle)
- Criar web app com Streamlit que execute o modelo treinado para realizar predições



## 🧠 Etapas do Projeto

### 1. Pré-processamento de Dados
- Tratamento de valores ausentes
- One-hot-encoding para variáveis categóricas
- Normalização / padronização de variáveis numéricas
- Separação em conjuntos de treino, validação e teste


### 2. Análise Exploratória de Dados (EDA)
- Distribuição de Fraude x Não-Fraude
- Distribuição por tipo de transação
- Taxa de fraude por tipo de transação
- Analise de quantidade transferida

### 3. Treinamento do Modelo
- Treinamento básico apenas para criar o Pipeline


### 4. Avaliação do Modelo
- Breve avaliação do modelo



### 5. Aplicação Streamlit
- Criação de um **aplicativo web interativo**
- Upload ou inserção manual de novos dados
- Predição em tempo real de possíveis fraudes
- Exibição da probabilidade de fraude
- Interface simples e intuitiva



## 🖥️ Tecnologias Utilizadas

- **Python**
- **Pandas / NumPy**
- **Scikit-learn**
- **Matplotlib / Seaborn / Plotly**
- **Imbalanced-learn**
- **Streamlit**
- **Joblib / Pickle**

---

## 📂 Estrutura do Projeto

```text
├── data/
│   ├── data.csv
│
├── notebooks/
│   ├── analise.ipynb
│
├── app/
│   └── fraud_detection.py              # Aplicação Streamlit
│
├── models/
│   └── fraud_detection_pipeline.pkl           # Pipeline de pre-processamento e treinamento do modelo
│
├── requirements.txt
├── README.md
└── .gitignore
