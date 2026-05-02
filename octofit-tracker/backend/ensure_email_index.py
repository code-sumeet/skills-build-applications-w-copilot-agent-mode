import subprocess

# Create unique index on email for users collection in octofit_db
def ensure_unique_email_index():
    cmd = [
        'mongosh',
        '--eval',
        'db = db.getSiblingDB("octofit_db"); db.users.createIndex({ "email": 1 }, { unique: true })'
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print('stdout:\n', result.stdout)
    print('stderr:\n', result.stderr)
    if result.returncode != 0:
        raise SystemExit('Failed to create unique index on email')

if __name__ == "__main__":
    ensure_unique_email_index()
