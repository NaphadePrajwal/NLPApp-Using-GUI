# 🧠 NLPApp - Natural Language Processing Desktop Application

**NLPApp** is a beginner-friendly, GUI-based Natural Language Processing desktop application built with **Python** and **Tkinter**. This project integrates powerful NLP libraries like **TextBlob** and **spaCy** to perform essential language processing tasks such as **Sentiment Analysis**, **Named Entity Recognition**, and **Emotion Detection**.

This app provides an intuitive interface for users to enter text, analyze it using pre-trained NLP models, and view the results in a clean and modern format. It also includes user authentication (Register/Login) using a local Json files

---

## 🌟 Key Features

### 🔐 User Authentication
- User-friendly **Login and Registration** system.
- Data stored locally using **SQLite**.
- Basic input validation and error handling.

### 📊 Sentiment Analysis
- Analyzes the input text and returns:
  - **Polarity** (value from -1 to +1 indicating negativity/positivity)
  - **Subjectivity** (value from 0 to 1 indicating objectivity/subjectivity)
- Powered by **TextBlob**, a simple yet effective NLP library.

### 🧠 Named Entity Recognition (NER)
- Detects **entities** (people, places, organizations, etc.) in the text.
- Shows each recognized entity along with its **label** (like `PERSON`, `ORG`, `GPE`, etc.).
- Uses **spaCy**’s pretrained English NLP model (`en_core_web_sm`).

### 😊 Emotion Detection (Prototype)
- Currently provides **mock emotion predictions** (static values).
- Can be upgraded using external APIs or a custom ML model in the future.

---

## 🖼️ Example Output

### Login Page
![image](https://github.com/user-attachments/assets/4ed7ff55-6909-4952-b95c-da17825b977e)

### Register Page
![image](https://github.com/user-attachments/assets/608402a0-4596-412f-8cb0-1769a4cc02a3)

### Dashboard
![image](https://github.com/user-attachments/assets/5154ac06-db21-4d88-a118-69eaf77f64db)

### Sentiment Analysis
![image](https://github.com/user-attachments/assets/ed39b3a7-2272-4aff-af3e-3130316a3205)

### Names Entity Recognition(NER)
![image](https://github.com/user-attachments/assets/51a4ba22-ac59-4e64-a3fc-66dfe1c26ef3)

### Emotion Detection
![image](https://github.com/user-attachments/assets/b2778eb4-cb6f-4d46-a3ea-a7b3d6f03be1)


