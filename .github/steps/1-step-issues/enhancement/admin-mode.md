# Modo Administrador

## Problema

Os estudantes estão removendo uns aos outros para liberar espaço para eles mesmos nas atividades.

## Solução Recomendada

Adicionar um ícone de usuário no canto superior direito. Quando clicado, mostra um botão de login. Quando o botão de login é clicado, apresenta uma janela para inserir nome de usuário e senha.

- Apenas os professores (logados) têm a capacidade de registrar e desregistrar estudantes nas atividades.

- Os estudantes (não logados) ainda podem ver quem está registrado.

- Não há necessidade de uma página de manutenção de conta. Os professores receberão senhas atribuídas.

## Contexto

Como ainda não há banco de dados, por favor armazenem os nomes de usuário e senhas dos professores em um arquivo `json` que é verificado pelo backend.
