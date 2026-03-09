# 🛠️ Windows System & Browser Cleaner (Automação de Limpeza)

Este projeto contém um script em Python projetado para automatizar a manutenção preventiva do Windows, focando na remoção de arquivos temporários, limpeza de lixeira e reset completo de perfis de navegadores.

## 📌 Objetivo do Estudo
O script demonstra o uso da biblioteca `subprocess` para interagir com o Sistema Operacional, manipulação de variáveis de ambiente com `os` e o gerenciamento de processos ativos no Windows.

---

## 🚀 Funcionalidades Detalhadas

O script executa uma limpeza profunda dividida em três frentes:

### 1. Reset de Navegadores (Chrome, Edge, Opera)
Diferente de uma limpeza comum de cache, este script:
* **Encerra os Processos:** Utiliza o comando `taskkill` para garantir que o navegador não esteja bloqueando os arquivos.
* **Deleta o Perfil de Usuário:** Remove a pasta `User Data`, o que resulta na exclusão de:
    * Histórico de navegação e Cookies.
    * Senhas salvas e extensões.
    * Cache de imagens e arquivos.



### 2. Esvaziamento da Lixeira
Integração com o **PowerShell** para executar o comando `Clear-RecycleBin`.
* O parâmetro `-Force` é utilizado para que a limpeza seja silenciosa (sem janelas de confirmação).

### 3. Limpeza de Arquivos Temporários
Limpa as duas principais pastas de "lixo" do sistema:
* **%TEMP% (Usuário):** Arquivos temporários de instalações e aplicativos do usuário logado.
* **C:\Windows\Temp (Sistema):** Arquivos temporários gerados pelo próprio Windows.

---

## 💻 Explicação Técnica do Código

### Bibliotecas Utilizadas
* `os`: Para mapear os caminhos das pastas de forma dinâmica (funciona em qualquer usuário).
* `subprocess`: Para enviar comandos de terminal (CMD/PowerShell) diretamente pelo Python.
* `time`: Para dar um intervalo (delay) necessário entre fechar o navegador e deletar os arquivos.

### Comandos de Terminal Implementados
| Comando | Função |
| :--- | :--- |
| `taskkill /F /IM` | Força o fechamento de um programa pelo nome da imagem. |
| `rd /s /q` | Remove diretórios e subdiretórios de forma silenciosa (Quiet mode). |
| `del /q /s /f` | Deleta arquivos específicos de forma forçada, mesmo se forem somente leitura. |



---

## ⚠️ Avisos Importantes

> [!CAUTION]
> **Perda de Dados:** Este script é agressivo. Ao deletar as pastas de "User Data", você perderá todas as configurações e logins nos navegadores listados.

> [!IMPORTANT]
> **Privilégios de Administrador:** Para que a limpeza da pasta `C:\Windows\Temp` e o encerramento de processos funcionem corretamente, o script deve ser executado como **Administrador**.

---

## 🛠️ Como Executar

1. Certifique-se de ter o Python instalado.
2. Abra o CMD ou PowerShell como Administrador.
3. Execute o comando:
   ```bash
   python nome_do_arquivo.py
