import os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "files", "MICRODADOS_ENEM_2023.csv")


# Check if the file exists
if os.path.exists(file_path):
    print(f"✅ File found: {file_path}")
else:
    print(f"❌ File NOT found: {file_path}")
