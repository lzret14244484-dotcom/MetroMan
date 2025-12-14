def format_time(sec):
    h = sec // 3600
    m = sec % 3600 // 60
    s = sec % 60
    return f"{h:02}:{m:02}:{s:02}"
