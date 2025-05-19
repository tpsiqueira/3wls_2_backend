import json

ARQUIVO_ORIGINAL = "db.json"
ARQUIVO_LIMPO = "db2.json"

# Lista de modelos obsoletos
MODELOS_OBSOLETOS = [
    "admin_app.ativo",
    "admin_app.relacao_especialista_industrial",
    "monitor_app.analise"
]

def deve_remover(obj):
    modelo = obj.get("model", "")
    campos = obj.get("fields", {})

    # Remove modelos de auth com permissões
    if modelo == "auth.permission":
        return True
    if modelo == "auth.group" and "permissions" in campos:
        return True

    # Remove entradas de logentry com content_type obsoleto
    if modelo == "admin.logentry":
        ct = campos.get("content_type", [])
        if isinstance(ct, list) and len(ct) == 2:
            app_label, model = ct
            if f"{app_label}.{model}" in MODELOS_OBSOLETOS:
                return True

    # Remove qualquer model diretamente marcado como obsoleto
    if modelo in MODELOS_OBSOLETOS:
        return True

    return False

def adicionar_grupo(grupo_nome, dados):
    grupo_existe = any(
        obj["model"] == "auth.group" and obj["fields"].get("name") == grupo_nome
        for obj in dados
    )
    if not grupo_existe:
        dados.append({
            "model": "auth.group",
            "pk": None,  
            "fields": {
                "name": grupo_nome
            }
        })
        print(f"Grupo '{grupo_nome}' adicionado.")

print("Lendo db.json...")
with open(ARQUIVO_ORIGINAL, "r", encoding="utf-8") as f:
    dados = json.load(f)

print("Removendo blocos inválidos...")
dados_filtrados = [obj for obj in dados if not deve_remover(obj)]

# Adiciona os grupos necessários
adicionar_grupo("Usuario", dados_filtrados)
adicionar_grupo("Administrador", dados_filtrados)

with open(ARQUIVO_LIMPO, "w", encoding="utf-8") as f:
    json.dump(dados_filtrados, f, ensure_ascii=False, indent=2)

print(f"Arquivo limpo salvo como: {ARQUIVO_LIMPO}")
