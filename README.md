# 📁 Estrutura Completa do Repositório

```
projeto-repositorio/                    # 📂 Repositório principal
├── 📄 README.md                       # Documentação principal
├── 📄 LICENSE                         # Licença MIT
├── 📄 .gitignore                      # Arquivos ignorados pelo Git
│
├── 📊 apresentacao/                   # Slides educacionais
│   ├── introducao.html               # Slide 1: Introdução
│   ├── clean_architecture.html      # Slide 2: Clean Architecture
│   ├── solid_principles.html        # Slide 3: Princípios SOLID
│   ├── design_patterns.html         # Slide 4: Design Patterns
│   ├── ddd_introducao.html          # Slide 5: DDD Introdução
│   ├── ddd_padroes.html             # Slide 6: DDD Padrões
│   ├── projeto_pratico.html         # Slide 7: Projeto Prático
│   ├── implementacao_api.html       # Slide 8: Implementação
│   ├── docker_containerizacao.html  # Slide 9: Docker
│   ├── conclusao.html               # Slide 10: Conclusão
│   ├── Perfil.png                   # Foto do instrutor
│   └── Logo.png                     # Logo Icoma Education
│
├── 🚀 api/                           # API REST com Clean Architecture
│   ├── 📄 README.md                 # Documentação da API
│   ├── 📄 README-Docker.md          # Guia Docker
│   ├── 📄 requirements.txt          # Dependências Python
│   ├── 📄 Dockerfile                # Imagem Docker
│   ├── 📄 docker-compose.yml        # Orquestração completa
│   ├── 📄 docker-compose.dev.yml    # Versão desenvolvimento
│   ├── 📄 docker-run.sh             # Script automação Docker
│   ├── 📄 .dockerignore             # Arquivos ignorados Docker
│   ├── 📄 .env.example              # Variáveis de ambiente
│   ├── 📄 .gitignore                # Git ignore específico
│   ├── 📄 test_structure.py         # Teste estrutura DDD
│   ├── 📁 venv/                     # Ambiente virtual Python
│   └── 📁 src/                      # Código fonte (Clean Architecture)
│       ├── 📄 main.py               # Aplicação principal
│       ├── 🎯 domain/               # Camada de Domínio
│       │   ├── entities/            # Entities (Livro, Usuario)
│       │   ├── value_objects/       # Value Objects (ISBN, Email)
│       │   ├── repositories/        # Repository Interfaces
│       │   └── services/            # Domain Services
│       ├── 🔧 application/          # Camada de Aplicação
│       │   ├── use_cases/           # Use Cases
│       │   └── dtos/                # Data Transfer Objects
│       ├── 🏭 infrastructure/       # Camada de Infraestrutura
│       │   ├── database/            # SQLAlchemy Models
│       │   └── repositories/        # Repository Implementations
│       ├── 🌐 presentation/         # Camada de Apresentação
│       │   └── controllers/         # REST Controllers
│       ├── 📁 models/               # Compatibilidade
│       ├── 📁 routes/               # Compatibilidade
│       └── 📁 database/             # Banco de dados SQLite
│
├── 📖 docs/                          # Documentação completa
│   ├── TUTORIAL_PASSO_A_PASSO.md    # Tutorial completo (50+ páginas)
│   ├── CHECKLIST_IMPLEMENTACAO.md   # Lista de verificação
│   ├── GUIA_INSTALACAO.md           # Instalação detalhada
│   └── ESTRUTURA_REPOSITORIO.md     # Este arquivo
│
├── 🎬 assets/                        # Recursos multimídia
│   ├── 📄 README.md                 # Documentação dos assets
│   ├── 🎥 apresentacao_completa.mp4 # Vídeo completo (30s)
│   ├── 🎥 intro_video.mp4           # Introdução
│   ├── 🎥 clean_arch_video.mp4      # Clean Architecture
│   ├── 🎥 solid_video.mp4           # Princípios SOLID
│   ├── 🎥 ddd_video.mp4             # Domain-Driven Design
│   ├── 🎥 api_demo_video.mp4        # Demo da API
│   ├── 🎥 conclusion_video.mp4      # Conclusão
│   ├── 🖼️ background_tech.png       # Fundo tecnológico
│   ├── 🖼️ clean_arch_diagram.png    # Diagrama Clean Architecture
│   ├── 🖼️ solid_principles.png      # Infográfico SOLID
│   ├── 🖼️ ddd_concept.png           # Conceitos DDD
│   └── 🖼️ api_demo.png              # Demo visual da API
│
├── 🔧 scripts/                       # Scripts de automação
│   ├── 📄 README.md                 # Documentação dos scripts
│   ├── 🚀 criar_projeto.sh          # Cria projeto do zero
│   └── ⚡ install.sh                # Instalação automática
│
└── 💡 examples/                      # Exemplos de código
    ├── 📄 README.md                 # Documentação dos exemplos
    ├── 📄 livro_completo.py         # Entity Livro completa
    ├── 📄 livro_tutorial.py         # Entity Livro simplificada
    ├── 📄 usuario_completo.py       # Entity Usuario completa
    └── 📄 usuario_tutorial.py       # Entity Usuario simplificada
```

