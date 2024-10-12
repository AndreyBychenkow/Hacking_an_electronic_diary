from datacenter.models import Schoolkid, Chastisement, Lesson, Commendation

# Настройки изменений
FULL_NAME = 'Рябова София Ильинична'
SUBJECT_TITLE = 'История'
PRAISE_TEXT = 'Отлично справилась,скрипт работает)))!'
BAD_GRADES = [2, 3]
NEW_GRADE = 5


# Функция удаления замечаний ученика по полному имени(ФИО).
def remove_chastisements(full_name):
    schoolkid = Schoolkid.objects.filter(full_name=full_name).first()
    if not schoolkid:
        print(f'Ученик с полным именем "{full_name}" не найден.')
        return
    comments = Chastisement.objects.filter(schoolkid=schoolkid)
    if comments.exists():
        comments.delete()
        print(f'Все замечания для {schoolkid.full_name} были удалены.')
    else:
        print(f'У {schoolkid.full_name} нет замечаний.')


remove_chastisements(FULL_NAME)


# Функция для исправления плохих оценок ученика по полному имени(ФИО).
def fix_marks(full_name):
    schoolkid = Schoolkid.objects.filter(full_name=full_name).first()
    if not schoolkid:
        print(f'Ученик с полным именем "{full_name}" не найден.')
        return
    bad_marks = schoolkid.mark_set.filter(points__in=BAD_GRADES)
    if bad_marks.exists():
        for mark in bad_marks:
            mark.points = NEW_GRADE
            mark.save()
        print(f'Все плохие оценки для {schoolkid.full_name} были исправлены.')
    else:
        print(f'У {schoolkid.full_name} нет плохих оценок.')


fix_marks(FULL_NAME)


# Функция добавления хорошего отзыва и предмета ученика по полному имени(ФИО).
def create_commendation(full_name, subject_title):
    schoolkid = Schoolkid.objects.filter(full_name=full_name).first()
    if not schoolkid:
        print(f'Ученик с полным именем "{full_name}" не найден.')
        return
    lesson = Lesson.objects.filter(subject__title=subject_title, group_letter='А', year_of_study=6).order_by(
        '-date').first()
    if lesson:
        Commendation.objects.create(
            text=PRAISE_TEXT,
            created=lesson.date,
            schoolkid=schoolkid,
            subject=lesson.subject,
            teacher=lesson.teacher
        )
        print(f'Похвала для {schoolkid.full_name} была добавлена от учителя по предмету "{subject_title}".')


create_commendation(FULL_NAME, SUBJECT_TITLE)
