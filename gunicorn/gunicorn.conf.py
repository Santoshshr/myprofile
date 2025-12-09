# Optional Gunicorn config file for extra settings
# This file is referenced if you start gunicorn with `-c gunicorn.conf.py`.
# Minimal sample options here — tune for your workload.
bind = 'unix:/run/gunicorn.sock'
workers = 3
threads = 2
worker_class = 'gthread'
worker_tmp_dir = '/dev/shm'
timeout = 30
loglevel = 'info'
accesslog = '-'
errorlog = '-'
