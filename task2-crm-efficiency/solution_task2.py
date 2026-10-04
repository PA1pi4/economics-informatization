import sys

# Принудительная установка UTF-8 для корректного вывода русского текста в консоль Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


import numpy as np
import pandas as pd

# ============================================================================
# ИСХОДНЫЕ ДАННЫЕ
# ============================================================================

# Количество менеджеров
n_managers = 15

# Зарплата менеджера в месяц (руб.)
salary_per_month = 120000

# Экономия времени на рутинных операциях после внедрения CRM
time_saving = 0.20  # 20%

# Процент рабочего времени на рутинные операции (без CRM)
routine_time = 0.30  # 30%

# Рост продаж после внедрения CRM (умеренный прогноз)
sales_growth = 0.08  # 8% в год

# Текущий годовой оборот отдела продаж (руб.)
current_turnover = 72_000_000

# Стоимость облачной CRM на год на пользователя (руб.)
crm_cost_per_user = 24_000

# Время на обучение (в месяцах)
training_months = 1

# Горизонт оценки (лет)
horizon = 3

# Ставка дисконтирования
discount_rate = 0.12

# Налог на прибыль
tax_rate = 0.20

# ============================================================================
# 1. ОЦЕНКА ПРЯМОГО ЭФФЕКТА
# ============================================================================

print("=" * 80)
print("ОЦЕНКА ЭКОНОМИЧЕСКОЙ ЭФФЕКТИВНОСТИ ВНЕДРЕНИЯ ОБЛАЧНОЙ CRM")
print("=" * 80)
print()

# 1.1. Экономия на заработной плате

# Годовая зарплата всех менеджеров
total_annual_salary = n_managers * salary_per_month * 12
print(f"1.1. Экономия на заработной плате")
print(f"    Годовая зарплата всех менеджеров: {total_annual_salary:,.0f} руб.")
print()

# Доля времени, освобождаемого за счет автоматизации
time_freed = routine_time * time_saving  # 0.30 * 0.20 = 0.06 = 6%
print(f"    Доля рабочего времени на рутинные операции: {routine_time * 100:.0f}%")
print(f"    Экономия времени за счет CRM: {time_saving * 100:.0f}%")
print(f"    Освобождаемая доля рабочего времени: {time_freed * 100:.1f}%")
print()

# Годовая экономия на зарплате
annual_salary_saving = total_annual_salary * time_freed
print(f"    Годовая экономия на заработной плате: {annual_salary_saving:,.0f} руб.")
print()

# 1.2. Дополнительный доход от роста продаж

print("1.2. Дополнительный доход от роста продаж")
print(f"    Текущий годовой оборот: {current_turnover:,.0f} руб.")
print(f"    Прогнозируемый рост продаж: {sales_growth * 100:.0f}% в год")
print()

# Расчет дополнительного дохода по годам (с учетом роста базы)
additional_revenue = []
turnover = current_turnover
for year in range(1, horizon + 1):
    growth = turnover * sales_growth
    additional_revenue.append(growth)
    turnover += growth
    print(f"    Год {year}: дополнительный доход = {growth:,.0f} руб.")
    print(f"    Оборот после года {year}: {turnover:,.0f} руб.")

print()

# ============================================================================
# 2. ОЦЕНКА ЗАТРАТ НА ВНЕДРЕНИЕ
# ============================================================================

print("=" * 80)
print("2. ОЦЕНКА ЗАТРАТ НА ВНЕДРЕНИЕ")
print("=" * 80)
print()

# 2.1. Стоимость лицензий за 3 года
annual_license_cost = n_managers * crm_cost_per_user
total_license_cost = annual_license_cost * horizon

print("2.1. Стоимость лицензий за 3 года")
print(f"    Стоимость на пользователя в год: {crm_cost_per_user:,.0f} руб.")
print(f"    Количество пользователей: {n_managers}")
print(f"    Годовая стоимость лицензий: {annual_license_cost:,.0f} руб.")
print(f"    Стоимость лицензий за 3 года: {total_license_cost:,.0f} руб.")
print()

# 2.2. Потери от снижения производительности в первый месяц обучения
# Потеря одного месяца работы (1/12 от годовой зарплаты)
training_loss = total_annual_salary / 12

print("2.2. Потери от снижения производительности в первый месяц обучения")
print(f"    Время на обучение: {training_months} месяц")
print(f"    Потери: {training_loss:,.0f} руб.")
print()

total_costs = total_license_cost + training_loss
print(f"    Итого затраты на внедрение за 3 года: {total_costs:,.0f} руб.")
print()

# ============================================================================
# 3. РАСЧЕТ ФИНАНСОВЫХ ПОКАЗАТЕЛЕЙ ЭФФЕКТИВНОСТИ
# ============================================================================

print("=" * 80)
print("3. РАСЧЕТ ФИНАНСОВЫХ ПОКАЗАТЕЛЕЙ ЭФФЕКТИВНОСТИ")
print("=" * 80)
print()

# 3.1. Прирост чистой прибыли по годам (с учетом налога)

# Расчет чистого денежного потока по годам
cash_flows = []

print("3.1. Прирост чистой прибыли по годам")
print("    (все суммы указаны в рублях)")
print()

