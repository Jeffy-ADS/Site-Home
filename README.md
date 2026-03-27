# NexHome - Sistema de Automacao Residencial Inteligente

## Visao Geral
NexHome e uma plataforma web de automacao residencial desenvolvida com Django.
O projeto permite autenticar usuarios, acessar um painel de controle de casa inteligente e navegar com tratamento personalizado para erros 404 e 500.

## Ultima Atualizacao
- Data: 26 de marco de 2026
- Status: Em desenvolvimento (alpha)

## Funcionalidades Implementadas

### Autenticacao e Seguranca
- Cadastro de usuario com `UserCreationForm`
- Login com `LoginView` do Django
- Logout com `LogoutView`
- Protecao de rota com `@login_required` no dashboard
- Redirecionamentos configurados por:
  - `LOGIN_URL = 'login'`
  - `LOGIN_REDIRECT_URL = 'dashboard'`
  - `LOGOUT_REDIRECT_URL = 'home'`
- Senhas armazenadas com hash seguro do Django (PBKDF2)

### Paginas
- Home com CTA contextual para entrar ou ir ao painel
- Dashboard protegido para usuarios autenticados
- Tela de login
- Tela de cadastro
- Pagina 404 personalizada
- Pagina 500 personalizada (minimalista, no estilo do site)

### Tratamento de Erros
- `handler404` global configurado
- `handler500` global configurado
- Middleware global em `core/middleware.py`:
  - Renderiza `404.html` em respostas 404
  - Renderiza `500.html` em respostas 500
  - Captura excecoes nao tratadas e renderiza `500.html`
- Funciona inclusive em desenvolvimento para a renderizacao personalizada

## Rotas Disponiveis

| Rota | Nome | Acesso | Descricao |
|---|---|---|---|
| `/` | `home` | Publico | Landing page |
| `/cadastro/` | `signup` | Publico | Cadastro de usuario |
| `/login/` | `login` | Publico | Login |
| `/logout/` | `logout` | Autenticado | Encerrar sessao |
| `/dashboard/` | `dashboard` | Autenticado | Painel principal |
| `/404-preview/` | `preview_404` | Dev | Preview da pagina 404 |
| `/500-preview/` | `preview_500` | Dev | Dispara erro para testar pagina 500 |
| `/admin/` | - | Superusuario | Admin Django |

## Estrutura do Projeto

```text
Site-Home/
├── manage.py
├── db.sqlite3
├── README.md
├── home/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── core/
│   ├── admin.py
│   ├── apps.py
│   ├── middleware.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       ├── home.html
│       ├── dashboard.html
│       ├── 404.html
│       ├── 500.html
│       └── registration/
│           ├── login.html
│           └── signup.html
└── venv/
```

## Tecnologias
- Python 3.14
- Django 6.0.3
- SQLite3
- HTML, CSS, JavaScript (vanilla)

## Como Executar

### 1. Entrar na pasta do projeto
```powershell
cd C:\Users\jeffe\OneDrive\Documentos\Django\NexHome\Site-Home
```

### 2. Ativar ambiente virtual (Windows)
```powershell
venv\Scripts\activate
```

### 3. Instalar dependencias principais
```powershell
pip install django tzdata
```

### 4. Aplicar migracoes
```powershell
python manage.py migrate
```

### 5. (Opcional) Criar superusuario
```powershell
python manage.py createsuperuser
```

### 6. Iniciar servidor
```powershell
python manage.py runserver
```

### 7. Acessar
- Home: http://127.0.0.1:8000/
- Login: http://127.0.0.1:8000/login/
- Cadastro: http://127.0.0.1:8000/cadastro/
- Dashboard: http://127.0.0.1:8000/dashboard/
- Admin: http://127.0.0.1:8000/admin/

## Testes Rapidos

### Fluxo de autenticacao
1. Acesse `/cadastro/`
2. Crie um usuario
3. Verifique redirecionamento para `/dashboard/`
4. Realize logout

### Erro 404
- Acesse uma rota invalida, por exemplo: `/nao-existe/`
- Ou use: `/404-preview/`

### Erro 500
- Use a rota de teste: `/500-preview/`
- A pagina personalizada de erro 500 deve ser renderizada

## Principais Causas de Erro 500 (documentadas na propria pagina)
- Banco de dados nao configurado (`db.sqlite3` ausente ou credenciais incorretas)
- Migracoes nao aplicadas
- Tabela `auth_user` inexistente
- Dependencias ausentes (ex.: `tzdata`)
- Excecao nao tratada em view ou operacao de banco

## Proximos Passos Sugeridos
- Criar `requirements.txt` e fixar versoes
- Implementar testes automatizados (`core/tests.py`)
- Implementar pagina 403 personalizada
- Modelar entidades de dispositivos IoT com persistencia em banco

## Licenca
Projeto sob licenca MIT (recomenda-se incluir arquivo `LICENSE`).
