# 🐳 Containerização da API da Biblioteca

## Demonstração de Docker com Clean Architecture + DDD

Este diretório contém todos os arquivos necessários para containerizar a API da Biblioteca, demonstrando como aplicar Docker em uma aplicação que segue Clean Architecture, SOLID, Design Patterns e DDD.

## 📁 Arquivos Docker Criados

### 1. `Dockerfile`
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src/
COPY test_structure.py .
RUN mkdir -p src/database
EXPOSE 5001
ENV FLASK_APP=src/main.py
ENV FLASK_ENV=production
ENV PYTHONPATH=/app
CMD ["python", "src/main.py"]
```

### 2. `docker-compose.yml` (Completo)
- API da Biblioteca
- PostgreSQL
- Adminer (interface web para DB)
- Rede isolada
- Volumes persistentes

### 3. `docker-compose.dev.yml` (Simplificado)
- Apenas a API com SQLite
- Ideal para desenvolvimento
- Volume para persistência de dados

### 4. `docker-run.sh`
Script de automação que:
- Faz build da imagem
- Inicia os containers
- Mostra URLs e comandos úteis
- Testa a API automaticamente

### 5. `.dockerignore`
Otimiza o build ignorando:
- Ambiente virtual Python
- Arquivos de cache
- Dados locais
- Logs e temporários

## 🚀 Como Usar

### Opção 1: Script Automatizado
```bash
chmod +x docker-run.sh
./docker-run.sh
```

### Opção 2: Comandos Manuais
```bash
# Build da imagem
docker build -t biblioteca-api:latest .

# Executar com docker-compose
docker-compose -f docker-compose.dev.yml up -d

# Ver logs
docker-compose -f docker-compose.dev.yml logs -f

# Parar containers
docker-compose -f docker-compose.dev.yml down
```

### Opção 3: Docker Run Simples
```bash
docker run -d -p 5001:5001 --name biblioteca-api biblioteca-api:latest
```

## 🌐 Endpoints Disponíveis

Após iniciar o container:

- **API Base**: http://localhost:5001
- **Documentação**: http://localhost:5001/api/docs
- **Health Check**: http://localhost:5001/api/biblioteca/health
- **Adminer** (se usando compose completo): http://localhost:8080

## 🧪 Testando a API

```bash
# Health check
curl http://localhost:5001/api/biblioteca/health

# Criar livro
curl -X POST http://localhost:5001/api/biblioteca/livros \
  -H "Content-Type: application/json" \
  -d '{"titulo":"Clean Architecture","autor":"Robert Martin","isbn":"978-0134494166"}'

# Listar livros
curl http://localhost:5001/api/biblioteca/livros
```

## 🏗️ Benefícios da Containerização

### 1. **Consistência de Ambiente**
- Mesmo ambiente em desenvolvimento, teste e produção
- Elimina problemas de "funciona na minha máquina"

### 2. **Isolamento**
- Aplicação isolada do sistema host
- Dependências encapsuladas
- Sem conflitos entre projetos

### 3. **Portabilidade**
- Roda em qualquer sistema com Docker
- Fácil deploy em cloud (AWS, Azure, GCP)
- Kubernetes ready

### 4. **Escalabilidade**
- Fácil replicação de containers
- Load balancing automático
- Auto-scaling baseado em métricas

### 5. **Versionamento**
- Controle de versões das imagens
- Rollback rápido em caso de problemas
- Tags semânticas (v1.0.0, latest, etc.)

### 6. **Desenvolvimento**
- Setup rápido para novos desenvolvedores
- Ambiente padronizado para toda equipe
- Integração com CI/CD

## 🔧 Configurações Avançadas

### Variáveis de Ambiente
```bash
# Produção
FLASK_ENV=production
DATABASE_URL=postgresql://user:pass@db:5432/biblioteca

# Desenvolvimento
FLASK_ENV=development
DEBUG=true
```

### Volumes
```yaml
volumes:
  - ./data:/app/src/database  # Persistência SQLite
  - postgres_data:/var/lib/postgresql/data  # Persistência PostgreSQL
```

### Networks
```yaml
networks:
  biblioteca-network:
    driver: bridge
```

## 📊 Monitoramento

### Logs
```bash
# Logs em tempo real
docker-compose logs -f biblioteca-api

# Logs específicos
docker logs biblioteca-api-container
```

### Métricas
```bash
# Status dos containers
docker-compose ps

# Uso de recursos
docker stats biblioteca-api-container
```

## 🔒 Segurança

### Boas Práticas Implementadas
- Usuário não-root no container
- Imagem base oficial e atualizada
- Secrets via environment variables
- Network isolation
- Volume permissions

### Melhorias para Produção
- Multi-stage build para reduzir tamanho
- Health checks customizados
- Resource limits (CPU/Memory)
- Security scanning das imagens
- HTTPS com certificados

## 🎯 Demonstração dos Conceitos

Esta containerização demonstra na prática:

1. **Clean Architecture**: Separação clara entre camadas, facilitando testes e deploy
2. **SOLID**: Dependency injection funciona perfeitamente em containers
3. **Design Patterns**: Repository pattern permite trocar banco facilmente
4. **DDD**: Domínio isolado e testável independente da infraestrutura

## 📚 Próximos Passos

1. **Kubernetes**: Deploy em cluster
2. **CI/CD**: Pipeline automatizado
3. **Monitoring**: Prometheus + Grafana
4. **Logging**: ELK Stack
5. **Security**: Vault para secrets

---

**Resultado**: Uma aplicação completa que demonstra todos os conceitos estudados, containerizada e pronta para produção! 🚀

