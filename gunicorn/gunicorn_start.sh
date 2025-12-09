#!/bin/bash
# gunicorn_start.sh
# Start script for Gunicorn to be used by systemd or manually.
# Adjust `DJANGODIR`, `USER`, and `VENVDIR` to your server paths/user.

NAME="portfolio_project"
DJANGODIR="/home/ubuntu/portfolio_project"      # Django project directory
SOCKFILE="/run/gunicorn.sock"                   # we will bind to this unix socket
USER="ubuntu"
GROUP="www-data"
NUM_WORKERS=3
NUM_THREADS=2
DJANGO_SETTINGS_MODULE="portfolio_project.settings_production"
VENVDIR="$DJANGODIR/env"                        # path to virtualenv

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
if [ -f "$VENVDIR/bin/activate" ]; then
    source "$VENVDIR/bin/activate"
else
    echo "Virtualenv not found at $VENVDIR. Please create it and install requirements." >&2
    exit 1
fi

# Move to project directory
cd $DJANGODIR || exit 1

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Ensure appropriate permissions for socket directory
sudo mkdir -p /run
sudo chown $USER:$GROUP /run || true

# Exec gunicorn
exec "$VENVDIR/bin/gunicorn" "$NAME.wsgi:application" \
  --name $NAME \
  --workers $NUM_WORKERS \
  --threads $NUM_THREADS \
  --bind unix:$SOCKFILE \
  --log-level=info \
  --pid /run/gunicorn.pid
