<h1>Rio10</h1>

## Descrição do projeto 

<p align="justify">
Projeto construído em Django, HTML, CSS e JavaScript. O objetivo da aplicação é ser uma solução para conectar atletas, treinadores e outros, gerando parcerias lucrativas. Inicialmente, o esporte de foco é o futebol.
</p>

<h1>## Funcionalidades</h1>

### Back-end:

:heavy_check_mark: Cadastro de novos usuários com informações salvas em um banco relacional.

:heavy_check_mark: Complementos do cadastro salvos em outra tabela do banco.

:heavy_check_mark: Controle de autenticação de usuários via Django e SQL.Ao ser realizado o cadastro de novos usuários a informação é salva em um banco relacional, os complementos do cadastro solicitados em outra página html também são salvos em uma outra tabela do banco.


### Front-end:

:heavy_check_mark: Tela principal "Home" com um header contendo a logo da empresa, botões de "login" e "cadastro". A home também possui uma mensagem de boas-vindas, tutorial de cadastro e um footer com páginas, campo de "outros" para sugestões e suporte, e um campo para redes sociais com links incorporados.

:heavy_check_mark: Tela de complemento de cadastro com campos específicos dependendo do tipo de pessoa cadastrada (Atleta, Treinador, etc.).

:heavy_check_mark: Tela "Minha Área" com informações do usuário, foto, estatísticas e leaderboards.

:heavy_check_mark: Responsividade Mobile de todo projeto.


<h1>## Pré-requisitos</h1>

<p>- Visual Studio Code</p>
<p>- Python</p>
<p>- JavaScript</p>
<p>- SaaS</p>
<p>- Html</p>
<p>- CSS</p>
<p>- MySQL</p>

<h1>## Comandos/ Passo a Passo</h1>

**Windows Power Shell/Outro terminal:**

1. Comando "cd" para localizar a pasta do projeto de desejo
2. pip install requirements.txt
3. django-admin startproject core

**MySQL:**

1. CREATE DATABASE startup;
2. USE DATABASE startup;

**Python:**

Após a configuração do ambiente e criação do banco de dados, siga estes passos:

1. Configure a variável DATABASES no arquivo settings.py.
2. Crie um super usuário: python manage.py createsuperuser.
3. Crie uma nova migração: python manage.py makemigrations.
4. Realize a migração criada: python manage.py migrate.
5. Inicie o servidor: python manage.py runserver.

Lembre-se de instalar todos os pré-requisitos, pré-configurar o ambiente Django, autenticação do usuário root no MySQL e alterar a variável de senha no arquivo .\app\settings.py.

<h1>## Desenvolvedores :octocat:</h1>

<p>VonDerLitch "Kelvin Silveira"</p>
<p>GuilhermeMoraes4</p>
<p>Gabwasch</p>
