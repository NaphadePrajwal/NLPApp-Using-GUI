from tkinter import *
from tkinter import ttk, messagebox
from mydb import Database
from myapi import API

class NLPApp:

    def __init__(self):
        self.dbo = Database()
        self.apio = API()

        self.root = Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('400x680')
        self.root.configure(bg='#1C1C1E')

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', background='#1C1C1E', foreground='white', font=('Segoe UI', 11))
        style.configure('TButton', font=('Segoe UI Semibold', 11), padding=10)
        style.configure('Header.TLabel', font=('Segoe UI', 20, 'bold'), foreground='#00BCD4', background='#1C1C1E')
        style.configure('Card.TFrame', background='#2C2C2E', borderwidth=1, relief='ridge')
        style.configure('Card.TLabel', background='#2C2C2E', foreground='white', font=('Segoe UI', 11))
        style.configure('CardHeader.TLabel', background='#2C2C2E', foreground='#00E5FF', font=('Segoe UI', 14, 'bold'))

        self.login_gui()
        self.root.mainloop()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_heading(self, text):
        heading = ttk.Label(self.root, text=text, style='Header.TLabel')
        heading.pack(pady=(30, 20))

    def create_card_frame(self):
        card = ttk.Frame(self.root, style='Card.TFrame', padding=20)
        card.pack(pady=20, padx=30, fill='x')
        return card

    def login_gui(self):
        self.clear()
        self.create_heading("Welcome to NLPApp")

        card = self.create_card_frame()

        ttk.Label(card, text='Email:', style='Card.TLabel').pack(anchor='w', pady=(0, 5))
        self.email_input = ttk.Entry(card, width=40)
        self.email_input.pack(pady=(0, 15), ipady=5)

        ttk.Label(card, text='Password:', style='Card.TLabel').pack(anchor='w', pady=(0, 5))
        self.password_input = ttk.Entry(card, width=40, show='*')
        self.password_input.pack(pady=(0, 15), ipady=5)

        ttk.Button(card, text='🔐 Login', command=self.perform_login).pack(pady=(10, 10))

        ttk.Label(self.root, text="Don't have an account?", style='TLabel').pack(pady=(10, 5))
        ttk.Button(self.root, text='📝 Register Now', command=self.register_gui).pack()

    def register_gui(self):
        self.clear()
        self.create_heading("Register")

        card = self.create_card_frame()

        ttk.Label(card, text='Name:', style='Card.TLabel').pack(anchor='w', pady=(0, 5))
        self.name_input = ttk.Entry(card, width=40)
        self.name_input.pack(pady=(0, 15), ipady=5)

        ttk.Label(card, text='Email:', style='Card.TLabel').pack(anchor='w', pady=(0, 5))
        self.email_input = ttk.Entry(card, width=40)
        self.email_input.pack(pady=(0, 15), ipady=5)

        ttk.Label(card, text='Password:', style='Card.TLabel').pack(anchor='w', pady=(0, 5))
        self.password_input = ttk.Entry(card, width=40, show='*')
        self.password_input.pack(pady=(0, 15), ipady=5)

        ttk.Button(card, text='✅ Register', command=self.perform_registration).pack(pady=(10, 10))

        ttk.Label(self.root, text="Already a member?", style='TLabel').pack(pady=(10, 5))
        ttk.Button(self.root, text='🔑 Login Now', command=self.login_gui).pack()

    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo('Success', 'Registration successful! Please login.')
            self.login_gui()
        else:
            messagebox.showerror('Error', 'Email already exists.')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.search(email, password)

        if response:
            messagebox.showinfo('Success', 'Login successful!')
            self.home_gui()
        else:
            messagebox.showerror('Error', 'Invalid email or password.')

    def home_gui(self):
        self.clear()
        self.create_heading('Dashboard')

        card = self.create_card_frame()

        ttk.Button(card, text='📊 Sentiment Analysis', width=30, command=self.sentiment_gui).pack(pady=10)
        ttk.Button(card, text='🧠 Named Entity Recognition', width=30, command=self.ner_gui).pack(pady=10)
        ttk.Button(card, text='😊 Emotion Prediction', width=30, command=self.emotion_gui).pack(pady=10)
        ttk.Button(card, text='🚪 Logout', width=30, command=self.login_gui).pack(pady=(20, 0))

    def sentiment_gui(self):
        self.clear()
        self.create_heading("Sentiment Analysis")

        card = self.create_card_frame()

        ttk.Label(card, text='Enter your text:', style='Card.TLabel').pack(anchor='w', pady=(0, 5))
        self.sentiment_input = Text(card, height=6, width=42, font=('Segoe UI', 10))
        self.sentiment_input.pack(pady=(0, 15))

        ttk.Button(card, text='Analyze Sentiment', command=self.do_sentiment_analysis).pack(pady=10)

        self.sentiment_result = ttk.Label(card, text='', style='CardHeader.TLabel', wraplength=340, justify='center')
        self.sentiment_result.pack(pady=10)

        ttk.Button(self.root, text='🔙 Go Back', command=self.home_gui).pack(pady=10)

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get("1.0", "end-1c")
        try:
            result = self.apio.sentiment_analysis(text)
            sentiment = result['sentiment']
            txt = f"Polarity: {sentiment['polarity']:.2f}\nSubjectivity: {sentiment['subjectivity']:.2f}"
            self.sentiment_result['text'] = txt
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def ner_gui(self):
        self.clear()
        self.create_heading("Named Entity Recognition")

        card = self.create_card_frame()

        ttk.Label(card, text='Enter your text:', style='Card.TLabel').pack(anchor='w', pady=(0, 5))
        self.ner_input = Text(card, height=6, width=42, font=('Segoe UI', 10))
        self.ner_input.pack(pady=(0, 15))

        ttk.Button(card, text='Extract Entities', command=self.do_ner).pack(pady=10)

        self.ner_result = ttk.Label(card, text='', style='CardHeader.TLabel', wraplength=340, justify='center')
        self.ner_result.pack(pady=10)

        ttk.Button(self.root, text='🔙 Go Back', command=self.home_gui).pack(pady=10)

    def do_ner(self):
        text = self.ner_input.get("1.0", "end-1c")
        try:
            result = self.apio.named_entity_recognition(text)
            entities = result['entities']
            if entities:
                ent_text = "\n".join([f"{text} ({label})" for text, label in entities])
            else:
                ent_text = "No named entities found."
            self.ner_result['text'] = ent_text
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def emotion_gui(self):
        self.clear()
        self.create_heading("Emotion Detection")

        card = self.create_card_frame()

        ttk.Label(card, text='Enter your text:', style='Card.TLabel').pack(anchor='w', pady=(0, 5))
        self.emotion_input = Text(card, height=6, width=42, font=('Segoe UI', 10))
        self.emotion_input.pack(pady=(0, 15))

        ttk.Button(card, text='Detect Emotion', command=self.do_emotion_detection).pack(pady=10)

        self.emotion_result = ttk.Label(card, text='', style='CardHeader.TLabel', wraplength=340, justify='center')
        self.emotion_result.pack(pady=10)

        ttk.Button(self.root, text='🔙 Go Back', command=self.home_gui).pack(pady=10)

    def do_emotion_detection(self):
        text = self.emotion_input.get("1.0", "end-1c")
        try:
            result = self.apio.emotion_detection(text)
            emotions = result['emotion']
            if emotions:
                emo_text = "\n".join([f"{emo}: {val*100:.1f}%" for emo, val in emotions.items()])
            else:
                emo_text = "No emotion detected."
            self.emotion_result['text'] = emo_text
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    NLPApp()
