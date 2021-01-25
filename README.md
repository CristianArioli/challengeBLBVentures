# Desafio para Contratação BLB Ventures

Objetivos Frontend

  - Quando der play em uma música pare qualquer outra que estiver tocando.
  - Deixar o nome da música e o player na mesma linha de maneira responsiva.
  - Opcional: qualquer outra melhoria que achar interessante no design ou mesmo nas funcionalidades
  
Objetivos Full Stack

  - Transformar o backend nodejs em um backend python (utilizar uma framework como django, flask e afins preferêncialmente)
  - Criar uma api REST para listar as musicas e utilizá-la para popular o frontend

**PS:** Todos os comandos utilizados são referentes ao powershell do windows.

## Instalação e inicializão do Venv

Navegue até a pasta raiz do projeto e use o seguintes comandos para instalar e depois inicilizar a venv:

```sh
python -m venv ./venv
Set-ExecutionPolicy Unrestricted -Scope Process
venv/Scripts/activate.ps1
```

# Dependências do projeto

Com o venv inicializado utilize o seguinte comando para instalar as dependências do projeto que estão no arquivo requirements.txt.

```sh
pip install -r requirements.txt
```

## Inicialização da API

Ainda na pasta raiz do projeto, com o venv ja inicializado, utilize o seguinte comandos para corrigir os migrates da api:

```sh
python manage.py migrate
```

E agora o seguinte código para inicilizar a api:

```sh
python manage.py runserver 9090
```

**PS:** o número na frente do **runserver** serve para atribuir uma porta para a aplicação.

## Inicialização da Página Web

Em um novo terminal, navegue até a pasta raiz do projeto e inicialize a venv.

```sh
Set-ExecutionPolicy Unrestricted -Scope Process
venv/Scripts/activate.ps1
```

Navegue até a pasta webpage que se encontra dentro da pasta raiz do projeto e corrija as migrates da página web:

```sh
python manage.py migrate
```

Agora inicialize o projeto da página web:

```sh
python manage.py runserver 8080
```

**PS:** o número na frente do **runserver** serve para atribuir uma porta para a aplicação.

## Utilizando o Projeto

#### Adicionando uma nova música
Na página da API que no exemplo se encontra em **http://localhost:9090** navegue até a rota /musics. Lá adicione um Título para a música e o nome do arquivo de música.
Exemplo:

```sh
title: Mixaund Sunshine Day
path: mixaund-sunshine-day.mp3
```
Com as entradas na api, adicione o arquivo de música dentro da pasta **webpage/myapp/static/tracks**.

Agora basta abrir a página web que no exemplo passado se encontra em **http://localhost:8080/**.

#### Removendo e editando uma música
Na página da API que no exemplo se encontra em **http://localhost:9090** navegue até a rota /musics. Lá encontre a música que gostaria de excluir e copie seu id. Após isso cole o id na frente do endereço.
Exemplo
```sh
http://localhost:9090/8bc6c006-7fe1-4097-a78d-a01771ffc5d4
```
Na nova página você pode clicar em **deletar** para remover uma música ou **editar** os campos da música.