for year in range(1, horizon + 1):
    # Доходы: экономия на зарплате + дополнительный доход
    revenue = annual_salary_saving + additional_revenue[year-1]
    
    # Расходы: стоимость лицензий + потери от обучения (только в первый год)
    costs = annual_license_cost
    if year == 1:
        costs += training_loss
    
    # Прибыль до налога
    profit_before_tax = revenue - costs
    
    # Чистая прибыль после налога
    net_profit = profit_before_tax * (1 - tax_rate)
    
    cash_flows.append(net_profit)
    
    print(f"    Год {year}:")
    print(f"      Доходы: {revenue:,.0f} руб.")
    print(f"      Расходы: {costs:,.0f} руб.")
    print(f"      Прибыль до налога: {profit_before_tax:,.0f} руб.")
    print(f"      Чистая прибыль: {net_profit:,.0f} руб.")
    print()

# 3.2. NPV проекта (при r=12%)

print("3.2. NPV проекта (при r=12%)")

npv = 0
discounted_cash_flows = []

for year, cf in enumerate(cash_flows, start=1):
    discounted_cf = cf / ((1 + discount_rate) ** year)
    discounted_cash_flows.append(discounted_cf)
    npv += discounted_cf
    print(f"    Год {year}: дисконтированный денежный поток = {discounted_cf:,.0f} руб.")

print()
print(f"    NPV проекта: {npv:,.0f} руб.")
print()

# 3.3. Простой срок окупаемости

print("3.3. Простой срок окупаемости")

cumulative_cf = 0
payback_year = None
cumulative_discounted = 0

for year, cf in enumerate(cash_flows, start=1):
    cumulative_cf += cf
    cumulative_discounted += discounted_cash_flows[year-1]
    print(f"    Год {year}: накопленный денежный поток = {cumulative_cf:,.0f} руб.")
    print(f"    Накопленный дисконтированный поток = {cumulative_discounted:,.0f} руб.")
    if payback_year is None and cumulative_cf >= 0:
        payback_year = year

print()
if payback_year is not None:
    print(f"    Простой срок окупаемости: {payback_year} года")
else:
    print(f"    Простой срок окупаемости: более {horizon} лет")
print()

# 3.4. ROI проекта

print("3.4. ROI проекта")

total_net_profit = sum(cash_flows)
total_investments = total_costs
roi = (total_net_profit / total_investments) * 100

print(f"    Суммарная чистая прибыль за {horizon} года: {total_net_profit:,.0f} руб.")
print(f"    Суммарные инвестиции: {total_investments:,.0f} руб.")
print(f"    ROI: {roi:.1f}%")
print()

# ============================================================================
# 4. АНАЛИЗ НЕМАТЕРИАЛЬНЫХ ЭФФЕКТОВ
# ============================================================================

print("=" * 80)
print("4. АНАЛИЗ НЕМАТЕРИАЛЬНЫХ ЭФФЕКТОВ")
print("=" * 80)
print()

print("4.1. Нематериальные выгоды CRM:")
print("    - Улучшение качества обслуживания клиентов")
print("    - Повышение прозрачности бизнес-процессов")
print("    - Улучшение аналитики и принятия решений")
print("    - Повышение удовлетворенности сотрудников")
print("    - Снижение текучести кадров")
print("    - Укрепление конкурентных позиций")
print()

print("4.2. Парадокс производительности Солоу:")
print("    Что это: кажущееся противоречие между инвестициями в ИТ и ростом")
print("    производительности в статистике.")
print()
print("    Как может повлиять на фактический эффект от внедрения:")
print("    - Временной лаг между внедрением и проявлением эффекта")
print("    - Неправильный выбор метрик для оценки эффективности")
print("    - Сопротивление сотрудников нововведениям")
print("    - Недостаточная квалификация персонала")
print("    - Неэффективное использование функционала системы")
print("    - Организационные изменения, необходимые для получения эффекта")
print()

# ============================================================================
# ИТОГОВОЕ ЗАКЛЮЧЕНИЕ
# ============================================================================

print("=" * 80)
print("ИТОГОВОЕ ЗАКЛЮЧЕНИЕ")
print("=" * 80)
print()

print("1. ЭКОНОМИЯ:")
print(f"   - Годовая экономия на зарплате: {annual_salary_saving:,.0f} руб.")
print(f"   - Дополнительный доход за 3 года: {sum(additional_revenue):,.0f} руб.")
print()

print("2. ЗАТРАТЫ:")
print(f"   - Стоимость лицензий за 3 года: {total_license_cost:,.0f} руб.")
print(f"   - Потери от обучения: {training_loss:,.0f} руб.")
print(f"   - Итого затраты: {total_costs:,.0f} руб.")
print()

print("3. ФИНАНСОВЫЕ ПОКАЗАТЕЛИ:")
print(f"   - NPV (r=12%): {npv:,.0f} руб.")
if payback_year is not None:
    print(f"   - Срок окупаемости: {payback_year} года")
else:
    print(f"   - Срок окупаемости: более {horizon} лет")
print(f"   - ROI: {roi:.1f}%")
print()

if npv > 0:
    print("ВЫВОД: Проект экономически ЭФФЕКТИВЕН (NPV > 0).")
    print("Рекомендуется к внедрению.")
else:
    print("ВЫВОД: Проект экономически НЕ ЭФФЕКТИВЕН (NPV <= 0).")
    print("Рекомендуется пересмотреть условия внедрения.")

print()
print("=" * 80)
print("КОНЕЦ РАСЧЕТОВ")
print("=" * 80)