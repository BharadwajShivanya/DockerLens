# backend/gunicorn_conf.py
bind = "0.0.0.0:5000"        # Listen on all interfaces, port 5000
workers = 2                  # Number of worker processes
loglevel = "info"            # Logging level
user = None                  # Use default user for workers
accesslog = "-"              # Log access to stdout
errorlog = "-"               # Log errors to stdout
timeout = 60                 # Worker timeout (seconds)

