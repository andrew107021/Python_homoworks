VOWELS = 'аеёиоуыэюя'


def rhythm(line_in: str) -> None:
    print(
        ('Пам парам', 'Парам пам-пам')[
            len(set(list(([len([x for x in phrase if x.lower() in VOWELS])
                           for phrase in line_in.split()])))) == 1
        ])


line1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'     # Парам пам-пам
line2 = 'пара-ра-раАм рам-пам-папам па-ра-па-дам'     # Пам парам
line3 = 'пЁра-ра-рЯмМ рЕм-пУм-пИпам пО-рЫ-пЭ-дЮм'     # Парам пам-пам
rhythm(line1)
rhythm(line2)
rhythm(line3)
rhythm(input())


