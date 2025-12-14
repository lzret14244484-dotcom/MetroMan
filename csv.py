def export_csv(self):
        path = filedialog.asksaveasfilename(defaultextension=".csv")
        if not path:
            return
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "total_seconds"])
            for t in self.tasks:
                writer.writerow([t["name"], t["time"]])

    def import_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV", "*.csv")])
        if not path:
            return
        self.tasks = []
        with open(path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.tasks.append({"name": row["name"], "time": int(row["total_seconds"])})
        self.current_index = 0
        self.remaining = self.tasks[0]["time"] if self.tasks else 0
        self.update_ui()


if __name__ == "__main__":
    root = tk.Tk()
    TaskTimerApp(root)
    root.mainloop()
