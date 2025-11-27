from datetime import datetime as dt


def time_responser(selector:str):
    """
    A function to return different time components in the form of a formatted string, based on the input parameter.

    Parameters:
        date = returns today's date in European format.
        time = returns current time of the day.
        datetime = returns today's date and time.
    """
    date = dt.now().strftime('%d-%m-%Y')
    time = dt.now().strftime('%H.%M.%S')

    output={
        'date' : date,
        'time' : time,
        'datetime' : f"{date} {time}"
    }

    try:
        return output.get(selector)
    except: 
        if selector not in output:
            raise ValueError(f"Error: {selector} is NOT a valid parameter. Time_responser only takes 'date', 'time' and 'datetime' as parameters")
