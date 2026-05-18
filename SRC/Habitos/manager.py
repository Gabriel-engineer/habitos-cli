"""Módulo de lógica de negócio: gerenciamento de hábitos diários."""

from __future__ import annotations

from pathlib import Path

from habitos import storage


def _get_today(data: dict, today: str) -> dict:
    return data.setdefault(today, {"habits": {}})


def add_habit(name: str, path: Path = storage.DEFAULT_PATH) -> str:
    """Adiciona um novo hábito. Retorna mensagem de resultado."""
    name = name.strip()
    if not name:
        raise ValueError("O nome do hábito não pode ser vazio.")

    data = storage.load(path)
    today = storage.today_key()
    day = _get_today(data, today)

    if name in day["habits"]:
        return f"Hábito '{name}' já existe para hoje."

    day["habits"][name] = False
    storage.save(data, path)
    return f"Hábito '{name}' adicionado com sucesso!"


def list_habits(path: Path = storage.DEFAULT_PATH) -> list[dict]:
    """Lista os hábitos do dia com seu status."""
    data = storage.load(path)
    today = storage.today_key()
    day = _get_today(data, today)
    storage.save(data, path)

    result = []
    for name, done in day["habits"].items():
        result.append({"name": name, "done": done})
    return result


def complete_habit(name: str, path: Path = storage.DEFAULT_PATH) -> str:
    """Marca um hábito como concluído. Retorna mensagem de resultado."""
    name = name.strip()
    data = storage.load(path)
    today = storage.today_key()
    day = _get_today(data, today)

    if name not in day["habits"]:
        raise KeyError(f"Hábito '{name}' não encontrado para hoje.")

    if day["habits"][name]:
        return f"Hábito '{name}' já estava concluído."

    day["habits"][name] = True
    storage.save(data, path)
    return f"Hábito '{name}' marcado como concluído! ✓"


def remove_habit(name: str, path: Path = storage.DEFAULT_PATH) -> str:
    """Remove um hábito do dia. Retorna mensagem de resultado."""
    name = name.strip()
    data = storage.load(path)
    today = storage.today_key()
    day = _get_today(data, today)

    if name not in day["habits"]:
        raise KeyError(f"Hábito '{name}' não encontrado para hoje.")

    del day["habits"][name]
    storage.save(data, path)
    return f"Hábito '{name}' removido."


def summary(path: Path = storage.DEFAULT_PATH) -> dict:
    """Retorna um resumo do progresso do dia."""
    habits = list_habits(path)
    total = len(habits)
    done = sum(1 for h in habits if h["done"])
    return {"total": total, "done": done, "pending": total - done}
