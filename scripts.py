from datacenter.models import Schoolkid, Chastisement, Lesson, Commendation

# Настройки изменений
FULL_NAME = 'Белозеров Авдей Федотович'
SUBJECT_TITLE = 'История'
PRAISE_TEXT = 'Отлично справилась,гусь, скрипт работает)))!'
BAD_GRADES = [2, 3]
NEW_GRADE = 5


# Вспомогательная функция для точного нахождения ученика по ФИО
def get_schoolkid(full_name):
    schoolkid = Schoolkid.objects.filter(full_name=full_name).first()
    if not schoolkid:
        print(f'Ученик с полным именем "{full_name}" не найден.')
    return schoolkid


# Функция удаления замечаний ученика по полному имени(ФИО).
def remove_chastisements(full_name):
    schoolkid = get_schoolkid(full_name)
    if not schoolkid:
        return
    deleted_count, _ = Chastisement.objects.filter(schoolkid=schoolkid).delete()
    if deleted_count > 0:
        print(f'Все замечания для {schoolkid.full_name} были удалены.')
    else:
        print(f'У {schoolkid.full_name} нет замечаний.')


remove_chastisements(FULL_NAME)


# Функция для исправления плохих оценок ученика по полному имени(ФИО).
def fix_marks(full_name):
    schoolkid = get_schoolkid(full_name)
    if not schoolkid:
        return
    updated_count = schoolkid.mark_set.filter(points__in=BAD_GRADES).update(points=NEW_GRADE)
    if updated_count > 0:
        print(f'Все плохие оценки для {schoolkid.full_name} были исправлены.')
    else:
        print(f'У {schoolkid.full_name} нет плохих оценок.')


fix_marks(FULL_NAME)


# Функция добавления хорошего отзыва и предмета ученика по полному имени(ФИО).
def create_commendation(full_name, subject_title):
    schoolkid = get_schoolkid(full_name)
    if not schoolkid:
        return
    lesson = Lesson.objects.filter(subject__title=subject_title, group_letter='А', year_of_study=6).select_related(
        'teacher').order_by('-date').first()
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
