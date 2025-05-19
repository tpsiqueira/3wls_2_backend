import subprocess
import os

# Arquivos
entrada_banco = "db.sqlite3"
saida_temp = "db_temp.json"
saida_final = "db.json"

# Verifica se o banco existe
if not os.path.exists(entrada_banco):
    print(f"Erro: banco de dados '{entrada_banco}' não encontrado.")
    exit(1)

# Executa dumpdata
print("Exportando dados do banco para JSON...")
subprocess.run([
    "python", "manage.py", "dumpdata",
    "--natural-primary", "--natural-foreign",
    "--exclude", "auth.permission",
    "--exclude", "contenttypes",
    f"--output={saida_temp}"
], check=True)

# Corrige codificação
print("Corrigindo codificação e salvando como db.json...")
with open(saida_temp, "r", encoding="latin1") as f:
    conteudo = f.read()

with open(saida_final, "w", encoding="utf-8") as f:
    f.write(conteudo.lstrip('\ufeff'))

# Remove o arquivo temporário
os.remove(saida_temp)

print("Exportação finalizada com sucesso! Arquivo gerado: db.json")
