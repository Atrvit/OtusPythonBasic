## Репозиторий для домашек по курсе Python Developer. Basic

# Домашнее задание разработано для курса "[Python Developer. Basic](https://otus.ru/lessons/python-basic/)"


## Подготовка репозитория для сдачи домашних заданий
- создайте новую папку, где будете хранить решения домашних заданий
- добавьте README файл в корень папки (это часть первой домашки)
- скачайте данный репозиторий, эту ветку (или склонируйте репозиторий и переключитесь на данную ветку)
- скопируйте файл `run_tests.yml` в папку `.github/workflows` (получится `.github/workflows/run_tests.yml`)
- скопируйте папку `testing` в корень вашего репозитория (в папку с readme файлом)
- убедитесь, что в вашем репозитории присутствует файл `.github/workflows/run_tests.yml` для GitHub Actions,
  а также папка `testing`, в которой находятся все тесты


### Важно!

> Не создавайте в проекте (не копируйте в ваш проект) папки домашек (`homework_01`, `homework_03`, etc),
> если не собираетесь их выполнять. Если загрузить невыполненное дз, тесты упадут.
> Если решения не будет вовсе (просто отсутствует модуль с домашкой), тест "пройдёт мимо" и не упадёт.


## Выполнение домашнего задания
- скачайте данный репозиторий, эту ветку (или склонируйте репозиторий и переключитесь на данную ветку)
- скопируйте папку `homework_02` в корень своего проекта (где `02` это номер домашней работы, которую вы выполняете)
- используйте каркас, доступный в этой папке, для выполнения домашней работы (редактируйте доступные файлы)
- не изменяйте имя папки, файлов, а также тесты
- созданные функции и классы не нужно переименовывать, так как тесты будут искать их для выполнения проверок,
  тем не менее можно (и зачастую нужно) редактировать (добавлять) параметры функций
- все зависимости, которые использует ваш проект, должны быть "заморожены" в корне репозитория: `pip freeze > requirements.txt`.
  Обновляйте файл по мере добавления новых зависимостей.
  Добавляйте в зависимости только то, что нужно для выполнения домашки, не нужно отправлять туда всё содержимое виртуального окружения
- **Перед сдачей домашки обязательно убедитесь, что тест `homework_0x` прошёл (`PASSED`), а не пропущен (`SKIPPED`)**


## Памятка по выполнению домашних заданий
- для проверки домашнего задания используются автоматические тесты
- не для каждого домашнего задания есть тесты.
  Однако, если тесты для определенного домашнего задания присутствуют в данном репозитории, они должны пройти
- решенным считается то домашнее задание, для которого полностью прошли соответствующие тесты - в таком случае "зачёт"
- код решения домашнего задания должен работать относительно папки домашнего задания. То есть файл `main.py` должен находиться в папке `homework_02` (соответственно для каждой домашки)
- все домашки должны быть в своих папках, всё в одной ветке, чтобы можно было сразу видеть количество выполненных домашек
- перед сдачей домашки убедитесь, что тесты проходят.
  Для этого можно выполнить их локально: `pytest testing/test_homework_02 -s -vv` из корня проекта
  - установите необходимые зависимости в текущее окружение: `pip install -r requirements-dev.txt`
  - не забудьте изменить номер домашки для проверки другого модуля
- также проверьте, что тесты прошли и на GitHub (для этого в репозитории необходимо перейти в раздел **Actions**)
- тесты не должны быть изменены: они должны совпадать с исходными тестами (находящимися в этом репозитории)
- в некоторых заданиях необходимо использовать переменные окружения (вы поймёте, когда это будет нужно, на первых домашках пропустите).
  Если вы выполняете тесты в терминале, то воспользуйтесь командой `export FOO_BAR=spam_eggs` для объявления в своём окружении.
  При выполнении тестов в PyCharm укажите Environmental variables в свойствах конфигурации теста
