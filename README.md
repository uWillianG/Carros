# Gerenciamento de Carros (Carros)

Este é um sistema de gerenciamento de carros desenvolvido com Django. O projeto permite o cadastro, visualização, atualização e exclusão de veículos, além de gerenciar marcas e inventário. Uma funcionalidade de destaque é a integração com a API da OpenAI para gerar descrições de venda automáticas para os veículos.

## Funcionalidades

*   **Cadastro de Carros:** Registre carros com detalhes como modelo, marca, ano de fabricação, ano do modelo, placa, valor e foto.
*   **Gerenciamento de Marcas:** Cadastro e organização de fabricantes de veículos.
*   **Inventário:** Acompanhamento do contagem e valor total dos carros em estoque.
*   **Autenticação de Usuários:** Sistema de login e registro para acesso administrativo.
*   **IA Generativa:** Integração com OpenAI (GPT-3.5) para criar descrições ("bios") de venda automaticamente para os carros cadastrados.
*   **Upload de Imagens:** Suporte para fotos dos veículos.

## Tecnologias Utilizadas

*   **Python:** Linguagem principal.
*   **Django 5.2:** Framework web.
*   **PostgreSQL:** Banco de dados (configurado por padrão).
*   **OpenAI API:** Para geração de textos com IA.
*   **Pillow:** Manipulação de imagens.
*   **Python-dotenv:** Gerenciamento de variáveis de ambiente.

## Pré-requisitos

*   Python 3.10 ou superior.
*   PostgreSQL (ou ajuste o `settings.py` para usar SQLite).
*   Uma chave de API da OpenAI (para a funcionalidade de IA).

## Instalação e Configuração

1.  **Clone o repositório:**

    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd Carros
    ```

2.  **Crie e ative um ambiente virtual:**

    *   Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    *   Linux/macOS:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuração de Variáveis de Ambiente:**

    Crie um arquivo `.env` na raiz do projeto (mesmo nível do `manage.py`) e adicione sua chave da OpenAI e, se necessário, configurações de banco de dados:

    ```env
    OPENAI_API_KEY=sua_chave_aqui
    ```

5.  **Configuração do Banco de Dados:**

    O projeto está configurado para usar PostgreSQL. Certifique-se de que o serviço está rodando e crie um banco de dados chamado `carros`.
    
    *Alternativamente*, para desenvolvimento rápido, você pode alterar `app/settings.py` para usar SQLite.

6.  **Execute as migrações:**

    ```bash
    python manage.py migrate
    ```

7.  **Crie um superusuário (opcional, para acessar o admin):**

    ```bash
    python manage.py createsuperuser
    ```

8.  **Inicie o servidor de desenvolvimento:**

    ```bash
    python manage.py runserver
    ```

## Estrutura do Projeto

*   `accounts/`: Aplicação responsável pela autenticação e usuários.
*   `app/`: Configurações principais do projeto (settings, urls, wsgi).
*   `cars/`: Aplicação principal com a lógica de negócios dos carros, marcas e inventário.
*   `openai_api/`: Módulo cliente para comunicação com a API da OpenAI.
*   `media/`: Diretório para armazenamento de uploads (imagens dos carros).
*   `templates/`: Templates HTML globais ou específicos das apps.
