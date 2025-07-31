## Passo 2: Modo Agente e um Servidor MCP para GitHub

Ótimo trabalho! Você acabou de conectar seu primeiro servidor MCP ao GitHub Copilot! 🎉

🚨 Parece que os professores continuam enviando bugs e solicitações! Tantas ideias boas! Provavelmente deveríamos analisá-las e começar a pesquisar outros upgrades.

Felizmente, com um servidor MCP para GitHub, fazer triagem destes e até fazer algumas pesquisas para nos adiantarmos deve ser bem rápido! 🕵️

### Como usamos as ferramentas de um servidor MCP?

Boa notícia! Da mesma forma que você normalmente interage com o Copilot, linguagem natural. Apenas tenha em mente as capacidades disponíveis e quaisquer restrições de permissão do seu token.

Então, com o Servidor MCP disponível, agora podemos pedir ao Copilot coisas além do nosso código. Aqui estão algumas ideias para imaginar as possibilidades:

Por exemplo:

- Buscar issues considerando descrição, comentários e curtidas.
- Abrir, atualizar ou fechar issues em outro repositório.
- Comparar repositórios.
- Aprender sobre outros autores com quem você está trabalhando.
- Recuperar uma issue, fazer mudanças em uma branch e iniciar um pull request.

Não é legal?! Agora vamos fazer isso! 👩‍🚀

### :keyboard: Atividade: Encontrar e salvar ideias rapidamente

1. Feche todos os arquivos abertos dentro do seu codespace. Isso ajudará a reduzir contexto desnecessário.

1. Certifique-se de que o painel **Copilot Chat** está aberto e o modo **Agente** está selecionado. Verifique se as ferramentas do servidor MCP também ainda estão disponíveis.

1. Peça ao Copilot para buscar no GitHub projetos similares a este.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Buscar por outros repositórios para organizar atividades extracurriculares
   > ```

1. Quando uma ferramenta MCP for necessária, o Copilot pedirá permissão. **Verifique a solicitação** e modifique se necessário, então clique em **Continuar**.

   <img width="250" alt="request permission dialog" src="https://github.com/user-attachments/assets/229473af-c206-47a4-b356-943b9c9bd946" />

1. Peça ao Copilot para descrever um dos projetos. Explore até encontrar algo que você goste.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Por favor, olhe o código da 3ª opção e me dê uma descrição detalhada das funcionalidades.
   > ```

1. Use o Copilot para comparar e gerar ideias de melhorias.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Por favor, compare essas funcionalidades com nosso projeto. Quais seriam novas?
   > ```

1. Legal! Vamos fazer o Copilot criar issues para salvar essas ideias.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Eu gosto disso. Vamos criar issues para essas no meu repositório.
   > ```

1. O Copilot pedirá permissão para criar issues no seu repositório. Clique em **Continuar** para cada nova issue. Lembrete: **verifique a solicitação** antes de executar.

   <img width="250" alt="request permission dialog" src="https://github.com/user-attachments/assets/52635294-950a-4168-b71e-498eb769f3af" />

1. Como terminamos de pesquisar, vamos finalizar esta sessão de chat para limpar o contexto. No topo do painel **Copilot Chat**, clique no ícone **Novo Chat** (sinal de mais).

1. Com as novas issues criadas, a Mona já deve estar ocupada verificando seu trabalho. Dê um momento para ela e fique de olho nos comentários. Você verá ela responder com informações de progresso e a próxima lição.


> [!NOTE]
> O cenário do Model Context Protocol (MCP) está evoluindo rapidamente. Muitos servidores, incluindo o [Servidor GitHub MCP Oficial](https://github.com/github/github-mcp-server) estão em desenvolvimento ativo e não têm paridade completa com suas APIs estáveis.
