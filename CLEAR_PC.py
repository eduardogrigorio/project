import subprocess
import os
import time

def faxina_geral_silenciosa():
    # 1. LISTA DE NAVEGADORES (Processos e Pastas)
    navegadores = {
        "Chrome": {"proc": "chrome.exe", "path": r'%LOCALAPPDATA%\Google\Chrome\User Data'},
        "Edge": {"proc": "msedge.exe", "path": r'%LOCALAPPDATA%\Microsoft\Edge\User Data'},
        "Opera": {"proc": "opera.exe", "path": r'%APPDATA%\Opera Software\Opera Stable'},
        "Opera_GX": {"proc": "opera.exe", "path": r'%APPDATA%\Opera Software\Opera GX Stable'}
    }

    # Executa a limpeza de cada navegador
    for nav, info in navegadores.items():
        try:
            # Fecha o navegador
            subprocess.run(f'taskkill /F /IM {info["proc"]} /T', shell=True, capture_output=True)
            time.sleep(1)
            # Deleta a pasta de dados
            pasta = os.path.expandvars(info["path"])
            if os.path.exists(pasta):
                subprocess.run(f'rd /s /q "{pasta}"', shell=True, capture_output=True)
        except:
            pass

    # 2. ESVAZIAR LIXEIRA
    # O comando PowerShell abaixo limpa a lixeira de todos os discos sem pedir confirmação
    try:
        subprocess.run('powershell.exe -Command "Clear-RecycleBin -Force -ErrorAction SilentlyContinue"', 
                       shell=True, capture_output=True)
    except:
        pass

    # 3. LIMPAR ARQUIVOS TEMPORÁRIOS DO WINDOWS
    # Isso apaga rastros de arquivos que você abriu ou baixou
    pastas_temp = [os.environ.get('TEMP'), r'C:\Windows\Temp']
    for temp in pastas_temp:
        try:
            if temp and os.path.exists(temp):
                subprocess.run(f'del /q /s /f "{temp}\*.*"', shell=True, capture_output=True)
        except:
            pass

if __name__ == "__main__":
    faxina_geral_silenciosa()