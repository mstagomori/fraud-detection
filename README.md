# 🕵️‍♂️ Sistema de Detecção de Fraudes com Machine Learning

Este projeto tem como objetivo o desenvolvimento de um **sistema completo de Machine Learning para detecção de fraudes**, cobrindo todas as etapas do ciclo de vida de um modelo: desde o **pré-processamento e análise dos dados**, passando pelo **treinamento e avaliação do modelo**, até a **disponibilização de um aplicativo web interativo, criado com Streamlit,** para predição de novos casos.



## 📌 Objetivos do Projeto

- Realizar **pré-processamento e limpeza de dados**
- Analisar variáveis e identificar padrões associados a fraudes
- Treinar e comparar modelos de Machine Learning
- Avaliar o desempenho dos modelos com métricas adequadas
- Criar um **aplicativo web** para predição de novos casos de fraude
- Disponibilizar uma solução prática e interativa para uso do modelo treinado



## 🧠 Etapas do Projeto

### 1. Pré-processamento de Dados
- Tratamento de valores ausentes
- Codificação de variáveis categóricas
- Normalização / padronização de variáveis numéricas
- Balanceamento de classes (ex: SMOTE, undersampling)
- Separação em conjuntos de treino, validação e teste



### 2. Análise Exploratória de Dados (EDA)
- Análise estatística das variáveis
- Visualização de distribuições e correlações
- Identificação de variáveis mais relevantes para fraude
- Detecção de outliers e padrões anômalos



### 3. Treinamento do Modelo
- Teste de diferentes algoritmos (ex: Logistic Regression, Random Forest, XGBoost, etc.)
- Ajuste de hiperparâmetros
- Validação cruzada
- Seleção do melhor modelo


### 4. Avaliação do Modelo
- Métricas utilizadas:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
  - ROC-AUC
- Análise da matriz de confusão
- Avaliação de trade-offs entre falsos positivos e falsos negativos



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
│   ├── raw/                # Dados brutos
│   ├── processed/          # Dados tratados
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04_model_evaluation.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── features.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── app/
│   └── app.py              # Aplicação Streamlit
│
├── models/
│   └── model.pkl           # Modelo treinado
│
├── requirements.txt
├── README.md
└── .gitignore
