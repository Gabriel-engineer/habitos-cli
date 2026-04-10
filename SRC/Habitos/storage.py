"""Módulo de persistência: leitura e escrita de hábitos em arquivo JSON."""
from __future__ import annotations
import json
from datetime import date
from pathlib import Path

DEFAULT_PATH = Path.home() / ".habitos_cli" / "data.json"


def _ensure_file(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(json.dumps({}), encoding="utf-8")


def load(path: Path = DEFAULT_PATH) -> dict:
    """Carrega os dados do arquivo JSON."""
    _ensure_file(path)
    content = path.read_text(encoding="utf-8").strip()
    if not content:
        return {}
    return json.loads(content)


def save(data: dict, path: Path = DEFAULT_PATH) -> None:
    """Salva os dados no arquivo JSON."""
    _ensure_file(path)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def today_key() -> str:
    """Retorna a data de hoje como chave string no formato YYYY-MM-DD."""
    return date.today().isoformat()
