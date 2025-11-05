# backend/gunicorn_conf.py
import multiprocessing
workers = max(2, multiprocessing.cpu_count() * 2 + 1)
bind = "0.0.0.0:5000"
worker_class = "gthread"
threads = 4
timeout = 30
graceful_timeout = 30
keepalive = 2

