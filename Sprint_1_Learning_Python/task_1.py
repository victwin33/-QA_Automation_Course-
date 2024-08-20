times_values = '1h 45m,360s,25m,30m 120s,2h 60s'

for time in times_values.replace(',' , ' ').split(','):
    time_parts = time.split()
    value_minutes = 0
    for part in time_parts:
        if 'h' in part:
            value_minutes += int(part[:-1]) * 60
        if 'm' in part:
            value_minutes += int(part[:-1])
        if 's' in part:
            value_minutes += int(part[:-1]) // 60
    print(value_minutes)
