# вычисляет угол между минутной и часовой стрелкой

import datetime

def calc_angel(t: datetime.time) -> float:
    h = t.hour
    if h > 12:
        h -= 12
    hour_angle = 0.5 * (h * 60 + t.minute)
    minute_angle = 6 * t.minute
    angle = abs(hour_angle - minute_angle)
    return min(angle, 360 - angle)

angel = calc_angel(datetime.datetime.now())
print(angel)
