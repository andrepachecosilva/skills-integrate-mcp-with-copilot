## Passo 1: Introdução ao MCP e configuração do ambiente

<img width="150" align="right" alt="copilot logo" src="https://github.com/user-attachments/assets/4d22496d-850b-4785-aafe-11cba03cd5f2" />

No exercício [Primeiros Passos com GitHub Copilot](https://github.com/skills/getting-started-with-github-copilot), fomos apresentados ao site de atividades extracurriculares da Mergington High School, que permitia aos estudantes se inscreverem em eventos.

E agora temos um problema... mas... é um bom problema! Mais professores estão pedindo para usá-lo! 🎉

Nossos colegas professores têm muitas ideias, mas parece que não conseguimos acompanhar todas as solicitações! 😮 Para resolver esse problema, vamos dar um upgrade ao GitHub Copilot habilitando o Model Context Protocol (MCP). Para ser mais específico, vamos adicionar o servidor GitHub MCP, que habilitará um fluxo de trabalho combinado de gerenciamento de issues e upgrades do site. 🧑‍🚀

Vamos começar!

### O que é Model Context Protocol (MCP)?

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) é frequentemente chamado de "USB-C para IA" - um conector universal que permite ao GitHub Copilot (e outras ferramentas de IA) interagir perfeitamente com outros serviços.

Essencialmente, é uma forma de descrever as capacidades e requisitos de um serviço, para que ferramentas de IA possam facilmente determinar quais métodos usar e fornecer os parâmetros com precisão. Um servidor MCP está fornecendo essa interface.

```mermaid
graph LR
    A[Developer] -->|Uses| B[GitHub Copilot]
    B -->|Unified API| MCP[Model Context Protocol]

    MCP <-->|Unique API| C[(GitHub)]
    MCP <-->|Unique API| D[(Slack)]
    MCP <-->|Unique API| E[(Figma)]

    style B fill:#4CAF50,stroke:#333,stroke-width:2px

    subgraph "Menos Mudança de Contexto, Mais Programação"
        B
        MCP
        C
        D
        E

    end
```

### :keyboard: Atividade: Conheça seu ambiente

Antes de mergulharmos no MCP, vamos iniciar nosso ambiente de desenvolvimento e nos refamiliarizar com a aplicação de atividades extracurriculares.

1. Clique com o botão direito no botão abaixo para abrir a página **Criar Codespace** em uma nova aba. Use a configuração padrão.

   [![Abrir no GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

1. Valide se as extensões **Copilot Chat** e **Python** estão instaladas e habilitadas.

   <img width="300" alt="copilot extension for VS Code" src="https://github.com/user-attachments/assets/ef1ef984-17fc-4b20-a9a6-65a866def468" /><br/>
   <img width="300" alt="python extension for VS Code" src="https://github.com/user-attachments/assets/3040c0f5-1658-47e2-a439-20504a384f77" />

1. Verifique se nossa aplicação roda antes da modificação. Na barra lateral esquerda, selecione a aba **Executar e Depurar** e então pressione o ícone **Iniciar Depuração**.

   <details>
   <summary>📸 Mostrar captura de tela</summary><br/>

   <img width="300" alt="run and debug" src="https://github.com/user-attachments/assets/50b27f2a-5eab-4827-9343-ab5bce62357e" />

   </details>

   <details>
   <summary>🤷 Tendo problemas?</summary><br/>

   Se a área **Executar e Depurar** estiver vazia, tente recarregar o VS Code: Abra a paleta de comandos (`Ctrl`+`Shift`+`P`) e procure por `Developer: Reload Window`.

   <img width="300" alt="empty run and debug panel" src="https://github.com/user-attachments/assets/0dbf1407-3a97-401a-a630-f462697082d6" />

   </details>

1. Use a aba **Portas** para encontrar o endereço da página web, abra-a e verifique se está funcionando.

   <details>
   <summary>📸 Mostrar captura de tela</summary><br/>

   <img width="350" alt="ports tab" src="https://github.com/user-attachments/assets/8d24d6b5-202d-4109-8174-2f0d1e4d8d44" />

   ![Screenshot of Mergington High School WebApp](https://github.com/user-attachments/assets/5cb88d53-d948-457e-9f4b-403d697fa93a)

   </details>

### :keyboard: Atividade: Adicionar o servidor GitHub MCP

1. Dentro do seu codespace, abra o painel **Copilot Chat** e verifique se o modo **Agente** está selecionado.

   <img width="200" alt="image" src="https://github.com/user-attachments/assets/201e08ab-14a0-48bf-824e-ba4f8f43f8ab" />

   <details>
   <summary>Modo Agente ausente?</summary><br/>

   - Verifique se o VS Code está pelo menos na versão `v1.99.0`.
   - Verifique se a extensão Copilot está pelo menos na versão `v1.296.0`.
   - Verifique se o modo Agente está habilitado nas suas [configurações de usuário ou workspace](https://code.visualstudio.com/docs/configure/settings#_workspace-settings).

      <img width="300" alt="image" src="https://github.com/user-attachments/assets/407a79dd-707e-471b-b56b-1938aece4ad8" />

   </details>

1. Dentro do seu codespace, navegue até a pasta `.vscode` e crie um novo arquivo chamado `mcp.json`. Cole o seguinte conteúdo:

   📄 **.vscode/mcp.json**

   ```json
   {
     "servers": {
       "github": {
         "type": "http",
         "url": "https://api.githubcopilot.com/mcp/"
       }
     }
   }
   ```

1. No arquivo `.vscode/mcp.json`, clique no botão **Iniciar** e aceite o prompt para autenticar com o GitHub. Isso acabou de informar o GitHub Copilot sobre as capacidades do servidor MCP.

   <img width="350" alt="mcp.json file showing start button" src="https://github.com/user-attachments/assets/0361a2ff-3fb3-428a-9cbc-d004a618afc8" />

   <img width="350" alt="allow authentication prompt" src="https://github.com/user-attachments/assets/e28b2b2b-7ac2-461e-9df8-e206dc888afa" /><br/>

   <img width="350" alt="mp.json file showing running server" src="https://github.com/user-attachments/assets/f61937a1-dcc3-49d6-bf7c-9a9108b8e2ae" />

1. No painel lateral do Copilot, clique no **ícone 🛠️** para mostrar as capacidades adicionais.

   <img width="350" alt="image" src="https://github.com/user-attachments/assets/b1be8b80-c69c-4da5-9aea-4bbaa1c6de10" />

   <img width="350" alt="image" src="https://github.com/user-attachments/assets/99178d1b-adbe-4cf4-ab9c-3a4d29918a13" />

1. **Faça commit** e **push** do arquivo `.vscode/mcp.json` para a branch `main`.

   > 🪧 **Nota:** Fazer push diretamente para `main` não é uma prática recomendada. É apenas para simplificar este exercício.

1. Agora que sua configuração do servidor MCP foi enviada para o GitHub, a Mona já deve estar ocupada verificando seu trabalho. Dê um momento para ela e fique de olho nos comentários. Você verá ela responder com informações de progresso e a próxima lição.

> [!NOTE]
> Os próximos passos envolverão criar issues do GitHub. Se você quiser evitar emails de notificação, pode parar de acompanhar o repositório.

<details>
<summary>Tendo problemas?</summary><br/>

Certifique-se de que:

- Seu arquivo `.vscode/mcp.json` é similar ao exemplo fornecido.
- Você fez push das mudanças para a branch `main`.

</details>
