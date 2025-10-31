import customtkinter as ctk 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class LogiTalk(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("LogiTalk")
        self.geometry("600x600")
        self.minsize(500, 500)
        self.username = None
        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.theme_buttons_visible = False
        self.show_username_prompt()

    def show_username_prompt(self): # Вікно запиту ніку користувача
        self.prompt_frame = ctk.CTkFrame(self)
        self.prompt_frame.pack(expand=True, fill="both")
        #Поверхнасть
        label = ctk.CTkLabel(self.prompt_frame, text="Введите ник:", font=("Arial", 18), text_color="white")
        label.pack(pady=20)
        # Поле для введення ніку
        self.username_entry = ctk.CTkEntry(self.prompt_frame, width=200, placeholder_text="Ваш ник", fg_color="#222244", text_color="white")
        self.username_entry.pack(pady=10)
        self.username_entry.focus()

        btn = ctk.CTkButton(self.prompt_frame, text="Подтвердить", command=self.set_username, fg_color="#3399FF", hover_color="#55AAFF")
        btn.pack(pady=10)
        # Дозволяє натискати Enter замість кнопки
        self.bind('<Return>', lambda e: self.set_username())
    # Метод збереження ніку та переходу до чату
    def set_username(self):
        name = self.username_entry.get().strip()
        if name:
            self.username = name
            self.prompt_frame.destroy()
            self.show_main_ui()
    # Основне вікно чату
    def show_main_ui(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        # Ліва панель з кнопками
        self.sidebar = ctk.CTkFrame(self, width=150)
        self.sidebar.grid(row=0, column=0, sticky="ns")
        # Кнопка для показу панелі зміни теми
        self.theme_toggle_btn = ctk.CTkButton(self.sidebar, text="Сменить тему", command=self.toggle_theme_buttons)
        self.theme_toggle_btn.pack(pady=10, padx=10, fill="x")
        # Кнопка для очищення чату
        self.clear_chat_btn = ctk.CTkButton(self.sidebar, text="Очистить чат", command=self.clear_chat)
        self.clear_chat_btn.pack(pady=10, padx=10, fill="x")
        # Панель кнопок зміни теми
        self.theme_btn_frame = ctk.CTkFrame(self.sidebar)
        self.theme_btn_frame.pack(pady=10, padx=10, fill="x")
        self.theme_btn_frame.pack_forget()
        # Кнопки для вибору темної теми
        self.dark_btn = ctk.CTkButton(self.theme_btn_frame, text="Тёмная", command=lambda: self.change_theme("dark"))
        self.dark_btn.pack(fill="x", pady=5)
        # Кнопка для вибору світлої теми
        self.light_btn = ctk.CTkButton(self.theme_btn_frame, text="Белая", command=lambda: self.change_theme("light"))
        self.light_btn.pack(fill="x", pady=5)
        # Кнопка для вибору голубої теми
        self.blue_btn = ctk.CTkButton(self.theme_btn_frame, text="Голубая", command=lambda: self.change_theme("blue"))
        self.blue_btn.pack(fill="x", pady=5)

        self.chat_frame = ctk.CTkFrame(self)
        self.chat_frame.grid(row=0, column=1, sticky="nsew")
        # Поле для відображення чату
        self.chat_log = ctk.CTkTextbox(self.chat_frame, fg_color="#1E1E1E", text_color="#D4D4D4", width=480, height=450)
        self.chat_log.pack(padx=10, pady=10, fill="both", expand=True)
        self.chat_log.configure(state="disabled")
        # Поле для введення повідомлення
        self.message_entry = ctk.CTkEntry(self.chat_frame, fg_color="#1E1E1E", text_color="#D4D4D4", width=400, placeholder_text="Введите сообщение")
        self.message_entry.pack(side="left", padx=(10, 0), pady=10, fill="x", expand=True)
        self.message_entry.focus()
        # Кнопка для відправки повідомлення
        send_btn = ctk.CTkButton(self.chat_frame, text="Отправить", width=80, command=self.send_message, fg_color="#3399FF", hover_color="#55AAFF")
        send_btn.pack(side="right", padx=(5, 10), pady=10)

        self.bind('<Return>', lambda e: self.send_message())

        self.current_theme = "dark"
        self.apply_theme_colors() # Застосування кольорів теми
    # Зміна теми
    def toggle_theme_buttons(self):
        if self.theme_buttons_visible:
            self.theme_btn_frame.pack_forget()
            self.theme_buttons_visible = False
        else:
            self.theme_btn_frame.pack(pady=10, padx=10, fill="x")
            self.theme_buttons_visible = True
    # Застосування вибраної теми
    def change_theme(self, theme_name):
        if theme_name == "dark":
            ctk.set_appearance_mode("dark")
            ctk.set_default_color_theme("blue")
            self.current_theme = "dark"
        elif theme_name == "light":
            ctk.set_appearance_mode("light")
            ctk.set_default_color_theme("blue")
            self.current_theme = "light"
        elif theme_name == "blue":
            ctk.set_appearance_mode("dark")
            ctk.set_default_color_theme("blue")
            self.current_theme = "blue"
        self.apply_theme_colors()
    
    def apply_theme_colors(self):
        if self.current_theme == "dark":
            chat_bg = "#1E1E1E"
            chat_fg = "#D4D4D4"
            entry_bg = "#1E1E1E"
            entry_fg = "#D4D4D4"
            sidebar_bg = "#2D2D2D"
            btn_fg = "#3399FF"
            btn_hover = "#55AAFF"
        elif self.current_theme == "light":
            chat_bg = "white"
            chat_fg = "black"
            entry_bg = "white"
            entry_fg = "black"
            sidebar_bg = "#F0F0F0"
            btn_fg = "#3399FF"
            btn_hover = "#55AAFF"
        elif self.current_theme == "blue":
            chat_bg = "#8FBCE6" 
            chat_fg = "#003366"
            entry_bg = "#8FBCE6"
            entry_fg = "#003366"
            sidebar_bg = "#2F4F7F"  
            btn_fg = "#AACCEE"
            btn_hover = "#CCE5FF"

        self.chat_log.configure(fg_color=chat_bg, text_color=chat_fg)
        self.message_entry.configure(fg_color=entry_bg, text_color=entry_fg)
        self.sidebar.configure(fg_color=sidebar_bg)
        self.theme_toggle_btn.configure(fg_color=btn_fg, hover_color=btn_hover)
        self.clear_chat_btn.configure(fg_color=btn_fg, hover_color=btn_hover)
    # Очищення чату
    def clear_chat(self):
        self.chat_log.configure(state="normal")
        self.chat_log.delete("0.0", "end")
        self.chat_log.configure(state="disabled")
    # Відправка повідомлення
    def send_message(self):
        msg = self.message_entry.get().strip()
        if msg:
            self.message_entry.delete(0, 'end')
            self.chat_log.configure(state="normal")
            self.chat_log.insert("end", f"{self.username}: {msg}\n")
            self.chat_log.configure(state="disabled")
            self.chat_log.see("end")
# Запуск додатку
if __name__ == "__main__":
    app = LogiTalk()
    app.mainloop()
