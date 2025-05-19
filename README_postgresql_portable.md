# Guia de Instalação do PostgreSQL Portable e Migração de Dados

---

## 1. Instale o PostgreSQL Portable na raiz do disco

Exemplo de diretório:

```
C:\postgresql16
```

---

## 2. Crie a pasta `data` dentro de `C:\postgresql16\pgsql`

Exemplo:

```
C:\postgresql16\pgsql\data
```

*Obs: Deixe a pasta vazia para que o banco possa ser inicializado nela.*

---

## 3. Inicialize o cluster com o usuário `admin` (ou outro superusuário)

Abra o terminal e navegue até o diretório `bin`:

```bash
cd C:\postgresql16\pgsql\bin
initdb -U admin -D "C:\postgresql16\pgsql\data"
```

---

## 4. Inicie o servidor PostgreSQL

```bash
cd C:\postgresql16\pgsql\bin
pg_ctl -D "C:\postgresql16\pgsql\data" -l logfile start
```

---

## 5. Conecte-se ao banco padrão `postgres`

```bash
cd C:\postgresql16\pgsql\bin
psql -U admin -d postgres
```

*Após criar o banco `3wls_db`, conecte-se com:*

```bash
cd C:\postgresql16\pgsql\bin
psql -U admin -d 3wls_db
```

---

## 6. Crie a pasta `db` no backend do projeto

```
C:\Users\PD5W\Downloads\BOT\3WLS\3wls_backend\db
```

---

## 7. Crie o tablespace e o banco de dados `3wls_db`

No terminal do `psql`:

```sql
CREATE TABLESPACE ts_3wls LOCATION 'C:/Users/PD5W/Downloads/BOT/3WLS/3wls_backend/db';

CREATE DATABASE "3wls_db"
  TABLESPACE ts_3wls
  OWNER admin;

\l  -- Para listar os bancos e confirmar a criação
```

---

## 8. Exporte os dados do SQLite para JSON

```bash
python exportar_json.py
```

---

## 9. Atualize o `settings.py` do Django

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '3wls_db',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 10. Aplique as migrações no novo banco PostgreSQL

```bash
python manage.py migrate
```

---

## 10.1. Crie um superusuário Django

```bash
python manage.py createsuperuser
```

---

## 11. Limpe permissões desnecessárias e prepare o JSON

```bash
python limpar_json.py
```

---

## 12. Importe os dados processados

```bash
python manage.py loaddata db2.json
```

---

## 13. Apague os arquivos temporários

```bash
del db.json
del db2.json
```

---

## 14. Inicie o servidor Django

```bash
python manage.py runserver
```
