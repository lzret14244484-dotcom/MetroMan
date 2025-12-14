 def update_ui(self):
        self.tree.delete(*self.tree.get_children())
        for i, t in enumerate(self.tasks):
            tag = "current" if i == self.current_index else ""
            self.tree.insert("", "end",
                             values=(t["name"], self.format_time(t["time"])),
                             tags=(tag,))

        total = sum(t["time"] for t in self.tasks)
        self.total_label.config(text=f"总时间：{self.format_time(total)}")
        self.remain_label.config(text=f"剩余时间：{self.format_time(self.remaining)}")

        if self.tasks:
            full = self.tasks[self.current_index]["time"]
            self.progress["value"] = (full - self.remaining) / full * 100 if full > 0 else 0
        else:
            self.progress["value"] = 0
