# Задача 1. Инвестор купил акцию 6 лет назад по цене $10. Сейчас он продал ее за $50. 
# Определить, какую доходность принесла ему эта инвестиция в процентах годовых.
print("Задача 1.")
print(round((((50 / 10)**(1/(6))) - 1)*100, 2),"%")

##########################################################################
# Задача 2. Инвестору исполнилось только что 30 лет. Он хочет выйти на пенсию в 60 лет 
# и жить на доход с капитала. Допустим, его целевой уровень капитала к пенсии составляет 
# $350 000. Если он ожидает ставку доходности на рынке порядка 8% годовых, то какую сумму 
# ему надо инвестировать каждый год для достижения цели?
print("Задача 2.")
# Считала по формуле из интернета PMT =  FV / (((1 + i)**n - 1) / i)
print("Сумма, которую инвестор должен пеерчислять каждый год:", round(350000 / (((1 + 0.08)**30 - 1) / 0.08), 2))

##########################################################################
# Задача 3. Человек взял ипотечный кредит на сумму 8 млн руб., на 20 лет под 10% годовых. 
# Погашение кредита будет происходить ежемесячными аннуитетными платежами. Определить, 
# сколько составит общая переплата (сумма процентов) по кредиту.
print("Задача 3.")
PV = 8000000  # Сумма кредита в рублях
i = 10  # Годовая процентная ставка
n = 20  # Срок кредита в годах

# Расчет месячной процентной ставки
month_rate = (i / 12) / 100

# Расчет общего количества платежей (в месяцах)
total_payments = n * 12

# Расчет аннуитетного платежа
annuity_payment = PV * (month_rate * (1 + month_rate)**total_payments) / ((1 + month_rate)**total_payments - 1)

# Расчет общей переплаты (суммы процентов)
total_interest_paid = annuity_payment * total_payments - PV
print(f"Общая переплата по кредиту составит {total_interest_paid:.2f} рублей.")


##########################################################################
# Задача 4. Известно, что безрисковая ставка на рынке составляет 1%, инфляция ожидается 
# 6% годовых и для данного проекта премия за риск равна 4%. Пусть ставка дисконтирования 
# определяется как сумма этих трех составляющих, тогда чему равна приведенная стоимость 
# потоков по проекту, если в первый год ожидается $2000, во второй $5000 и в третьем году 
# проект будет продан за $10000?
print("Задача 4.")
FV1 = 2000  # Денежный поток в первом году
FV2 = 5000  # Денежный поток во втором году
FV3 = 10000  # Денежный поток в третьем году
risk_free_i = 0.01  # Безрисковая ставка
inflation_i = 0.06  # Инфляция
i_premium = 0.04  # Премия за риск
# вычислим ставку дисконтирования ((i)):
i = risk_free_i + inflation_i + i_premium
# вычислим приведенную стоимость ((PV)):
PV = FV1 / (1 + i) + FV2 / (1 + i) ** 2 + FV3 / (1 + i) ** 3
print(round(PV, 2))

##########################################################################
# Задача 5. Что выгодней: положить деньги на депозит под 11% годовых с ежемесячной 
# капитализацией или на депозит под 11,5% с ежегодной капитализацией процентов?
print("Задача 5.")
P = 50000
i = 0.11
k = 12
n = 1

A_monthly = P * (1 + i / k)**(k * n)
print(round(A_monthly, 2))
r = 0.115
k = 1
n = 1

A_annually = P * (1 + i / k)**(k * n)
print(round(A_annually, 2))
if A_monthly > A_annually:
    print("Депозит с ежемесячной капитализацией выгоднее.")
else:
    print("Депозит с ежегодной капитализацией выгоднее.")