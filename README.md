# A Minute of Silence 🎶

Програма для автоматичного програвання аудіофайлу у визначений час щодня (зокрема, в будні дні о 8:58) з використанням Python і `pygame`, із налаштуванням завдань через `cron`.

## Особливості
- Автоматично відтворює аудіофайл у визначений час, який можна налаштувати.
- Використовує модуль `pygame` для відтворення аудіо з можливістю регулювання гучності.
- Підтримка автоматичного планування за допомогою `cron`.
- Логування повідомлень для відстеження стану програми та діагностики помилок.

## Вимоги
- Python 3.x
- Модуль `pygame` (для встановлення: `pip install pygame`)

## Встановлення та налаштування
1. Клонуйте цей репозиторій:
   ```bash
   git clone https://github.com/Gabenoh/minute_of_silens.git

Ось виправлений README.md з правильним форматуванням у Markdown:

markdown
￼Копіювати код
# A Minute of Silence 🎶

Програма для автоматичного програвання аудіофайлу у визначений час щодня (зокрема, в будні дні о 8:58) з використанням Python і `pygame`, із налаштуванням завдань через `cron`.

## Особливості
- Автоматично відтворює аудіофайл у визначений час, який можна налаштувати.
- Використовує модуль `pygame` для відтворення аудіо з можливістю регулювання гучності.
- Підтримка автоматичного планування за допомогою `cron`.
- Логування повідомлень для відстеження стану програми та діагностики помилок.

## Вимоги
- Python 3.x
- Модуль `pygame` (для встановлення: `pip install pygame`)

## Встановлення та налаштування
1. Клонуйте цей репозиторій:
   ```bash
   git clone https://github.com/Gabenoh/minute_of_silens.git
2. Перейдіть до директорії проекту:
  ```bash
  cd minute_of_silens

3. Створіть віртуальне середовище:
  ```bash
python3 -m venv .venv

4.Активуйте віртуальне середовище:

Linux/macOS:
  ```bash
source .venv/bin/activate

Windows:
  ```bash
  .venv\Scripts\activate
5. Встановіть необхідні залежності:

  ```bash
  pip install pygame
  Замініть назву аудіофайлу в коді на назву вашого файлу.

## Налаштування cron для автоматичного запуску
Щоб автоматично запускати програму щодня о 8:58 в будні дні:

1. Відкрийте редактор crontab:

  ```bash
  crontab -e
2. Додайте наступний рядок для запуску програми у віртуальному середовищі:

  ```bash
  58 8 * * 1-5 /home/galmed/A_minute_of_silence/.venv/bin/python /home/galmed/A_minute_of_silence/main.py
Це налаштування забезпечить щоденний запуск скрипта у визначений час.

## Логування
Логування налаштоване для збереження у файлі music_player.log, який буде автоматично створено у директорії проекту. У логах зберігається інформація про запуск, відтворення аудіо та можливі помилки.

Автори
Цей проект створено Gabenoh як частину автоматизованої системи нагадувань.

Ліцензія
MIT License
