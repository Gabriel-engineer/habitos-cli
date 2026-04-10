"""Testes automatizados para o módulo storage."""

from __future__ import annotations

from habitos import storage


def test_load_arquivo_inexistente_retorna_dict_vazio(tmp_path):
    """Carregar arquivo que não existe deve retornar dicionário vazio."""
    path = tmp_path / "novo.json"
    data = storage.load(path)
    assert data == {}


def test_save_e_load_preservam_dados(tmp_path):
    """Salvar e carregar deve preservar os dados corretamente."""
    path = tmp_path / "data.json"
    original = {"2025-01-01": {"habits": {"Beber água": True}}}
    storage.save(original, path)
    loaded = storage.load(path)
    assert loaded == original


def test_today_key_formato_correto():
    """A chave de hoje deve estar no formato YYYY-MM-DD."""
    key = storage.today_key()
    parts = key.split("-")
    assert len(parts) == 3
    assert len(parts[0]) == 4  # ano
    assert len(parts[1]) == 2  # mês
    assert len(parts[2]) == 2  # dia
