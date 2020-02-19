import pyttsx3
import database
from Command import CommandHolder, Command
from SpeechSyntez import*

#initiate base answers
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

while (True):
    with sr.Microphone() as source:
        try:
            print("Say something!")
            audio = r.listen(source)
            voice = r.recognize_google(audio, language="ru-RU").lower()
            print(voice)
            speak(result.cost(voice).answer)
        except sr.UnknownValueError:
            print("[log] Голос не распознан!")
        except sr.RequestError as e:
            print("[log] Неизвестная ошибка, проверьте интернет!")

