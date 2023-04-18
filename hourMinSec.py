def getHoursMinutesSeconds(totalSeconds):
    
    if totalSeconds == 0:
        return '0s'
    
    hms = []
    hours = totalSeconds//3600
    if hours >= 1:
        totalSeconds -= hours * 3600
        hms.append(str(hours) + 'h')
    
    minutes = totalSeconds//60
    if minutes >= 1:
        totalSeconds -= minutes * 60
        hms.append(str(minutes) + 'm')
    
    seconds = totalSeconds
    if seconds >= 1:
        hms.append(str(seconds) + 's')
    
    return ' '.join(hms)

assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getHoursMinutesSeconds(90042) == '25h 42s'
assert getHoursMinutesSeconds(0) == '0s'