Como configurar o projeto

Para fazê-lo, utilizei de Docker Desktop, WSL2, Portainer, Python 3.9.6, Django 3.2.5, PostgreSQL 14.
Tenha eles instalados em sua máquina.

Primeiramente, baixe este projeto, clicando em 'Code' e depois 'Download ZIP'
Após isso, crie uma pasta no diretório de sua preferência chamada 'src' e coloque todos os arquivos lá dentro, com a execessão de três:
'requirements.txt'
'Dockerfile'
'docker-compose.yml'

Eles devem ficar no diretório inicial, juntamente com a pasta 'src'.

Tutorial para configurar o Portainer(vide ava da disciplina):

https://www.youtube.com/watch?v=H2LPxKL5CvU

OBS: Utilize uma porta diferente da 8000! No projeto, usamos ela para iniciar as apis.

Em seguida, vamos digitar alguns comandos no prompt de Comando do Windows.
Vá até a barra de pesquisa do Windows, digite 'cmd' e abra como administrador.
Copie e cole os comandos abaixo:

docker create -v /var/lib/postgresql/data --name PostgresData alpine
docker run -p 5432:5432 --name postgres-container -e POSTGRES_PASSWORD=suaSenhaAqui -d --volumes-from PostgresData postgres

Esses comandos criam um espaço para guardar dados e um container para o nosso querido PostgreSQL, de forma que, quando houverem novas versões do Postgres, possamos destruir o container e recria-lo sem perder nossos dados.
(Referência, em inglês, https://ryaneschinger.com/blog/dockerized-postgresql-development-environment/)

Além disso, vale notar o campo 'POSTGRES_PASSWORD=suaSenhaAqui'.
Esta senha é para se conectar ao servidor do Postgres, você criou ela quando instalou o software.

Agora, vá ao seu Portainer.

Selecione o container do postgres ( https://imgur.com/rmqr3Lf )
Vá até a aba de 'Create image', dê o nome 'trab-data' a imagem e pressione 'Create' ( https://imgur.com/3qUhjM5 )

Ok, agora vamos ao Container das APIs.

Volte ao prompt de comando aberto em modo administrador.
Navegue até a pasta do projeto.
Exemplo, se a pasta estiver no seu Desktop, digite o comando 'cd C:\Users\meu-usuario\Desktop\minha-pasta'
Substituindo 'meu-usuario' e 'minha-pasta' pelo *seu* usuário e pelo nome que você colocou na pasta.

Após isso, copie e cole o comando 'docker-compose run web python src/trab-comp-dist/manage.py migrate'
Você deve ver algo assim: https://imgur.com/9rHzYuq
Em seguida, digite 'docker-compose up'
Vão aparecer muitas mensagens na tela, mas as últimas serão algo como: https://imgur.com/9TVWVEr

Pronto! Os containers das APIs e do banco já estão funcionando!
