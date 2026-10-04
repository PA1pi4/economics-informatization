#!/usr/bin/env python3
"""Запуск обоих решений курса «Экономика информатизации».

Использование:
    python run_all.py
"""

import runpy
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent

TASKS = [
    ("Задача 1. Влияние автоматизации на производительность", BASE / "task1-erp-productivity" / "solution_task1.py"),
    ("Задача 2. Эффективность внедрения облачной CRM", BASE / "task2-crm-efficiency" / "solution_task2.py"),
]


def main() -> int:
    for title, script in TASKS:
        print("\n" + "#" * 80)
        print(f"# {title}")
        print("#" * 80 + "\n")
        if not script.exists():
            print(f"[!] Не найден файл: {script}", file=sys.stderr)
            return 1
        runpy.run_path(str(script), run_name="__main__")
    print("\n[OK] Все решения выполнены.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
