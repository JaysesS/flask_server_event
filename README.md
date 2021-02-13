# Event from server example


### Run

    gunicorn3 -k eventlet --access-logfile - --bind 0.0.0.0:5000 -w 1 app:app

    Write file name in input! 1 or 2.