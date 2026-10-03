lecture = ["Аня", "Борис", "Вика", "Гоша", "Аня"]
seminar = ["Вика", "Дима", "Борис", "Ева"]
lectureUnic = set(sorted(lecture))
seminarUnic = set(seminar)
print('Всего уникальных студентов:', len(lectureUnic | seminarUnic))
print('На обеих парах:', sorted(list(lectureUnic & seminarUnic)))
print('Только на лекции:', sorted(list(lectureUnic - seminarUnic)))
print('Хотя бы на одной:', list(lectureUnic | seminarUnic))