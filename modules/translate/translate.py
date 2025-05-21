import os
import base64

dirname = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")) #absolute path

input_dir = os.path.join(dirname, "data", "abc")
output_dir = os.path.join(dirname, "decoded_files")

for filename in os.listdir(input_dir):  #full path 
    input_path = os.path.join(input_dir, filename)
    output_path = os.path.join(output_dir, filename)

    try:
        with open(input_path, "r") as f:
            encoded = f.read().strip()
            decoded = base64.b64decode(encoded).decode("utf-8")

        with open(output_path, "w") as f:
            f.write(decoded)
            print(f"+Yes {filename}")

    except Exception as e:
        print("Mistake %s" % e)

    






