# Event from server example


### Run

    gunicorn3 -k eventlet --access-logfile - --bind 0.0.0.0:5000 -w 1 app:app