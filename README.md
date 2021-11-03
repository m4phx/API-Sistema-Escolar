<h1>Como configurar o projeto</h1>

Para fazê-lo, utilizei de Docker Desktop, WSL2, Portainer, Python 3.9.6, Django 3.2.5, PostgreSQL 14.
Tenha eles instalados em sua máquina.

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
