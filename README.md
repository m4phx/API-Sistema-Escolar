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

<p><b>==============================================================================</b></p>

<p><h2><b>Documentação das APIs</b></h2></p>
<p><b>Ferramenta para se comunicar com as APIs: Postman</b></p>

<p><h3><br>API Alunos</h3></br></p>

<p>Link: http://127.0.0.1:8000/alunos/</p>
<p>Para todos os alunos</p>

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Aluno List",
    "description": "\"Exibindo todos os alunos e alunas",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "POST": {
            "id": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "ID"
            },
            "nome": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Nome",
                "max_length": 100
            },
            "rg": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Rg",
                "max_length": 9
            },
            "cpf": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Cpf",
                "max_length": 11
            },
            "data_nascimento": {
                "type": "date",
                "required": true,
                "read_only": false,
                "label": "Data nascimento"
            }
        }
    }
}

<p>Para apenas um aluno:</p>
<p>http://127.0.0.1:8000/alunos/id/</p> 

HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Aluno Instance",
    "description": "\"Exibindo um aluno",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "PUT": {
            "id": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "ID"
            },
            "nome": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Nome",
                "max_length": 100
            },
            "rg": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Rg",
                "max_length": 9
            },
            "cpf": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Cpf",
                "max_length": 11
            },
            "data_nascimento": {
                "type": "date",
                "required": true,
                "read_only": false,
                "label": "Data nascimento"
            }
        }
    }
}

<p><h3><br>API Cursos</h3></br></p>

<p>Link: http://127.0.0.1:8000/cursos/</p>
<p>Para todos os cursos</p>

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Curso List",
    "description": "Exibindo todos os cursos",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "POST": {
            "id": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "ID"
            },
            "nome": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Nome",
                "max_length": 255
            },
            "codigo_curso": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Codigo curso",
                "max_length": 10
            },
            "descricao": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Descricao",
                "max_length": 100
            },
            "nivel": {
                "type": "choice",
                "required": false,
                "read_only": false,
                "label": "Nivel",
                "choices": [
                    {
                        "value": "B",
                        "display_name": "Básico"
                    },
                    {
                        "value": "I",
                        "display_name": "Intermediário"
                    },
                    {
                        "value": "A",
                        "display_name": "Avançado"
                    }
                ]
            }
        }
    }
}

<p>Para apenas um curso:</p>

<p>http://127.0.0.1:8000/cursos/id/</p>

HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Curso Instance",
    "description": "Exibindo um curso",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "PUT": {
            "id": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "ID"
            },
            "nome": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Nome",
                "max_length": 255
            },
            "codigo_curso": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Codigo curso",
                "max_length": 10
            },
            "descricao": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Descricao",
                "max_length": 100
            },
            "nivel": {
                "type": "choice",
                "required": false,
                "read_only": false,
                "label": "Nivel",
                "choices": [
                    {
                        "value": "B",
                        "display_name": "Básico"
                    },
                    {
                        "value": "I",
                        "display_name": "Intermediário"
                    },
                    {
                        "value": "A",
                        "display_name": "Avançado"
                    }
                ]
            }
        }
    }
}

<p><h3><br>API Nota</h3></br></p>

<p>Para todas as notas</p>
<p>Link: http://127.0.0.1:8000/notas/</p>

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Nota List",
    "description": "Exibindo todos as notas",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "POST": {
            "id": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "ID"
            },
            "valor": {
                "type": "integer",
                "required": true,
                "read_only": false,
                "label": "Valor",
                "min_value": -2147483648,
                "max_value": 2147483647
            },
            "aluno": {
                "type": "field",
                "required": true,
                "read_only": false,
                "label": "Aluno"
            }
        }
    }
}

<p>Para apenas uma nota</p>
<p>Link: http://127.0.0.1:8000/notas/id</p>

HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Nota Instance",
    "description": "Exibindo uma nota",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "PUT": {
            "id": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "ID"
            },
            "valor": {
                "type": "integer",
                "required": true,
                "read_only": false,
                "label": "Valor",
                "min_value": -2147483648,
                "max_value": 2147483647
            },
            "aluno": {
                "type": "field",
                "required": true,
                "read_only": false,
                "label": "Aluno"
            }
        }
    }
}

<p><h3><br>API Esportes</br></h3></p>
<p>Link http://127.0.0.1:8000/esportes/</p>
<p>Para todos os esportes</p>

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Esporte List",
    "description": "Exibindo todos os esportes",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "POST": {
            "id": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "ID"
            },
            "nome": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Nome",
                "max_length": 10
            },
            "descricao": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Descricao",
                "max_length": 100
            },
            "tipo": {
                "type": "choice",
                "required": false,
                "read_only": false,
                "label": "Tipo",
                "choices": [
                    {
                        "value": "B",
                        "display_name": "Bola"
                    },
                    {
                        "value": "P",
                        "display_name": "Peso"
                    },
                    {
                        "value": "A",
                        "display_name": "Aquático"
                    }
                ]
            }
        }
    }
}

<p>Link http://127.0.0.1:8000/esportes/id</p>
<p>Para apenas um esporte</p>

HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Esporte Instance",
    "description": "Exibindo um esporte",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "PUT": {
            "id": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "ID"
            },
            "nome": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Nome",
                "max_length": 10
            },
            "descricao": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Descricao",
                "max_length": 100
            },
            "tipo": {
                "type": "choice",
                "required": false,
                "read_only": false,
                "label": "Tipo",
                "choices": [
                    {
                        "value": "B",
                        "display_name": "Bola"
                    },
                    {
                        "value": "P",
                        "display_name": "Peso"
                    },
                    {
                        "value": "A",
                        "display_name": "Aquático"
                    }
                ]
            }
        }
    }
}

<p><h3><br>API Matérias</br></h3></p>

<p>Link: http://127.0.0.1:8000/materias/</p>
<p>Para todas as matérias</p>

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Materia List",
    "description": "\"Exibindo todos as matérias",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "POST": {
            "id": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "ID"
            },
            "nome": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Nome",
                "max_length": 30
            },
            "carga_horaria": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Carga horaria",
                "max_length": 3
            },
            "curso": {
                "type": "field",
                "required": true,
                "read_only": false,
                "label": "Curso"
            }
        }
    }
}

<p>Link: http://127.0.0.1:8000/materias/id/
<p>Para uma matéria</p>

HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Materia Instance",
    "description": "\"Exibindo todos os alunos e alunas",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "PUT": {
            "id": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "ID"
            },
            "nome": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Nome",
                "max_length": 30
            },
            "carga_horaria": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Carga horaria",
                "max_length": 3
            },
            "curso": {
                "type": "field",
                "required": true,
                "read_only": false,
                "label": "Curso"
            }
        }
    }
}
