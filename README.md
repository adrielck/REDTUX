# RedTux

**RedTux** é uma ferramenta multifuncional desenvolvida para fins educacionais e de pentest controlado. Ela integra uma variedade de utilitários para reconhecimento, exploração, enumeração de rede, exfiltração de dados e evasão básica.

⚠️ **Uso restrito a ambientes controlados com autorização explícita. O uso indevido pode ser ilegal.**

---

## 🔧 Tecnologias Utilizadas

- **Python 3**
- **Sublist3r** – Enumeração de subdomínios.
- **Pwntools** – Exploração de binários.
- **Paramiko** – Execução de comandos remotos via SSH.
- **Impacket (SMBConnection)** – Enumeração de compartilhamentos SMB.
- **Metasploit (via CLI)** – Execução de exploits com RPC via shell.
- **cURL** – Exfiltração de arquivos.
- **Colorama** – Estilização do terminal.

---

## 📂 Funcionalidades

1. **Reconhecimento de Subdomínios**  
   Usa o `sublist3r` para encontrar subdomínios do domínio alvo.

2. **Port Scan**  
   Verifica portas específicas (21, 22, 80, 443) se estão abertas usando sockets.

3. **Exploração com Pwntools**  
   Explora binários locais usando técnica de buffer overflow.

4. **Exploração via Metasploit RPC**  
   Automatiza o uso do `msfconsole` com payloads e parâmetros fornecidos.

5. **Execução Remota via SSH**  
   Usa `paramiko` para conectar-se via SSH e executar comandos.

6. **Enumeração SMB**  
   Enumera compartilhamentos SMB usando credenciais com a biblioteca `impacket`.

7. **Obfuscação de Payloads**  
   Codifica payloads em base64 para evasão simples.

8. **Exfiltração de Arquivos**  
   Envia arquivos para um servidor remoto via `curl`.

9. **Limpeza de Logs**  
   Remove logs básicos do sistema (`/var/log/*.log`).

---

## 🧪 Como Usar

### ⚙️ Requisitos

Antes de rodar o script, instale as dependências:

```bash
pip install pwntools paramiko colorama impacket
sudo apt install sublist3r curl metasploit-framework
```

### ▶️ Execução

```bash
python3 Redtux.py
```

Você verá um menu interativo com as opções de uso.

### 📘 Exemplo de Uso

**Exemplo: Port Scan**

```
Select option: 2
Target IP: 192.168.1.1
```

**Exemplo: Execução remota via SSH**

```
Select option: 5
Target IP: 192.168.1.100
Username: admin
Password: password123
Command: whoami
```

---

## 📌 Observações

- A função de exploração binária com `pwntools` pressupõe que o binário possui uma função `win` explorável por buffer overflow.
- O uso do `msfconsole` requer que o Metasploit esteja instalado e acessível via terminal.
- A exfiltração requer um servidor remoto que aceite uploads via `curl`.

---

## ⚠️ Aviso Legal

Este projeto é destinado **exclusivamente para aprendizado e testes em ambientes controlados**. O uso em sistemas sem permissão é ilegal e contra os Termos de Uso da maioria das redes e serviços.

> O autor e colaboradores não se responsabilizam por quaisquer danos causados pelo uso indevido desta ferramenta.

---


