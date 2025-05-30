# REDTUX - Red Team Automation Toolkit

REDTUX é um toolkit interativo avançado para Red Team, desenvolvido em Python. Ele automatiza as principais etapas de um ataque, como reconhecimento, exploração, movimentação lateral, exfiltração e limpeza de rastros.

---

## 🚀 Funcionalidades

- **Reconhecimento:** Enumeração de subdomínios e varredura de portas.
- **Exploração:** Automação de exploits com `pwntools` e integração com Metasploit RPC.
- **Movimentação lateral:** Acesso remoto e enumeração de shares via `Impacket`.
- **Evasão:** Ofuscação de payloads em Base64.
- **Exfiltração:** Transferência de arquivos via `curl`.
- **Limpeza de rastros:** Remoção de logs em sistemas Linux.

---

## 🛠️ Tecnologias e Bibliotecas

- **Python 3.x**
- `paramiko`
- `colorama`
- `pwntools`
- `impacket`
- `subprocess`, `socket`, `os`
- `Metasploit Framework` com RPC habilitado
- `Sublist3r` para enumeração de subdomínios
- `Nmap` para escaneamento opcional de portas

---

## 📦 Instalação

```bash
pip install paramiko colorama pwntools impacket
sudo apt install nmap
git clone https://github.com/aboul3la/Sublist3r.git
