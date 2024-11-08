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
music_file = "silens.mp3"  # Замініть на фактичний шлях до файлу

# Перевірка наявності файлу
if not os.path.exists(music_file):
    logging.error(f"Файл '{music_file}' не знайдено!")
else:
    pygame.mixer.init()
    logging.info("Ініціалізація pygame.mixer завершена.")

    # Функція для програвання музики з підвищеною гучністю
    def play_music():
        try:
            pygame.mixer.music.load(music_file)
            pygame.mixer.music.set_volume(1)  # Встановлюємо гучність на 80%
            logging.info(f"Програвання файлу: {music_file} з гучністю 100%")
            pygame.mixer.music.play()
            # Затримка для прослуховування протягом 3 хвилин або до кінця файлу
            time.sleep(180)
            pygame.mixer.music.stop()
            logging.info("Відтворення завершено.")
        except Exception as e:
            logging.error(f"Помилка під час відтворення: {e}")

    if __name__ == "__main__":
        play_music()
