# 🛠️ Windows System & Browser Cleaner (Automação de Limpeza)

Este repositório contém um script em Python desenvolvido para automatizar a manutenção de sistemas Windows. Ele realiza a limpeza de dados de navegação, esvazia a lixeira e remove arquivos temporários do sistema e do usuário.

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
Utiliza comandos de **PowerShell** (`Clear-RecycleBin`) com o parâmetro `-Force` para garantir que a lixeira seja limpa sem interrupções ou janelas de confirmação.

### 3. Limpeza de Arquivos Temporários
Ataca as duas principais fontes de arquivos desnecessários:
* **Temp do Usuário (`%TEMP%`)**
* **Temp do Sistema (`C:\Windows\Temp`)**

---

## 📦 Como converter para Executável (.exe)

Para transformar este script em um arquivo executável que rode em qualquer Windows (mesmo sem Python instalado), siga os passos abaixo:

### 1. Instale o PyInstaller
No seu terminal, execute:
```bash
pip install pyinstaller