## 📊 **Estatísticas do Repositório**

- **📁 Total de arquivos**: 2.443
- **📄 Arquivos Markdown**: 12
- **🐍 Arquivos Python**: 15+ (código principal)
- **🎬 Vídeos**: 6 (MP4)
- **🖼️ Imagens**: 8 (PNG)
- **📊 Slides HTML**: 10
- **🔧 Scripts**: 2 (Shell)
- **🐳 Docker**: 4 arquivos
- **📖 Documentação**: 200+ páginas

## 🎯 **Organização por Propósito**

### 📚 **Educacional**
- `apresentacao/` - Slides para aulas
- `docs/` - Tutoriais e guias
- `examples/` - Código para estudo
- `assets/` - Material visual

### 💻 **Técnico**
- `api/` - Código da aplicação
- `scripts/` - Automação
- Arquivos de configuração (Docker, Git)

### 🎬 **Multimídia**
- Vídeos educacionais
- Diagramas e infográficos
- Assets visuais

## 🔍 **Navegação Rápida**

### **Para Começar**
1. 📄 `README.md` - Visão geral
2. 📖 `docs/GUIA_INSTALACAO.md` - Como instalar
3. 🚀 `scripts/criar_projeto.sh` - Criar do zero

### **Para Estudar**
1. 📊 `apresentacao/` - Conceitos visuais
2. 📖 `docs/TUTORIAL_PASSO_A_PASSO.md` - Tutorial completo
3. 💡 `examples/` - Código de exemplo

### **Para Implementar**
1. 🚀 `api/src/` - Código fonte
2. 📖 `docs/CHECKLIST_IMPLEMENTACAO.md` - Lista de tarefas
3. 🔧 `scripts/` - Automação

### **Para Ensinar**
1. 📊 `apresentacao/` - Slides prontos
2. 🎬 `assets/` - Vídeos e imagens
3. 📖 `docs/` - Material de apoio

## 🎓 **Uso Recomendado**

### **Estudantes**
```bash
# 1. Clonar repositório
git clone <repositorio>

# 2. Estudar conceitos
open apresentacao/introducao.html

# 3. Seguir tutorial
open docs/TUTORIAL_PASSO_A_PASSO.md

# 4. Praticar com exemplos
cd examples && python livro_tutorial.py

# 5. Implementar projeto
cd api && ./install.sh
```

### **Instrutores**
```bash
# 1. Preparar material
cp -r apresentacao/ minha-aula/
cp -r assets/ minha-aula/

# 2. Personalizar slides
# Editar apresentacao/*.html

# 3. Preparar ambiente para alunos
./scripts/criar_projeto.sh

# 4. Distribuir projeto base
tar -czf projeto-alunos.tar.gz api/
```

### **Desenvolvedores**
```bash
# 1. Estudar arquitetura
cd api/src && find . -name "*.py" -exec head -20 {} \;

# 2. Executar projeto
cd api && docker-compose up

# 3. Testar API
curl http://localhost:5001/api/health

# 4. Modificar e expandir
# Implementar novas features
```

## 🔄 **Atualizações Futuras**

### **Planejadas**
- [ ] Testes unitários completos
- [ ] Frontend React/Vue
- [ ] Deploy automatizado
- [ ] Mais exemplos de DDD
- [ ] Tradução para inglês

### **Sugestões**
- Microserviços
- Event Sourcing
- CQRS
- GraphQL API
- Kubernetes

---

**💡 Esta estrutura foi projetada para ser educacional, prática e profissional ao mesmo tempo!**

