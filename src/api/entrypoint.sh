# test: entrypoint.sh

# Exit immediately if a command fails
set -e

# We execute migrations.
core makemigrations
core migrate

# Execute the command passed as an argument.
exec "$@"
