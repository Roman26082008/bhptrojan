import os
import base64

# Получаем путь до папки bhptrojan
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Вход и выход
input_dir = os.path.join(BASE_DIR, "data", "abc")
output_dir = os.path.join(BASE_DIR, "decoded_files")

# Создать выходную папку, если не существует
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    input_path = os.path.join(input_dir, filename)
    output_path = os.path.join(output_dir, filename)

    if not os.path.isfile(input_path):
        continue

    try:
        with open(input_path, "r") as f:
            encoded = f.read().strip()
            decoded = base64.b64decode(encoded).decode("utf-8")

        with open(output_path, "w") as f:
            f.write(decoded)

        print(f"[+] Декодирован: {filename}")

    except Exception as e:
        print(f"[!] Ошибка в файле {filename}: {e}")
