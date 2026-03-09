# 🛠️ Windows System & Browser Cleaner (SystemMaintenance)

Este repositório contém um script em Python desenvolvido para automatizar a manutenção de sistemas Windows. Ele realiza a limpeza profunda de dados de navegação, esvazia a lixeira e remove arquivos temporários do sistema e do usuário.

## 📌 Objetivo do Projeto
O script serve como estudo de automação para:
* Interação com o Sistema Operacional via `subprocess`.
* Manipulação de variáveis de ambiente (`os.path.expandvars`).
* Gerenciamento de processos e permissões no Windows.

---

## 🚀 Funcionalidades

### 1. Reset de Navegadores
O script identifica e encerra os processos dos navegadores **Chrome, Edge, Opera e Opera GX**. 
* **Ação:** Deleta a pasta `User Data` (Perfil do Usuário).
* **Resultado:** Remove histórico, cookies, senhas salvas e extensões, retornando o navegador ao estado original de instalação.

### 2. Esvaziamento da Lixeira
Utiliza comandos de **PowerShell** (`Clear-RecycleBin`) com o parâmetro `-Force` para garantir que a lixeira seja limpa sem interrupções.

### 3. Limpeza de Arquivos Temporários
Ataca as duas principais fontes de arquivos desnecessários:
* **Temp do Usuário (`%TEMP%`)**
* **Temp do Sistema (`C:\Windows\Temp`)**

---

## 🐍 1. O Código Fonte (`CLEAR_PC.py`)

O script utiliza bibliotecas nativas do Python, dispensando a necessidade de instalar dependências externas.

```python
import subprocess
import os
import time

def executar_limpeza_total():
    # MAPEAMENTO DE NAVEGADORES (Processos e Caminhos)
    navegadores = {
        "Chrome": {
            "proc": "chrome.exe", 
            "path": os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data')
        },
        "Edge": {
            "proc": "msedge.exe", 
            "path": os.path.expandvars(r'%LOCALAPPDATA%\Microsoft\Edge\User Data')
        },
        "Opera": {
            "proc": "opera.exe", 
            "path": os.path.expandvars(r'%APPDATA%\Opera Software\Opera Stable')
        },
        "Opera_GX": {
            "proc": "opera.exe", 
            "path": os.path.expandvars(r'%APPDATA%\Opera Software\Opera GX Stable')
        }
    }

    for nav, info in navegadores.items():
        try:
            # Encerra o navegador e subprocessos (/T)
            subprocess.run(f'taskkill /F /IM {info["proc"]} /T', shell=True, capture_output=True)
            time.sleep(1) # Pausa para liberação de arquivos
            
            if os.path.exists(info["path"]):
                subprocess.run(f'rd /s /q "{info["path"]}"', shell=True, capture_output=True)
        except:
            pass

    # LIMPEZA DA LIXEIRA
    try:
        subprocess.run('powershell.exe -Command "Clear-RecycleBin -Force -ErrorAction SilentlyContinue"', 
                       shell=True, capture_output=True)
    except:
        pass

    # LIMPEZA DE ARQUIVOS TEMPORÁRIOS
    pastas_temp = [os.environ.get('TEMP'), r'C:\Windows\Temp']
    for temp in pastas_temp:
        try:
            if temp and os.path.exists(temp):
                subprocess.run(f'del /q /s /f "{temp}\\*.*"', shell=True, capture_output=True)
        except:
            pass

if __name__ == "__main__":
    executar_limpeza_total()
