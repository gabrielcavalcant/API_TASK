# API DJANGO

    Esta é uma API desenvolvida em Django para ajudar os alunos a gerenciarem suas disciplinas e tarefas. A API permite a criação, atualização, exclusão e consulta de alunos, disciplinas e tarefas, bem como a associação de tarefas a alunos e disciplinas.

## Índice

- [Configuração do Ambiente](#configuração-do-ambiente)
- [Modelos de Dados](#modelos-de-dados)
- [Endpoints da API](#endpoints-da-api)
- [Documentação da API](#documentação-da-api)
- [Testando a API](#testando-a-api)
- [Manipulação de Erros](#manipulação-de-erros)
- [Validação de Dados](#validação-de-dados)
- [Consistência de Nomenclatura](#consistência-de-nomenclatura)

## Configuração do Ambiente

    Antes de iniciar, é necessário configurar o ambiente de desenvolvimento Django:

    1. Clone este repositório: `git clone https://github.com/Sir-Chronos/API_DJANGO.git`
    2. Crie um ambiente virtual: `python -m venv "myenv"`
    3. Ative o ambiente virtual: `source "myenv"/bin/activate` (Linux/macOS) ou `"myenv"\Scripts\activate` (Windows)
    4. Instale as dependências: `pip install -r requirements.txt`
    5. Configure as variáveis de ambiente, como as chaves secretas e as configurações do banco de dados, no arquivo `.env`.

## Modelos de Dados

    A aplicação possui três modelos de dados principais:

    - *Aluno*: Representa um aluno com campos `nome` e `email`.
    - *Disciplina*: Representa uma disciplina com campos `nome` e `descricao`.
    - *Tarefa*: Representa uma tarefa com campos `titulo`, `descricao`, `data_entrega`, `concluida`, associada a um aluno e a uma ou mais disciplinas.

## Endpoints da API

    A API oferece os seguintes endpoints:

    1. *Listagem de Alunos*:
    - `GET /api/students/`: Retorna a lista de todos os alunos.

    2. *Criação de um Aluno*:
    - `POST /api/students/`: Permite a criação de um novo aluno.

    3. *Detalhes do Aluno*:
    - `GET /api/students/<id>/`: Retorna detalhes de um aluno específico com base no ID.

    4. *Atualização de um Aluno*:
    - `PUT /api/students/<id>/`: Permite a atualização dos detalhes de um aluno específico com base no ID.

    5. *Exclusão de um Aluno*:
    - `DELETE /api/students/<id>/`: Permite a exclusão de um aluno específico com base no ID. Todas as tarefas associadas a esse aluno serão excluídas ou desassociadas.

    6. *Listagem de Disciplinas*:
    - `GET /api/subjects/`: Retorna a lista de todos os alunos.

    7. *Criação de uma Disciplina*:
    - `POST /api/subjects/`: Permite a criação de um novo aluno.

    8. *Detalhes da Disciplina*:
    - `GET /api/subjects/<id>/`: Retorna detalhes de um aluno específico com base no ID.

    9. *Atualização de uma Disciplina*:
    - `PUT /api/subjects/<id>/`: Permite a atualização dos detalhes de um aluno específico com base no ID.

    10. *Exclusão de uma Disciplina*:
    - `DELETE /api/subjects/<id>/`: Permite a exclusão de um aluno específico com base no ID. Todas as tarefas associadas a esse aluno serão excluídas ou desassociadas.

    11. *Listagem de Tarefas*:
    - `GET /api/tasks/`: Retorna a lista de todos os alunos.

    12. *Criação de uma Tarefa*:
    - `POST /api/tasks/`: Permite a criação de um novo aluno.

    13. *Detalhes da Tarefa*:
    - `GET /api/tasks/<id>/`: Retorna detalhes de um aluno específico com base no ID.

    14. *Atualização de uma Tarefa*:
    - `PUT /api/tasks/<id>/`: Permite a atualização dos detalhes de um aluno específico com base no ID.

    15. *Exclusão de uma Tarefa*:
    - `DELETE /api/tasks/<id>/`: Permite a exclusão de um aluno específico com base no ID. Todas as tarefas associadas a esse aluno serão excluídas ou desassociadas.

    16. *Listagem de Tarefas de um Aluno*:
    - `GET /api/students/<id>/tasks/`: Retorna a lista de todas as tarefas associadas a um aluno específico.

## Testando a API

    Você pode testar a API usando ferramentas como [Postman](https://www.postman.com/) ou [curl](https://curl.se/). Certifique-se de seguir a documentação para fazer solicitações corretamente.

    Uma colection do postman se encontra disponivel no raiz do projeto

## Manipulação de Erros

    A API lida adequadamente com erros, fornecendo respostas de erro apropriadas com códigos de status HTTP significativos e mensagens de erro descritivas.

## Validação de Dados

    A API realiza validações adequadas dos dados de entrada, incluindo a verificação de datas, formatos de e-mail, campos obrigatórios e outros requisitos específicos para cada entidade.

## Consistência de Nomenclatura

    Os nomes de endpoints, campos de modelos e respostas da API seguem uma nomenclatura consistente e fácil de entender, seguindo as convenções recomendadas.