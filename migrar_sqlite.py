import sqlite3
import os

# Caminho dos arquivos
base_path = r"C:\Users\PD5W\Downloads\BOT\3WLS\3wls_backend"
origem_path = os.path.join(base_path, "db_gideao.sqlite3")
destino_path = os.path.join(base_path, "db.sqlite3")

# Conexões
conn_src = sqlite3.connect(origem_path)
conn_dst = sqlite3.connect(destino_path)

cursor_src = conn_src.cursor()
cursor_dst = conn_dst.cursor()

# Mapeamento das tabelas
mapa_tabelas = {
    "auth_group": "auth_group",
    "auth_group_permissions": "auth_group_permissions",
    "auth_permission": "auth_permission",
    "auth_user": "auth_user",
    "auth_user_groups": "auth_user_groups",
    "auth_user_user_permissions": "auth_user_user_permissions",
    "django_admin_log": "django_admin_log",
    "django_content_type": "django_content_type",
    "django_migrations": "django_migrations",
    "django_session": "django_session",
    "monitor_app_amostra_perf": "perf_app_amostra_perf",
    "monitor_app_analise_perf": "perf_app_analise_perf",
    "admin_app_ativo_perf": "perf_app_ativo_perf",
    "admin_app_grandeza_especialista_perf": "perf_app_grandeza_especialista_perf",
    "admin_app_grandeza_industrial_perf": "perf_app_grandeza_industrial_perf",
    "monitor_app_lookup_servidor_perf": "perf_app_lookup_servidor_perf",
    "admin_app_poco_perf": "perf_app_poco_perf",
    "admin_app_relacao_especialista_industrial_perf": "perf_app_relacao_especialista_industrial_perf",
    "monitor_app_servidor_perf": "perf_app_servidor_perf",
    "monitor_app_sonda_perf": "perf_app_sonda_perf",
    "admin_app_unidade_medida_padrao": "prod_app_unidade_medida_padrao",
    "admin_app_unidade_medida": "prod_app_unidade_medida",
    "admin_app_uo_perf": "perf_app_uo_perf",
    "admin_app_variavel_industrial_perf": "perf_app_variavel_industrial_perf",
    "monitor_app_amostra": "prod_app_amostra",
    "monitor_app_analise": "prod_app_analise",
    "admin_app_ativo": "prod_app_ativo",
    "admin_app_grandeza_especialista": "prod_app_grandeza_especialista",
    "admin_app_grandeza_industrial": "prod_app_grandeza_industrial",
    "admin_app_poco": "prod_app_poco",
    "admin_app_relacao_especialista_industrial": "prod_app_relacao_especialista_industrial",
    "admin_app_uep": "prod_app_uep",
    "admin_app_uo": "prod_app_uo",
    "admin_app_variavel_industrial": "prod_app_variavel_industrial",
    "sqlite_sequence": "sqlite_sequence",
}

# Tabelas duplicadas para os dois apps (perf e prod)
duplicar_unidade_medida = [
    ("admin_app_unidade_medida_padrao", "perf_app_unidade_medida_padrao_perf"),
    ("admin_app_unidade_medida_padrao", "prod_app_unidade_medida_padrao"),
    ("admin_app_unidade_medida", "perf_app_unidade_medida_perf"),
    ("admin_app_unidade_medida", "prod_app_unidade_medida"),
]

print("Iniciando migração de dados...\n")

# Migração das tabelas com correspondência 1:1
for tabela_antiga, tabela_nova in mapa_tabelas.items():
    try:
        print(f"Migrando: {tabela_antiga} -> {tabela_nova}")

        cursor_dst.execute(f"DELETE FROM {tabela_nova}")

        cursor_src.execute(f"PRAGMA table_info({tabela_antiga})")
        colunas = [info[1] for info in cursor_src.fetchall()]
        colunas_str = ", ".join(colunas)
        placeholders = ", ".join(["?"] * len(colunas))

        cursor_src.execute(f"SELECT {colunas_str} FROM {tabela_antiga}")
        dados = cursor_src.fetchall()

        if dados:
            cursor_dst.executemany(
                f"INSERT INTO {tabela_nova} ({colunas_str}) VALUES ({placeholders})", dados
            )
            print(f"  -> {len(dados)} registros inseridos.")
        else:
            print("  -> Nenhum registro encontrado.")
    except Exception as e:
        print(f"  [ERRO] {tabela_antiga}: {e}")

# Migração para as tabelas duplicadas
for tabela_origem, tabela_destino in duplicar_unidade_medida:
    try:
        print(f"Migrando duplicada: {tabela_origem} -> {tabela_destino}")

        cursor_dst.execute(f"DELETE FROM {tabela_destino}")

        cursor_src.execute(f"PRAGMA table_info({tabela_origem})")
        colunas = [info[1] for info in cursor_src.fetchall()]
        colunas_str = ", ".join(colunas)
        placeholders = ", ".join(["?"] * len(colunas))

        cursor_src.execute(f"SELECT {colunas_str} FROM {tabela_origem}")
        dados = cursor_src.fetchall()

        if dados:
            cursor_dst.executemany(
                f"INSERT INTO {tabela_destino} ({colunas_str}) VALUES ({placeholders})", dados
            )
            print(f"  -> {len(dados)} registros inseridos.")
        else:
            print("  -> Nenhum registro encontrado.")
    except Exception as e:
        print(f"  [ERRO] {tabela_origem} -> {tabela_destino}: {e}")

conn_dst.commit()
conn_src.close()
conn_dst.close()

print("\nMigração finalizada.")
