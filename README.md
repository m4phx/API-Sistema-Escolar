<h1>Como configurar o projeto</h1>

O sistema operacional utilizado foi o Windows.
Para fazê-lo, utilizei de Docker Desktop, WSL2, Portainer, Python 3.9.6, Django 3.2.5, PostgreSQL 14.
Tenha eles instalados em sua máquina.

<p>Instalação do Docker e WSL2 (português): https://docs.microsoft.com/pt-br/windows/wsl/tutorials/wsl-containers</p>
<p>Instalação do Docker (inglês): https://docs.docker.com/desktop/windows/wsl/</p>
<p>Instalação do WSL2 (português): https://docs.microsoft.com/pt-br/windows/wsl/install</p>
<p>Instalação do Python: https://python.org.br/instalacao-windows/</p>
<p>Instalação do PostgreSQL https://techexpert.tips/pt-br/windows-pt-br/instalacao-do-postgresql-no-windows/</p>
<p>Instalação do Django: https://docs.djangoproject.com/pt-br/3.2/intro/install/</p>


<p>Primeiramente, baixe este projeto, clicando em 'Code' e depois 'Download ZIP'</p>
<p>Após isso, crie uma pasta no diretório de sua preferência chamada 'src' e coloque todos os arquivos lá dentro, com a execessão de três:</p>
<ul><b>'requirements.txt'</b></ul>
<ul><b>'Dockerfile'</b></ul>
<ul><b>'docker-compose.yml'</b></ul>

Eles devem ficar no diretório inicial, juntamente com a pasta 'src'.

Tutorial para configurar o Portainer(vide ava da disciplina):

https://www.youtube.com/watch?v=H2LPxKL5CvU

<b>OBS:</b> Utilize uma porta diferente da 8000! No projeto, usamos ela para iniciar as apis.

<p>Em seguida, vamos digitar alguns comandos no prompt de Comando do Windows.</p>
<p>Vá até a barra de pesquisa do Windows, digite 'cmd' e abra como administrador.</p>
<p>Copie e cole os comandos abaixo:</p>

<p>docker create -v /var/lib/postgresql/data --name PostgresData alpine</p>
<p>docker run -p 5432:5432 --name postgres-container -e POSTGRES_PASSWORD=suaSenhaAqui -d --volumes-from PostgresData postgres</p>

<p>Esses comandos criam um espaço para guardar dados e um container para o nosso querido PostgreSQL, de forma que, quando houverem novas versões do Postgres, possamos destruir o container e recria-lo sem perder nossos dados.</p>
<p>(Referência, em inglês, https://ryaneschinger.com/blog/dockerized-postgresql-development-environment/)</p>

<p>Além disso, vale notar o campo 'POSTGRES_PASSWORD=suaSenhaAqui'.</p>
<p>Esta senha é para se conectar ao servidor do Postgres, você criou ela quando instalou o software. </p>

<p>Agora, vá ao seu Portainer.</p>

<p>Selecione o container do postgres ( https://imgur.com/rmqr3Lf )</p>
<p>Vá até a aba de 'Create image', dê o nome 'trab-data' a imagem e pressione 'Create' ( https://imgur.com/3qUhjM5 )</p>

<p>Ok, agora vamos ao Container das APIs.</p>

<p>Volte ao prompt de comando aberto em modo administrador.</p>
<p>Navegue até a pasta do projeto.</p>
<p>Exemplo, se a pasta estiver no seu Desktop, digite o comando 'cd C:\Users\meu-usuario\Desktop\minha-pasta'</p>
<p>Substituindo 'meu-usuario' e 'minha-pasta' pelo *seu* usuário e pelo nome que você colocou na pasta.</p>

<p>Após isso, copie e cole o comando 'docker-compose run web python src/trab-comp-dist/manage.py migrate'</p>
<p>Você deve ver algo assim: https://imgur.com/9rHzYuq</p>
<p>Em seguida, digite 'docker-compose up'</p>
<p>Vão aparecer muitas mensagens na tela, mas as últimas serão algo como: https://imgur.com/9TVWVEr</p>

<p><b>Pronto!</b> Os containers das APIs e do banco já estão funcionando!</p>

<p>==============================================================================</p>
<p>Ferramenta para se comunicar com as APIs: Postman</p>
<p>Documentação das APIs:</p>

<p>API Alunos </p>


Link: http://127.0.0.1:8000/alunos/

Para recuperar alunos:
Método: GET

Usando o link geral, retorna todos, por exemplo:
[
    {
        "id": 1,
        "nome": "Aluno 1",
        "rg": "123456789",
        "cpf": "12345678901",
        "data_nascimento": "2021-11-03"
    },
    {
        "id": 2,
        "nome": "Joaozinho",
        "rg": "123456789",
        "cpf": "12345678901",
        "data_nascimento": "1990-07-13"
    },
    {
        "id": 3,
        "nome": "Pedrinho",
        "rg": "123456789",
        "cpf": "12345678901",
        "data_nascimento": "1995-03-22"
    }
]

Usando um link com id especifico, retorna apenas 1, por exemplo:

GET http://127.0.0.1:8000/alunos/2/

Exemplo de resposta:

{
    "id": 2,
    "nome": "Joaozinho",
    "rg": "123456789",
    "cpf": "12345678901",
    "data_nascimento": "1990-07-13"
}


Para inserir um aluno:
Método: POST

Exemplo de Body:

{
    "nome": "Joaozinho",
    "rg": "123456789",
    "cpf": "12345678901",
    "data_nascimento": "1990-07-13"
}

Exemplo de retorno:

{
    "id": 2,
    "nome": "Joaozinho",
    "rg": "123456789",
    "cpf": "12345678901",
    "data_nascimento": "1990-07-13"
}

Para atualizar um aluno:

Método: PUT

Link deve especificar id

Exemplo:

PUT http://127.0.0.1:8000/alunos/2/

{
        "nome": "Paulo",
        "rg": "129111111",
        "cpf": "12345678901",
        "data_nascimento": "1995-04-13"
}

Retorna o aluno editado

    {
        "id": 2,
        "nome": "Paulo",
        "rg": "129111111",
        "cpf": "12345678901",
        "data_nascimento": "1995-04-13"
    }

Deletar um aluno:

Link deve especificar id, por exemplo:

DELETE http://127.0.0.1:8000/alunos/2/

Apaga o aluno e não retorna nada.
