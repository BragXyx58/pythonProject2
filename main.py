import os
from tkinter import *

def hello():
    print("hello world")
def analyze_path():
    path = entry.get()
    if not os.path.exists(path):
        result_label.config(text="Путь не существует.")
        return

    folders = files = 0
    images = music = documents = archives = 0
    count_subdirs = subdir_var.get()
    show_extra_info = extra_info_var.get()

    def file_type_counter(file_name):
        nonlocal images, music, documents, archives
        ext = os.path.splitext(file_name)[1].lower()
        if ext in {".jpg", ".jpeg", ".png", ".gif", ".bmp"}:
            images += 1
        elif ext in {".mp3", ".wav", ".flac", ".aac", ".ogg"}:
            music += 1
        elif ext in {".doc", ".docx", ".pdf", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"}:
            documents += 1
        elif ext in {".zip", ".rar", ".7z", ".tar", ".gz"}:
            archives += 1

    if count_subdirs:
        for root, dirs, files_in_dir in os.walk(path):
            folders += len(dirs)
            for file in files_in_dir:
                files += 1
                if show_extra_info:
                    file_type_counter(file)
    else:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                folders += 1
            elif os.path.isfile(item_path):
                files += 1
                if show_extra_info:
                    file_type_counter(item)

    result_text = f"Папок: {folders}\nФайлов: {files}"
    if show_extra_info:
        result_text += (f"\nКартинок: {images}\nМузыки: {music}\n"
                        f"Документов: {documents}\nАрхивов: {archives}")

    result_label.config(text=result_text)

root = Tk()
root.title("Анализ папок и файлов")
Label(root, text="Введите путь:").pack()
entry = Entry(root, width=50)
entry.pack()
subdir_var = BooleanVar()
Checkbutton(root, text="Учесть вложенные файлы", variable=subdir_var).pack()
extra_info_var = BooleanVar()
Checkbutton(root, text="Доп информация (картинки, музыка, документы, архивы)", variable=extra_info_var).pack()
Button(root, text="Анализировать", command=analyze_path).pack()
result_label = Label(root, text="")
result_label.pack()
hello()
root.mainloop()

