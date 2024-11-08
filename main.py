import pygame
import time
import os
import logging

# Налаштування логування
logging.basicConfig(
    filename="music_player.log",   # Ім'я файлу для збереження логів
    level=logging.INFO,            # Рівень логування
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Вкажіть шлях до файлу з музикою
music_file = "/home/galmed/A_minute_of_silence/silens.mp3"

# Перевірка наявності файлу
if not os.path.exists(music_file):
    logging.error(f"Файл '{music_file}' не знайдено!")
else:
    pygame.mixer.init()
    logging.info("Ініціалізація pygame.mixer завершена.")

    # Функція для програвання аудіофайлу
    def play_music():
        try:
            pygame.mixer.music.load(music_file)
            logging.info(f"Програвання файлу: {music_file}")
            pygame.mixer.music.play()
            # Затримка для прослуховування протягом 3 хвилин або до кінця файлу
            time.sleep(121)
            pygame.mixer.music.stop()
            logging.info("Відтворення завершено.")
        except Exception as e:
            logging.error(f"Помилка під час відтворення: {e}")


if __name__ == "__main__":
    play_music()
