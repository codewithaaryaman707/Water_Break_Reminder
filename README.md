

 # 🚰 Drink Water Reminder (Python)

A simple Python-based reminder application that notifies you to drink water at fixed intervals.  
It generates an audio alert using **gTTS**, shows a desktop notification, plays the sound, and repeats automatically.

---

## 📌 Features

- ⏰ Repeats every 15 seconds (modifiable)
- 🔊 Generates voice reminder using gTTS
- 🖥️ Desktop notification support
- 🎶 Plays audio alert
- 🧹 Deletes audio file after playing
- 💻 Works on Windows, Linux, macOS

---

## 🛠️ Tech Stack

- Python  
- gTTS  
- schedule  
- plyer  
- playsound  

---

## 🧩 How It Works

1. The program generates a **new MP3 voice message**.
2. It shows a **desktop notification**.
3. It **plays the voice alert**.
4. It **deletes the MP3 file** after playing.
5. Repeats every 15 seconds.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/drink-water-reminder.git
cd drink-water-reminder
