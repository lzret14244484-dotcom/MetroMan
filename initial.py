class TaskTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("子任务计时器")
        self.root.geometry("750x700")

        self.tasks = []
        self.current_index = 0
        self.remaining = 0
        self.timer_id = None

        self.build_ui()