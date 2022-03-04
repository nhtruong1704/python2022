import random

namePrefix = ["А", "Айне", "Арна", "Фионн", "Илле", "Лианн", "Рис"]
namePostfix = ["долл", "ори", "аразу", "ссо", "гейт"]
surnamePrefix = ["Нум", "Онде", "Чор", "Вонд", "Сенв"]
surnamePostfix = ["ад", "дейх", "рок", "эйсайд", "зуст"]
intitial = ["А.", "Б.", "Д.", "С", "Ч."]

n = int(input())

for i in range(n):
    print(random.choice(namePrefix) + random.choice(namePostfix), random.choice(intitial),
          random.choice(surnamePrefix) + random.choice(surnamePostfix))
