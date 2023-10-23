def naughty_or_nice(data):
    naughty_count = 0  
    nice_count = 0  
  
    for month in data:  
        for day in data[month]:  
            if data[month][day] == 'Naughty':  
                naughty_count += 1  
            elif data[month][day] == 'Nice':  
                nice_count += 1  
  
    if naughty_count > nice_count:  
        return 'Naughty!'  
    elif naughty_count < nice_count:  
        return 'Nice!'  
    else:  
        return 'Nice!'