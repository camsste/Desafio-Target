# DESAFIO TARGET

Este projeto implementa três funcionalidades principais:

- Cálculo de comissões por vendedor  
- Sistema de movimentação de estoque  
- Cálculo de juros simples  
- Interface Web simples para executar tudo pelo navegador

O objetivo é fornecer uma solução completa e organizada, com backend em Python e frontend em HTML/JS.

---

## 📁 Estrutura do Projeto

```
desafio_project/
├─ data/
│  ├─ vendas.json
│  └─ estoque.json
├─ src/
│  ├─ commissions.py
│  ├─ stock.py
│  └─ interest.py
├─ web/
│  └─ index.html
├─ main.py
└─ requirements.txt
```

---

## 🧪 Como executar o BACKEND (Python)

Abra o terminal na pasta do projeto:

```
cd desafio_project
```

### ▶️ Calcular comissões:

```
python main.py comissoes
```

### ▶️ Movimentar estoque:

```
python main.py movimentar --codigo 101 --quantidade -10 --descricao "Saída por venda"
```

### ▶️ Calcular juros simples:

```
python main.py juros --valor 1000 --vencimento 2025-11-01
```

---

## 🌐 Como rodar a INTERFACE WEB

A interface está na pasta:

```
desafio_project/web/index.html
```

### ✔️ Forma mais simples

Abra o arquivo `index.html` clicando duas vezes.  
O navegador abrirá a interface automaticamente.

### ✔️ Rodar com servidor local (opcional)

```
cd desafio_project/web
python -m http.server 8080
```

Depois acesse no navegador:

```
http://localhost:8080
```

---

## 📂 Uso dos arquivos JSON no Frontend

A interface web pedirá para você carregar:

- `vendas.json` para calcular comissões
- `estoque.json` para fazer movimentações

Eles estão na pasta:

```
desafio_project/data/
```

Basta selecionar os arquivos quando o navegador pedir.

---

## 📘 Tecnologias utilizadas

### Backend:
- Python 3 (somente bibliotecas padrão)

### Frontend:
- HTML5  
- CSS3  
- JavaScript puro  

Nenhum framework externo é necessário.

---

## 🚀 Possíveis melhorias

Se quiser, posso adicionar:

- API em Flask/FastAPI
- Histórico de movimentações
- Dashboard com gráficos
- Layout com Tailwind ou Bootstrap
- Versão em React ou Next.js

---

## ✨ Autoria

Desenvolvido com foco em aprendizagem e organização profissional do desafio **DESAFIO TARGET**.

