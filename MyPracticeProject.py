import customtkinter as ctk
from tkinter import ttk, messagebox

# Настройки темы
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class UATApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ИС Учет успеваемости — Уфимский Авиационный Техникум")
        self.geometry("1100x600")

        # --- 1. Верхняя панель (Header) ---
        self.header = ctk.CTkFrame(self, fg_color="#1a3661", height=70, corner_radius=0)
        self.header.pack(fill="x", side="top")
        
        self.title_label = ctk.CTkLabel(self.header, 
            text="УФИМСКИЙ АВИАЦИОННЫЙ ТЕХНИКУМ", 
            text_color="white", font=("Segoe UI", 20, "bold"))
        self.title_label.pack(pady=(10, 0), padx=30, side="left")
        
        self.subtitle_label = ctk.CTkLabel(self.header, 
            text="| Автоматизация учёта успеваемости", 
            text_color="#cbd5e0", font=("Segoe UI", 14))
        self.subtitle_label.pack(pady=(15, 0), padx=10, side="left")

        # --- 2. Основная рабочая область ---
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=20, pady=20)

        # Левая панель (Форма ввода)
        self.form_frame = ctk.CTkFrame(self.main_container, width=300, corner_radius=10)
        self.form_frame.pack(side="left", fill="y", padx=(0, 20))
        
        ctk.CTkLabel(self.form_frame, text="Карточка студента", font=("Segoe UI", 16, "bold")).pack(pady=15)
        
        self.entry_fio = ctk.CTkEntry(self.form_frame, placeholder_text="ФИО студента", width=240)
        self.entry_fio.pack(pady=10, padx=20)
        
        self.entry_group = ctk.CTkEntry(self.form_frame, placeholder_text="Группа (напр. 21-АТ-1)", width=240)
        self.entry_group.pack(pady=10, padx=20)
        
        self.combo_subject = ctk.CTkComboBox(self.form_frame, values=["Математика", "Физика", "Информатика", "ТОЭ"], width=240)
        self.combo_subject.set("Выберите предмет")
        self.combo_subject.pack(pady=10, padx=20)
        
        self.entry_grade = ctk.CTkEntry(self.form_frame, placeholder_text="Оценка (2-5)", width=240)
        self.entry_grade.pack(pady=10, padx=20)

        # Кнопки действий
        self.add_btn = ctk.CTkButton(self.form_frame, text="Добавить запись", 
                                    fg_color="#2ecc71", hover_color="#27ae60", command=self.add_student)
        self.add_btn.pack(pady=(20, 10), padx=20, fill="x")

        # Правая панель (Таблица)
        self.table_frame = ctk.CTkFrame(self.main_container, fg_color="white", corner_radius=10)
        self.table_frame.pack(side="right", fill="both", expand=True)

        # Стилизация таблицы (стандартный ttk)
        style = ttk.Style()
        style.configure("Treeview", font=("Segoe UI", 11), rowheight=30)
        style.configure("Treeview.Heading", font=("Segoe UI", 12, "bold"))

        cols = ("id", "fio", "group", "subject", "grade")
        self.tree = ttk.Treeview(self.table_frame, columns=cols, show="headings")
        
        self.tree.heading("id", text="ID")
        self.tree.heading("fio", text="ФИО")
        self.tree.heading("group", text="Группа")
        self.tree.heading("subject", text="Предмет")
        self.tree.heading("grade", text="Оценка")

        self.tree.column("id", width=50, anchor="center")
        self.tree.column("grade", width=80, anchor="center")
        
        self.tree.pack(fill="both", expand=True, padx=5, pady=5)

        # Кнопка удаления под таблицей
        self.del_btn = ctk.CTkButton(self, text="Удалить выбранного студента", 
                                    fg_color="#e63946", hover_color="#c12e3a", command=self.delete_student)
        self.del_btn.pack(pady=10)

    # Логика функций
    def add_student(self):
        fio = self.entry_fio.get()
        group = self.entry_group.get()
        subject = self.combo_subject.get()
        grade = self.entry_grade.get()

        if fio and group and grade:
            # В реальном приложении тут будет SQL INSERT
            new_id = len(self.tree.get_children()) + 1
            self.tree.insert("", "end", values=(new_id, fio, group, subject, grade))
            # Очистка полей
            self.entry_fio.delete(0, 'end')
            self.entry_grade.delete(0, 'end')
        else:
            messagebox.showwarning("Ошибка", "Заполните все поля!")

    def delete_student(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)
        else:
            messagebox.showinfo("Инфо", "Выберите студента в таблице")

if __name__ == "__main__":
    app = UATApp()
    app.mainloop()
# Комментарий для демонстрации обновления логики
