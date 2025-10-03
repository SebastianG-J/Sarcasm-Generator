import tkinter as tk
import random

def to_sarcastic(text: str) -> str:
    return "".join(
        random.choice([ch.upper(), ch.lower()]) if ch.isalpha() else ch
        for ch in text
    ) + " " + "🤡"

def generate():
    user_text = input_text.get("1.0", tk.END).strip()
    if not user_text:
        output_label.config(text="Please type something first 😤")
        return
    sarcastic = to_sarcastic(user_text)
    output_label.config(text=sarcastic)

# Create the window
root = tk.Tk()
root.title("Sarcasm Generator 3000")
root.geometry("500x400")
root.config(bg="#282c34")

# Title label
title = tk.Label(root, text="😂 Sarcasm Generator 3000", font=("Arial", 18, "bold"), fg="#61dafb", bg="#282c34")
title.pack(pady=15)

# Input box
input_text = tk.Text(root, height=5, width=50, font=("Arial", 12))
input_text.pack(pady=10)
input_text.bind("<Return>", lambda event: (generate(), "break"))  # Bind Enter key

# Button
generate_btn = tk.Button(root, text="Make it sarcastic!", font=("Arial", 14, "bold"), bg="#61dafb", fg="black", command=generate)
generate_btn.pack(pady=10)

# Output label
output_label = tk.Label(root, text="", wraplength=400, font=("Arial", 14), fg="white", bg="#282c34")
output_label.pack(pady=20)

root.mainloop()
