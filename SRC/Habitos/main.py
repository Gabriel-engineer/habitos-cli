"""Interface de linha de comando (CLI) do Hábitos CLI."""
from __future__ import annotations
import argparse
import sys
from habitos import manager


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="habitos",
        description="✅ Hábitos CLI — Acompanhe seus hábitos diários pelo terminal.",
    )
    sub = parser.add_subparsers(dest="comando", required=True)

    # adicionar
    p_add = sub.add_parser("adicionar", help="Adiciona um novo hábito para hoje.")
    p_add.add_argument("nome", help="Nome do hábito")

    # listar
    sub.add_parser("listar", help="Lista os hábitos do dia com status.")

    # concluir
    p_done = sub.add_parser("concluir", help="Marca um hábito como concluído.")
    p_done.add_argument("nome", help="Nome do hábito")

    # remover
    p_rem = sub.add_parser("remover", help="Remove um hábito do dia.")
    p_rem.add_argument("nome", help="Nome do hábito")

    # resumo
    sub.add_parser("resumo", help="Exibe o resumo do progresso do dia.")

    return parser


def run(args: list[str] | None = None) -> None:
    parser = build_parser()
    ns = parser.parse_args(args)

    try:
        if ns.comando == "adicionar":
            print(manager.add_habit(ns.nome))

        elif ns.comando == "listar":
            habits = manager.list_habits()
            if not habits:
                print("Nenhum hábito cadastrado para hoje.")
            else:
                print(f"\n📋 Hábitos de hoje ({len(habits)} total):\n")
                for h in habits:
                    status = "✓" if h["done"] else "○"
                    print(f"  [{status}] {h['name']}")
                print()

        elif ns.comando == "concluir":
            print(manager.complete_habit(ns.nome))

        elif ns.comando == "remover":
            print(manager.remove_habit(ns.nome))

        elif ns.comando == "resumo":
            s = manager.summary()
            pct = int((s["done"] / s["total"]) * 100) if s["total"] else 0
            bar = ("█" * (pct // 10)).ljust(10, "░")
            print(f"\n📊 Progresso do dia: [{bar}] {pct}%")
            print(f"   ✓ Concluídos : {s['done']}")
            print(f"   ○ Pendentes  : {s['pending']}")
            print(f"   Total        : {s['total']}\n")

    except ValueError as e:
        # BUG CORRIGIDO: KeyError era capturado junto com ValueError, mas
        # str(KeyError(...)) inclui aspas extras no Python (ex: "'mensagem'").
        # Separando os except, usamos e.args[0] no KeyError para exibir
        # a mensagem limpa sem aspas desnecessárias.
        print(f"Erro: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyError as e:
        print(f"Erro: {e.args[0]}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    run()


if __name__ == "__main__":
    main()
