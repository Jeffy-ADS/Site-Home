# NexHome — Sistema de Automação Residencial Inteligente

## 📋 Visão Geral

**NexHome** é uma plataforma web de automação residencial construída com Django que permite controlar dispositivos IoT, gerenciar ambientes, monitorar consumo de energia e automatizar rotinas da sua casa inteligente em tempo real.

O projeto oferece uma experiência moderna com interface intuitiva, autenticação segura de usuários, painel de controle responsivo e tratamento de erros criativo.

---

## ✨ Principais Funcionalidades

### 🔐 Autenticação e Segurança
- **Sistema de Login e Cadastro** com validação de senha segura
- **Proteção de rotas** com decorator `@login_required`
- **Senhas criptografadas** com hash SHA-256 (padrão Django)
- **Sessões seguras** com suporte a logout
- **Redirecionamentos inteligentes** para usuários autenticados

### 🏠 Dashboard de Controle
- **Visualização em tempo real** do status dos dispositivos
- **Controle de ambientes** (Sala, Cozinha, Quarto, etc)
- **Toggle de dispositivos** (Iluminação, Ar-condicionado, Sensores, etc)
- **Monitoramento de consumo** de energia estimado
- **Rotina noturna automática** com ativações programadas
- **Tema claro/escuro** com alternância dinâmica
- **Responsivo** e otimizado para mobile

### 🌐 Página de Boas-vindas (Home)
- **Hero section** com apresentação do sistema
- **Showcase de recursos** com cards interativos
- **Diferenciais** da plataforma
- **Call-to-action contextual** (mostra "Entrar" ou "Ir para Painel" conforme autenticação)
- **Design moderno** com animações fluidas

### ❌ Tratamento de Erros
- **Página 404 personalizada** com design criativo
- **Middleware global** de interceptação de rotas não encontradas
- **Renderização garantida** mesmo em modo desenvolvimento
- **Links de navegação** para voltar à home ou painel

---

## 🎨 Páginas Implementadas

| Rota | Descrição | Acesso |
|------|-----------|--------|
| `/` | Home (Landing Page) | Público |
| `/cadastro/` | Formulário de cadastro de usuário | Público |
| `/login/` | Formulário de login | Público |
| `/dashboard/` | Painel principal de controle | Autenticado |
| `/logout/` | Sair da sessão | Autenticado |
| `/404-preview/` | Preview da página de erro 404 | Dev |
| `/admin/` | Painel administrativo Django | Superusuário |

---

## 🛠 Tecnologias e Framework

### Backend
- **Django 6.0.3** — Framework web Python de alta performance
- **Python 3.14.0** — Linguagem base
- **SQLite3** — Banco de dados relacional local
- **Django ORM** — Camada de abstração de banco

### Frontend
- **HTML5** — Estrutura semântica
- **CSS3** — Estilos avançados (Grid, Flexbox, Gradientes, Animações)
- **JavaScript Vanilla** — Interatividade (toggle de temas, modais, etc)
- **Google Fonts** — Tipografia (Playfair Display, Plus Jakarta Sans, DM Sans)
- **Material Symbols** — Biblioteca de ícones vetoriais

### Ferramentas de Desenvolvimento
- **Git** — Controle de versão
- **Virtual Environment (venv)** — Isolamento de dependências
- **pip** — Gerenciador de pacotes Python

---

## 📦 Estrutura do Projeto

