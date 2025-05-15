# 🍽️ PROJETO ONG JARDIM ITAOCA

Sistema web desenvolvido para exibir, em tempo real, o cardápio de refeições oferecidas nos refeitórios da ONG Jardim Itaoca. A aplicação permite o cadastro e a visualização das refeições do dia por meio de uma interface simples e acessível, ideal para ser exibida em telas posicionadas no próprio refeitório. Desenvolvido com Flask (Python), SQLite e HTML, o sistema facilita a comunicação clara e rápida dos alimentos servidos aos beneficiários da instituição.

---

## 📦 Funcionalidades

- Cadastro das três principais refeições do dia (café da manhã, almoço e jantar)
- Visualização clara e direta do cardápio diário
- Interface responsiva e otimizada para telas fixas (modo TV)
- Painel administrativo para atualização do cardápio

---

## 🚀 Tecnologias utilizadas

- Python 3.x
- Flask
- SQLite
- HTML5 + CSS3 (Bootstrap)
- AWS Elastic Beanstalk (deploy)

---

## ⚙️ Como rodar o projeto localmente

```bash
# Clone o repositório
git clone https://github.com/seuusuario/nomedoprojeto.git

# Acesse a pasta do projeto
cd nomedoprojeto

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Rode a aplicação
python app.py
