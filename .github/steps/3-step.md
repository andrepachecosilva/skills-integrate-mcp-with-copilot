## Passo 3: Resolver issues com Modo Agente e Servidor GitHub MCP

Ótimo trabalho fazendo essa pesquisa e encontrando uma oportunidade potencial de colaboração.
Não apenas encontramos algumas ideias novas para ajudar a organizar atividades extracurriculares, mas fizemos tudo isso rapidamente também.

Muito tempo para focar nas coisas divertidas, como ensinar nossos estudantes incríveis! 🌱

Falando nisso, parece que os professores também estiveram ativos.
Parece que eles enviaram alguns bugs e solicitações! Perfeito! 🚀

Agora, vamos usar as ferramentas do nosso servidor MCP e o Copilot para fazer um pouco de triagem e realizar algum trabalho.

### :keyboard: Atividade: Implementar facilmente uma issue importante

1. Certifique-se de que o painel **Copilot Chat** está aberto e o modo **Agente** está selecionado. Verifique se as ferramentas do servidor MCP também ainda estão disponíveis.

1. Pergunte ao Copilot sobre as issues abertas neste repositório.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Quantas issues abertas existem no meu repositório?
   > ```

   > 🪧 **Nota:** Verifique se a ferramenta List Issues é chamada com parâmetros adequados.

1. Peça ao Copilot para resumir as issues importantes.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Oh não. São muitas para mim! Por favor, obtenha a lista de issues,
   > revise as descrições e comentários, e escolha as 3 mais importantes.
   > ```

   <details>
   <summary> <b> 💡 Dica:</b> Pré-autorizar o uso de ferramentas</summary><br/>

   Se o Copilot usa uma ferramenta frequentemente, você pode conceder permissão proativamente para o resto da sessão de conversa.

   <img width="350" src="https://github.com/user-attachments/assets/d741191e-4d98-489d-92d2-f1069fd6c34e"/>

   </details>

1. Revise as issues sugeridas. Se o Copilot não deu uma recomendação específica, tente fornecer algum feedback para refinar os resultados.

1. Com a lista refinada, peça ao Copilot para implementar uma issue. **A Mona não avaliará se as mudanças funcionam, apenas se uma tentativa foi feita.**

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > #codebase Vamos fazer a primeira. Siga estes passos:
   > 1. Faça checkout de uma nova branch local para fazer nossas mudanças.
   > 2. Faça as mudanças e depois confirme comigo se elas parecem corretas.
   > 3. Faça push das mudanças e inicie um pull request.
   > ```

   > ⚠️ **Aviso:** Sempre verifique as ações que o Copilot está pedindo para executar, especialmente com as capacidades externas fornecidas por um servidor MCP, que provavelmente não têm opção de desfazer.

1. Uma vez que o pull request for criado, a Mona começará a verificar seu trabalho. Dê um momento para ela e fique de olho nos comentários. Você verá ela responder com informações de progresso e o próximo passo!

<details>
<summary>Tendo problemas?</summary><br/>

- Se as ferramentas não estão sendo solicitadas, verifique se sua configuração MCP está correta.
- Se o Copilot não consegue recuperar resultados, verifique se você está usando o token deste Codespace ou um Personal Access Token (PAT) com permissões apropriadas. Por padrão, o token do codespace que estamos usando só tem acesso a este repositório.

</details>
