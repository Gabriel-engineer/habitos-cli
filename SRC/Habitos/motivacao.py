import requests


def buscar_frase_motivacional():
    try:
        response = requests.get("https://zenquotes.io/api/today", timeout=5)
        response.raise_for_status()
        dados = response.json()
        frase = dados[0]["q"]
        autor = dados[0]["a"]
        return f'💡 "{frase}" — {autor}'
    except Exception:
        return "💡 Continue firme nos seus hábitos!"