```
Site-Home/
├── manage.py                          # Utilitário de gerenciamento Django
├── db.sqlite3                         # Banco de dados SQLite
├── home/
│   ├── __init__.py
│   ├── settings.py                   # Configurações do projeto
│   ├── urls.py                       # Rotas globais
│   ├── asgi.py
│   └── wsgi.py
├── core/
│   ├── migrations/                   # Histórico de mudanças no BD
│   ├── templates/
│   │   ├── home.html                # Landing page
│   │   ├── dashboard.html           # Painel de controle
│   │   ├── 404.html                 # Página de erro personalizada
│   │   └── registration/
│   │       ├── login.html           # Tela de login
│   │       └── signup.html          # Tela de cadastro
│   ├── views.py                      # Lógica de requisições
│   ├── urls.py                       # Rotas da aplicação
│   ├── models.py                     # Modelos de dados
│   ├── admin.py                      # Configuração admin
│   ├── middleware.py                 # Middleware de tratamento 404
│   └── __init__.py
└── venv/                             # Ambiente virtual
```

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone <repository-url>
cd Site-Home
```

### 2. Ativar ambiente virtual
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Executar migrações
```bash
python manage.py migrate
```

### 5. Criar superusuário (opcional)
```bash
python manage.py createsuperuser
```

### 6. Iniciar servidor de desenvolvimento
```bash
python manage.py runserver
```

### 7. Acessar a aplicação
- **Home**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/
- **Dashboard**: http://127.0.0.1:8000/dashboard/ (requer login)

---

## 👤 Autenticação de Usuários

### Cadastro
1. Acesse `/cadastro/`
2. Defina username e senha (mínimo 8 caracteres)
3. Confirme a senha
4. Será feito login automático e redirecionado ao painel

### Login
1. Acesse `/login/`
2. Digite username e senha
3. Será redirecionado ao dashboard se credenciais estiverem corretas

### Dados Armazenados
- **Tabela**: `auth_user` (banco SQLite)
- **Campos principais**:
  - `username` — Identificador único do usuário
  - `password` — Hash SHA-256 criptografado (não em texto puro)
  - `email` — Email do usuário
  - `first_name` / `last_name` — Nome completo
  - `is_active` — Status da conta
  - `date_joined` — Data de criação

---

## 🔒 Segurança Implementada

✅ **Proteção de rotas** — Decorator `@login_required` no dashboard  
✅ **Hash de senha** — PBKDF2 + SHA-256 (padrão Django)  
✅ **CSRF Token** — Proteção contra ataques cross-site  
✅ **Sessões seguras** — Gerenciadas pelo Django  
✅ **Redirect automático** — Usuários não autenticados redirecionados para login  
✅ **Tratamento de exceções** — Middleware global para erros 404  

---

## 🎯 Possíveis Implementações Futuras

### 🔄 Curto Prazo (MVP)
- [ ] **Modelo de Device** — Criar modelo `Device` para salvar dispositivos no BD
- [ ] **Persistência de estado** — Ligar/desligar dispositivos e salvar estado
- [ ] **Página 500 e 403** — Tratamento criativo para outros erros
- [ ] **API REST** — Endpoints para operações de dispositivos (DRF)
- [ ] **Consumo de energia dinâmico** — Calcular consumo real atualizado

### 📱 Médio Prazo
- [ ] **Aplicativo mobile** — React Native ou Flutter
- [ ] **Notificações push** — Alertas de eventos
- [ ] **Histórico de operações** — Log de ações do usuário
- [ ] **Agendamento de tarefas** — Rotinas automáticas programadas
- [ ] **Integração com Alexa/Google Home** — Voice control
- [ ] **Relatórios de consumo** — Gráficos e análises de energia

### 🏢 Longo Prazo
- [ ] **Suporte a múltiplas residências** — Gerenciar várias casas
- [ ] **Compartilhamento de acesso** — Controle de permissões por usuário
- [ ] **Sistema de câmeras** — Stream de video dos ambientes
- [ ] **Sensores avançados** — Temperatura, umidade, qualidade do ar
- [ ] **Machine Learning** — Automação inteligente baseada em padrões
- [ ] **WebSocket/Realtime** — Atualizações em tempo real sem polling
- [ ] **Backup automático** — Sincronização com cloud

### 🔧 DevOps e Infraestrutura
- [ ] **Docker** — Containerização da aplicação
- [ ] **PostgreSQL** — Banco de dados produção
- [ ] **Redis** — Cache e filas assincronas
- [ ] **Celery** — Task scheduling
- [ ] **GitHub Actions** — CI/CD pipeline
- [ ] **Deploy em cloud** — Heroku, AWS, DigitalOcean, etc
- [ ] **SSL/HTTPS** — Certificados de segurança
- [ ] **Reverse proxy** — Nginx ou similares

---

## 📝 Configurações Principais

### settings.py
```python
DEBUG = True                          # Desenvolvimento (False em produção)
ALLOWED_HOSTS = []                    # Adicione hosts em produção
DATABASE = SQLite3 (db.sqlite3)       # Considere PostgreSQL em produção
LOGIN_URL = 'login'                   # Rota de redireção
LOGIN_REDIRECT_URL = 'dashboard'      # Após login
LOGOUT_REDIRECT_URL = 'home'          # Após logout
```

---

## 🧪 Testando a Aplicação

### Login/Cadastro
1. Acesse `http://127.0.0.1:8000/cadastro/`
2. Crie um usuário de teste
3. Você será automaticamente logado
4. Navegue até o dashboard

### Página 404
- Acesse uma URL inválida: `http://127.0.0.1:8000/rota-inexistente/`
- Ou, use o preview: `http://127.0.0.1:8000/404-preview/`

### Admin
1. Crie um superusuário: `python manage.py createsuperuser`
2. Acesse `http://127.0.0.1:8000/admin/`
3. Gerencie usuários, logs e mais

---

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 👨‍💻 Autor

**NexHome** — Desenvolvido com Django e ❤️ para casas inteligentes.

**Status**: 🟢 Em desenvolvimento | **Versão**: 0.1.0 (Alpha)

---

## 📞 Suporte

Para dúvidas, issues ou sugestões, abra uma issue no repositório ou entre em contato com o time de desenvolvimento.

---

**Última atualização**: 26 de março de 2026
