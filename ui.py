def build_ui(self):
        self.total_label = tk.Label(self.root, text="总时间：00:00:00", font=("Arial", 18))
        self.total_label.pack(pady=10)

        self.remain_label = tk.Label(self.root, text="剩余时间：00:00:00", font=("Arial", 16))
        self.remain_label.pack(pady=5)

        btns = tk.Frame(self.root)
        btns.pack(pady=10)

        tk.Button(btns, text="暂停", command=self.pause).pack(side="left", padx=5)
        tk.Button(btns, text="开始", command=self.start).pack(side="left", padx=5)
        tk.Button(btns, text="重置", command=self.reset).pack(side="left", padx=5)
        tk.Button(btns, text="全部清除", command=self.clear_all, bg="red", fg="white").pack(side="left", padx=5)

        self.tree = ttk.Treeview(self.root, columns=("name", "time"), show="headings")
        self.tree.heading("name", text="子任务")
        self.tree.heading("time", text="时间")
        self.tree.pack(fill="x", padx=20, pady=10)
        self.tree.tag_configure("current", background="#ffd6e8")

        add_frame = tk.Frame(self.root)
        add_frame.pack(pady=10)

        self.name_entry = tk.Entry(add_frame, width=20)
        self.name_entry.pack(side="left", padx=5)
        self.min_entry = tk.Entry(add_frame, width=5)
        self.min_entry.pack(side="left")
        self.sec_entry = tk.Entry(add_frame, width=5)
        self.sec_entry.pack(side="left")

        tk.Button(add_frame, text="添加子任务", command=self.add_task).pack(side="left", padx=5)

        ctrl = tk.Frame(self.root)
        ctrl.pack(pady=10)

        tk.Button(ctrl, text="当前任务 +10 分钟", command=self.add_10min).pack(side="left", padx=5)
        tk.Button(ctrl, text="跳过当前任务", command=self.skip_task).pack(side="left", padx=5)
        tk.Button(ctrl, text="当前任务上移", command=self.move_up).pack(side="left", padx=5)
        tk.Button(ctrl, text="当前任务下移", command=self.move_down).pack(side="left", padx=5)

        csv_frame = tk.Frame(self.root)
        csv_frame.pack(pady=10)

        tk.Button(csv_frame, text="导出 CSV", command=self.export_csv).pack(side="left", padx=5)
        tk.Button(csv_frame, text="导入 CSV", command=self.import_csv).pack(side="left", padx=5)

        self.progress = ttk.Progressbar(self.root, length=500)
        self.progress.pack(pady=20)
