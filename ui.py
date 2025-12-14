import tkinter as tk
from tkinter import ttk

def build_ui(app):
    root = app.root

    app.total_label = tk.Label(root, text="总时间：00:00:00", font=("Arial", 18))
    app.total_label.pack(pady=10)

    app.remain_label = tk.Label(root, text="剩余时间：00:00:00", font=("Arial", 16))
    app.remain_label.pack(pady=5)

    ...
    app.progress = ttk.Progressbar(root, length=500)
    app.progress.pack(pady=20)
