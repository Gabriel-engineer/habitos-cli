"""Testes automatizados para o módulo manager."""

from __future__ import annotations

import pytest

from habitos import manager


@pytest.fixture
def tmp_path_data(tmp_path):
    """Fixture que fornece um arquivo JSON temporário para os testes."""
    return tmp_path / "test_data.json"


# ─── Testes: add_habit ────────────────────────────────────────────────────────


def test_add_habit_sucesso(tmp_path_data):
    """Caminho feliz: adicionar um hábito válido."""
    msg = manager.add_habit("Beber água", tmp_path_data)
    assert "adicionado" in msg.lower()

    habits = manager.list_habits(tmp_path_data)
    assert any(h["name"] == "Beber água" for h in habits)


def test_add_habit_nome_vazio_levanta_erro(tmp_path_data):
    """Entrada inválida: nome vazio deve lançar ValueError."""
    with pytest.raises(ValueError, match="vazio"):
        manager.add_habit("", tmp_path_data)


def test_add_habit_nome_apenas_espacos_levanta_erro(tmp_path_data):
    """Entrada inválida: nome com apenas espaços deve lançar ValueError."""
    with pytest.raises(ValueError, match="vazio"):
        manager.add_habit("   ", tmp_path_data)


def test_add_habit_duplicado_retorna_mensagem(tmp_path_data):
    """Caso limite: adicionar hábito já existente não duplica e avisa."""
    manager.add_habit("Meditar", tmp_path_data)
    msg = manager.add_habit("Meditar", tmp_path_data)
    assert "já existe" in msg.lower()

    habits = manager.list_habits(tmp_path_data)
    nomes = [h["name"] for h in habits]
    assert nomes.count("Meditar") == 1


# ─── Testes: complete_habit ───────────────────────────────────────────────────


def test_complete_habit_sucesso(tmp_path_data):
    """Caminho feliz: marcar hábito existente como concluído."""
    manager.add_habit("Exercitar", tmp_path_data)
    msg = manager.complete_habit("Exercitar", tmp_path_data)
    assert "concluído" in msg.lower()

    habits = manager.list_habits(tmp_path_data)
    h = next(h for h in habits if h["name"] == "Exercitar")
    assert h["done"] is True


def test_complete_habit_inexistente_levanta_erro(tmp_path_data):
    """Caso limite: marcar hábito inexistente deve lançar KeyError."""
    with pytest.raises(KeyError):
        manager.complete_habit("Hábito que não existe", tmp_path_data)


def test_complete_habit_ja_concluido_retorna_mensagem(tmp_path_data):
    """Caso limite: concluir hábito já concluído não gera erro."""
    manager.add_habit("Ler", tmp_path_data)
    manager.complete_habit("Ler", tmp_path_data)
    msg = manager.complete_habit("Ler", tmp_path_data)
    assert "já estava" in msg.lower()


# ─── Testes: remove_habit ────────────────────────────────────────────────────


def test_remove_habit_sucesso(tmp_path_data):
    """Caminho feliz: remover hábito existente."""
    manager.add_habit("Dormir cedo", tmp_path_data)
    msg = manager.remove_habit("Dormir cedo", tmp_path_data)
    assert "removido" in msg.lower()

    habits = manager.list_habits(tmp_path_data)
    assert not any(h["name"] == "Dormir cedo" for h in habits)


def test_remove_habit_inexistente_levanta_erro(tmp_path_data):
    """Caso limite: remover hábito inexistente deve lançar KeyError."""
    with pytest.raises(KeyError):
        manager.remove_habit("Não existe", tmp_path_data)


# ─── Testes: summary ─────────────────────────────────────────────────────────


def test_summary_sem_habitos(tmp_path_data):
    """Resumo com nenhum hábito deve retornar zeros."""
    s = manager.summary(tmp_path_data)
    assert s["total"] == 0
    assert s["done"] == 0
    assert s["pending"] == 0


def test_summary_com_habitos_parcialmente_concluidos(tmp_path_data):
    """Resumo deve refletir corretamente o progresso parcial."""
    manager.add_habit("Hábito A", tmp_path_data)
    manager.add_habit("Hábito B", tmp_path_data)
    manager.add_habit("Hábito C", tmp_path_data)
    manager.complete_habit("Hábito A", tmp_path_data)

    s = manager.summary(tmp_path_data)
    assert s["total"] == 3
    assert s["done"] == 1
    assert s["pending"] == 2
