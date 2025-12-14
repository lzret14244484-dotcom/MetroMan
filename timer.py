def tick(app):
    if app.remaining <= 0:
        app.skip_task()
        return
    app.remaining -= 1
    app.update_ui()
    app.timer_id = app.root.after(1000, lambda: tick(app))


def start(app):
    if app.timer_id is None and app.tasks:
        app.timer_id = app.root.after(1000, lambda: tick(app))


def pause(app):
    if app.timer_id:
        app.root.after_cancel(app.timer_id)
        app.timer_id = None


def reset(app):
    pause(app)
    app.current_index = 0
    app.remaining = app.tasks[0]["time"] if app.tasks else 0
    app.update_ui()
