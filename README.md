# Portfolio Project

This is a Django portfolio site. Steps to run locally and prepare static assets for production:

1. Create and activate virtualenv

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run migrations and collect static

```bash
python manage.py migrate
python manage.py collectstatic
```

3. Run server

```bash
python manage.py runserver
```

Notes for production:
- `STATIC_ROOT` is configured; run `collectstatic` and serve `staticfiles/` with your webserver or via WhiteNoise.
- See `portfolio_project/settings.py` for WhiteNoise middleware and storage configuration.
 
Production checklist:
- Set environment variables (see `.env.example`) and keep `DJANGO_DEBUG=False` in production.
- Install production dependencies and run `python manage.py collectstatic`.
- Use `Gunicorn` (Procfile included) or a WSGI process manager behind a reverse proxy.
- Optionally build the included `Dockerfile` for containerized deployments.

Example production commands (after env vars are set):
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn portfolio_project.wsgi:application --bind 0.0.0.0:8000
```

Systemd & Nginx deployment steps (example):

```bash
# 1. Create a virtualenv in the project `env/` directory and install requirements
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

# 2. Collect static and migrate
python manage.py migrate
python manage.py collectstatic --noinput

# 3. Copy systemd unit and reload
sudo cp gunicorn/gunicorn.service /etc/systemd/system/gunicorn.service
sudo systemctl daemon-reload
sudo systemctl enable gunicorn
sudo systemctl start gunicorn

# 4. Copy nginx config and enable
sudo cp nginx/portfolio_project.conf /etc/nginx/sites-available/portfolio_project
sudo ln -s /etc/nginx/sites-available/portfolio_project /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl enable nginx
sudo systemctl restart nginx
```

Notes:
- Ensure `/home/ubuntu/portfolio_project` (WorkingDirectory) matches your actual deployment path.
- Replace `your_domain.com` and certificate paths in the Nginx config before enabling.
- For HTTPS get certificates with Let's Encrypt: `sudo certbot --nginx -d your_domain.com -d www.your_domain.com`.