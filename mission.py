 def add_task(self):
        name = self.name_entry.get().strip()
        if not name:
            return
        m = int(self.min_entry.get() or 0)
        s = int(self.sec_entry.get() or 0)
        self.tasks.append({"name": name, "time": m * 60 + s})
        if len(self.tasks) == 1:
            self.remaining = self.tasks[0]["time"]
        self.update_ui()

    def skip_task(self):
        self.current_index += 1
        if self.current_index >= len(self.tasks):
            self.pause()
            self.current_index = 0
        self.remaining = self.tasks[self.current_index]["time"] if self.tasks else 0
        self.update_ui()

    def add_10min(self):
        if not self.tasks:
            return
        self.tasks[self.current_index]["time"] += 600
        self.remaining += 600
        self.update_ui()

    def move_up(self):
        if self.current_index > 0:
            self.tasks[self.current_index - 1], self.tasks[self.current_index] = \
                self.tasks[self.current_index], self.tasks[self.current_index - 1]
            self.current_index -= 1
            self.update_ui()

    def move_down(self):
        if self.current_index < len(self.tasks) - 1:
            self.tasks[self.current_index + 1], self.tasks[self.current_index] = \
                self.tasks[self.current_index], self.tasks[self.current_index + 1]
            self.current_index += 1
            self.update_ui()

    def clear_all(self):
        if not messagebox.askyesno("确认", "确认全部清除并恢复初始状态？"):
            return
        self.pause()
        self.tasks = []
        self.current_index = 0
        self.remaining = 0
        self.update_ui()
