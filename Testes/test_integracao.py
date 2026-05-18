"""Testes de integração para o módulo motivacao."""

from __future__ import annotations

from unittest.mock import patch, MagicMock

from motivacao import buscar_frase_motivacional


def test_api_retorna_frase_com_sucesso():
    """Caminho feliz: API responde corretamente e frase é exibida."""
    mock_response = MagicMock()
    mock_response.json.return_value = [{"q": "Seja consistente.", "a": "Autor Teste"}]
    mock_response.raise_for_status = MagicMock()

    with patch("motivacao.requests.get", return_value=mock_response):
        resultado = buscar_frase_motivacional()

    assert "Seja consistente." in resultado
    assert "Autor Teste" in resultado


def test_api_falha_retorna_mensagem_padrao():
    """Caso de falha: erro de rede deve retornar mensagem padrão."""
    with patch("motivacao.requests.get", side_effect=Exception("Erro de rede")):
        resultado = buscar_frase_motivacional()

    assert "Continue firme" in resultado


def test_api_status_erro_retorna_mensagem_padrao():
    """Caso de falha: status HTTP de erro deve retornar mensagem padrão."""
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = Exception("404 Not Found")

    with patch("motivacao.requests.get", return_value=mock_response):
        resultado = buscar_frase_motivacional()

    assert "Continue firme" in resultado
