# Build completo (reconstrói as imagens)
docker compose build --no-cache

# Subida dos containers em segundo plano
docker compose up -d

# Derruba containers e remove volumes (reseta dados do banco)
docker compose down -v

# Rebuild completo
docker compose build --no-cache

# Sobe novamente
docker compose up -d

# Acessar o shell do Django
docker compose exec web poetry run python manage.py shell

# Rodar comandos de migração
docker compose exec web poetry run python manage.py migrate

# Rodar os testes da aplicação
docker compose exec web poetry run python manage.py test

# Criar superusuário
docker compose exec web poetry run python manage.py createsuperuser

# Entrar no container do banco
docker compose exec db sh

# Dentro do container:
psql -U dev -d bookstore_db
