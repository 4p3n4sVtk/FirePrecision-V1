# FirePrecision-V1
## :warning: Alerta legais

Este projeto foi desenvolvido com fins educacionais e deve ser utilizado **apenas por pessoas que possuem pleno conhecimento das implicações legais e éticas de seus atos**. O uso inadequado deste software pode acarretar em consequências legais, e a responsabilidade pelo uso é inteiramente do usuário. A utilização deste projeto é estritamente restrita a **ambientes controlados e para fins de utilidade legal, como investigações digitais autorizadas**.


## 🚀 Funcionalidades

- Captura de localização com alta precisão (GPS, WiFi, IP)
- Tela Fake personalizáveis
- Captura de logs automatico 'log/captures.txt'
  IP, User-Agent, Acess time
- Armazenamento em banco de dados SQLite
- Redirecionamento 1nv!s!vel

## ⚙️ Instalação

1. Clone o repositório:
```bash
 git clone https://github.com/4p3n4sVtk/FirePrecision-V1.git
 cd FirePrecision-V1
```

2. atualize e baixe python:
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

3. Utilize um ambiente py virtual para isolar as dependencias:
```bash
python3 -m venv venv
source venv/bin/activate # para desativar 'deactivate'
```

4. Instale as dependencias:
```bash
pip install -r requirements.txt
pip list # verifica as dependencias
pip freeze > requirements.txt  # Atualiza com os pacotes exatos do venv
```
4. Ative o ngrok e inicie a ferramenta:
```bash
ngrok start --all
python3 FirePrecision-V1.py
```

## Obs Carregue seu token pessoal do ngrok em um .env
