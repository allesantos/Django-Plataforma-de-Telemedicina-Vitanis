# Plataforma de Telemedicina Vitanis Total Care

Este é um projeto de uma plataforma de telemedicina desenvolvida com Django, permitindo que médicos e pacientes se cadastrem, façam login e interajam no sistema para agendar e realizar consultas online.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Vitanis/img1.png">

## Índice
- [Descrição](#Descrição)
- [Recursos](#Recursos)
- [Tecnologias Utilizadas](#Tecnologias)
- [Pré-requisitos](#Pré-requisitos)
- [Instalação](#Instalação)
- [Uso](#Uso)
- [Contribuição](#Contribuição)
- [Licença](#Licença)


## Descrição

Este projeto é uma plataforma de telemedicina onde médicos e pacientes podem se registrar e interagir para realizar consultas. O sistema foi desenvolvido usando Django e fornece as funcionalidades para agendamento de consultas e videochamadas.

-  __Médicos:__ Podem se cadastrar, fornecer credenciais profissionais, cadastrar horários disponíveis para consultas, visualizar consultas agendadas e realizar videochamadas com os pacientes.

-  __Pacientes:__ Podem se cadastrar, escolher especialidades, visualizar médicos disponíveis, agendar consultas e se conectar com os médicos via videochamada.


## Recursos

-  __Cadastro e login de usuários:__  Tanto médicos quanto pacientes podem se cadastrar e realizar login.
  
-  __Cadastro de médicos:__ Médicos devem fornecer credenciais e especialidades.
  
-  __Agendamento de consultas:__ Pacientes escolhem médicos e marcam consultas com base nos horários disponíveis.
  
-  __Visualização de consultas:__ Médicos podem visualizar as consultas agendadas e entrar em videochamadas.
  
-  __Videochamada:__ Funcionalidade para médicos e pacientes interagirem em tempo real através de videochamadas.


## Uso

1. Para utilizar o sistema é necessário realizar um cadastro, registrando apenas usuário, email e senha. Caso seja médico, também é necessário marcar a caixinha de seleção.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Vitanis/img2.png">

2. Se o usuário for médico, após clicar no botão "Cadastrar", será redirecionado para uma página onde irá ter que realizar um cadastro legal de médico. Este cadastro irá definir que tipo de usuário e quais privilégios irá ter na plataforma.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Vitanis/img3.png">

3. Após o cadastro, o usuário médico, será redirecionado para uma página para que ele possa abrir horários para consultas.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Vitanis/img4.png">

4. Caso tenhamos um usuário que será apenas paciente, ele irá precisar fazer também um cadastro inicial, basta apenas não marcar a opção de médico.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Vitanis/img5.png">

5. O usuário paciente será redirecionado para a página de login.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Vitanis/img6.png">

6. Após o login, o usuário paciente irá para a página home, onde é possível visualizar todos os médicos cadastrados e suas especialidades.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Vitanis/img7.png">

7. É possível realizar um filtro para localizar um médico cadastrado de acordo com sua especialidade. Esta função está disponível para médicos ou pacientes realizarem o filtro.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Vitanis/img8.png">

8. O filtro também poderá ser feito localizando o médico de acordo com sua especialidade.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Vitanis/img9.png">

9. Caso o usuário paciente tenha optado por filtrar um médico de acordo com sua especialidade, poderá ser exibida uma lista com todos que exercem a mesma função.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Vitanis/img10.png">

10. Após escolher o médico, o paciente será redirecionado para esta página, onde poderá agendar a consulta com base nos dias e horários disponíveis.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Vitanis/img11.png">

11. Após agendar a consulta, será redirecionado para esta página onde aqui exibirá todas as consultas já agendadas.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Vitanis/img12.png">

12. Clicando no nome do médico, o paciente irá acessar os detalhes da consulta que ele agendou. Nesta página, é possível realizar o cancelamento da consulta, caso o paciente decida desistir. Está disponível também a opção de adicionar a consulta no calendário, assim o paciente será sempre lembrado sobre a consulta que ele agendou.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Vitanis/img13.png">

13. No caso do médico, assim que ele fizer login, é possível visualizar todas as suas consultas e seus status.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Vitanis/img14.png">

14. Quando chegar o dia e horário da consulta, o médico irá clicar no nome do paciente.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Vitanis/img15.png">

15. Nesta página, médico irá adicionar o link da videoconferência e depois iniciar a consulta.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Vitanis/img16.png">

16. No caso do paciente, nesta página, o botão Acessar Consulta estará disponível, basta clicar e fazer o acesso.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Vitanis/img17.png">

17. Durante a consulta ou depois, o médico também pode publicar documentos como atestado médico, receitas, exames etc.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Vitanis/img18.png">

17. Quando uma consulta é finalizada, é exibido um verificador indicando o status de consulta realizada.

<img src = "https://github.com/allesantos/allesantos/blob/main/imagens/Vitanis/19.png">


## Tecnologias

-  __Django__
  
-  __SQLite__ (banco de dados local)

-  __HTML/CSS/JavaScript__ para a interface do usuário


## Pré-requisitos

Antes de começar, você precisará ter as seguintes ferramentas instaladas:
-  __Python 3.x__
-  __Git__
  
Além disso, recomenda-se usar um ambiente virtual Python para gerenciar dependências.


## Instalação

1. Clone o repositório para sua máquina local:

    ```
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. Crie e ative um ambiente virtual:

    ```
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências do projeto:

    ```
    pip install -r requirements.txt
    ```

4. Execute as migrações do banco de dados:

    ```
    python manage.py migrate
    ```

5. Inicie o servidor de desenvolvimento:

    ```
    python manage.py runserver
    ```

6. Acesse o sistema em http://127.0.0.1:8000/ no seu navegador.


## Contribuição

Sinta-se à vontade para contribuir com este projeto. Siga estas etapas:

1. Faça um fork do repositório.

2. Crie uma nova branch para sua feature/bugfix:

    ```
    git checkout -b minha-feature
    ```

3. Envie suas alterações:

    ```
    git push origin minha-feature
    ```

4. Abra um Pull Request neste repositório.


## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais informações.
