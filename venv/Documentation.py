from Command import CommandHolder, Command
# Документация по использованию
# Commands
# Для вывода ответа используется поле answer
# Для оценки соответствия ключа строке answerCount
# Команда с единственным ключем
c = Command("трава","зеленая")
# print(c.answerCount("тра"))

# Команда с множественным ключем, работает ключ с наиближайшем сходством
c1 = Command(["ключ", "тест", "сумка"], "ANSWER")
# print(c1.answerCount("тес"))

# CommandHolder
# Без вложений с одной командой
# ch = CommandHolder(c, None)
# print(ch.cost("сума").answer)

# Без вложений с массивом команд
# ch = CommandHolder([c,c1], None)
# print(ch.cost("тест").answer)

# С n вложениями и одной командой
# ch1 = CommandHolder(c1, CommandHolder(c, CommandHolder(c, None)))
# print(ch1.cost("трав").answer)

# Система в действии
c1 = Command(["Университет", "Шарага", "политех"], "Алтгту")

c11 = Command(["фст","специальные технологии"],"Инноватика, машиностроение, ктм")
c12 = Command(["фит","информационные технологии"],"БИ, ПИ, Приборостоение")

c111 = Command("инноватика","помойка")
c112 = Command("машиностроение","не знаю что там")
c113 = Command("ктм","там Ден учится")

c121 = Command("бизнес информатика", "ерунда полная")
c122 = Command("программная инженерия ", "жесть полная")
c123 = Command("приборостроение", "там Вова преподает")

result = CommandHolder(c1,
                    [CommandHolder(c11,
                                   CommandHolder([c111,c112,c113])),
                     CommandHolder(c12,
                                   CommandHolder([c121, c122, c123]))
                     ])

print(result.cost("программная инженер").answer)