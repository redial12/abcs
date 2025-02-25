import os



workers = int(os.environ.get('GUNICORN_PROCESSES', '1'))

threads = int(os.environ.get('GUNICORN_THREADS', '1'))

# timeout = int(os.environ.get('GUNICORN_TIMEOUT', '120'))

bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:9000')



forwarded_allow_ips = '*'

secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }