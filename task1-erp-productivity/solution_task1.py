import sys
from pathlib import Path

# Принудительная установка UTF-8 для корректного вывода русского текста в консоль Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Включение поддержки русского языка в графиках
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'DejaVu Sans', 'SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# Исходные данные
departments = ['A', 'B', 'C', 'D', 'E']
before = np.array([120, 135, 110, 150, 130])
after = np.array([145, 155, 140, 160, 150])

# Создаем DataFrame
df = pd.DataFrame({
    'Отдел': departments,
    'До внедрения': before,
    'После внедрения': after
})

# Расчет абсолютного и относительного прироста
df['Абсолютный прирост'] = df['После внедрения'] - df['До внедрения']
df['Относительный прирост, %'] = (df['Абсолютный прирост'] / df['До внедрения']) * 100

# Средние значения
mean_before = np.mean(before)
mean_after = np.mean(after)

# Вывод результатов
print("="*60)
print("ТЕМА 1: Оценка влияния автоматизации на производительность")
print("="*60)
print(df.to_string(index=False))
print("\n" + "-"*60)
print(f"Средняя выработка ДО внедрения: {mean_before:.2f} тыс. руб./чел.")
print(f"Средняя выработка ПОСЛЕ внедрения: {mean_after:.2f} тыс. руб./чел.")
print(f"Абсолютный прирост: {mean_after - mean_before:.2f} тыс. руб./чел.")
print(f"Относительный прирост: {((mean_after - mean_before) / mean_before * 100):.2f}%")

# t-критерий Стьюдента для зависимых выборок (парный)
t_stat, p_value = stats.ttest_rel(after, before)

print("\n" + "-"*60)
print("Статистическая проверка гипотезы (парный t-критерий):")
print(f"t-статистика = {t_stat:.4f}")
print(f"p-value = {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Вывод: p-value < 0.05 -> Отвергаем H0. Рост производительности СТАТИСТИЧЕСКИ ЗНАЧИМ.")
else:
    print("Вывод: p-value >= 0.05 -> Не отвергаем H0. Рост производительности НЕ ЗНАЧИМ.")

# Визуализация
plt.figure(figsize=(8,5))
x = np.arange(len(departments))
width = 0.35
plt.bar(x - width/2, before, width, label='До внедрения', color='skyblue')
plt.bar(x + width/2, after, width, label='После внедрения', color='orange')
plt.xlabel('Отделы')
plt.ylabel('Выработка, тыс. руб./чел.')
plt.title('Динамика производительности труда')
plt.xticks(x, departments)
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()

# Сохранение диаграммы в файл рядом со скриптом (без plt.show, чтобы не блокировать run_all.py)
out_png = Path(__file__).resolve().parent / "illustration.png"
plt.savefig(out_png, dpi=150, bbox_inches="tight")
plt.close()

# Дополнительный вывод: медианная оценка
print("\n" + "-"*60)
print("Медианная оценка эффекта:")
print(f"Медиана ДО: {np.median(before):.2f}")
print(f"Медиана ПОСЛЕ: {np.median(after):.2f}")
print(f"Медианный прирост: {np.median(after) - np.median(before):.2f}")