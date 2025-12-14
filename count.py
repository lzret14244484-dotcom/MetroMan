 def tick(self):
        if self.remaining <= 0:
            self.skip_task()
            return
        self.remaining -= 1
        self.update_ui()
        self.timer_id = self.root.after(1000, self.tick)

    def start(self):
        if self.timer_id is None and self.tasks:
            self.timer_id = self.root.after(1000, self.tick)

    def pause(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

    def reset(self):
        self.pause()
        self.current_index = 0
        self.remaining = self.tasks[0]["time"] if self.tasks else 0
        self.update_ui()

