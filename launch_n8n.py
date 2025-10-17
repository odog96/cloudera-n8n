#!/usr/bin/env python3
import subprocess
import os

# Use correct CML port variable
PORT = os.getenv('CDSW_READONLY_PORT', '8090')

print(f"=== Starting n8n directly ===")
print(f"Port: {PORT}")

# Configure n8n environment
os.environ['N8N_PORT'] = PORT
os.environ['N8N_HOST'] = '127.0.0.1'
os.environ['N8N_LISTEN_ADDRESS'] = '127.0.0.1'
os.environ['N8N_PROTOCOL'] = 'http'
os.environ['N8N_PATH'] = '/'
os.environ['N8N_USER_FOLDER'] = '/home/cdsw/.n8n'
os.environ['DB_SQLITE_POOL_SIZE'] = '2'
os.environ['N8N_BASIC_AUTH_ACTIVE'] = 'false'
os.environ['N8N_DIAGNOSTICS_ENABLED'] = 'true'
os.environ['N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS'] = 'false'
os.environ['N8N_RUNNERS_ENABLED'] = 'true'
os.environ['GENERIC_TIMEZONE'] = 'America/Denver'

print("Starting n8n...")
subprocess.run(['n8n', 'start'])


# #!/usr/bin/env python3
# import subprocess
# import os
# import sys

# # Get the port CML assigns
# port = os.environ.get('CDSW_APP_PORT', '8080')

# print(f"=== Starting n8n ===")
# print(f"Port: {port}")
# print(f"Host: 0.0.0.0")

# # Set n8n environment variables for CML
# os.environ['N8N_PORT'] = port
# os.environ['N8N_HOST'] = '0.0.0.0'
# os.environ['N8N_LISTEN_ADDRESS'] = '0.0.0.0'

# # CRITICAL: Tell n8n it's behind a proxy
# os.environ['N8N_PATH'] = '/'
# os.environ['N8N_PROTOCOL'] = 'https'

# # Don't set WEBHOOK_URL - let n8n auto-detect
# # Remove or don't set: os.environ['WEBHOOK_URL']

# # Use CML project storage for data
# os.environ['N8N_USER_FOLDER'] = '/home/cdsw/.n8n'

# # Database settings
# os.environ['DB_SQLITE_POOL_SIZE'] = '2'

# # Auth settings (from environment variables you set in CML)
# os.environ['N8N_BASIC_AUTH_ACTIVE'] = os.environ.get('N8N_BASIC_AUTH_ACTIVE', 'true')
# os.environ['N8N_BASIC_AUTH_USER'] = os.environ.get('N8N_BASIC_AUTH_USER', 'admin')
# os.environ['N8N_BASIC_AUTH_PASSWORD'] = os.environ.get('N8N_BASIC_AUTH_PASSWORD', 'changeme123')

# os.environ['N8N_DIAGNOSTICS_ENABLED'] = 'true'
# os.environ['N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS'] = 'false'  # ← ADD THIS
# os.environ['N8N_RUNNERS_ENABLED'] = 'true'  # ← ADD THIS

# # Timezone
# os.environ['GENERIC_TIMEZONE'] = 'America/Denver'

# print("=== Environment configured ===")
# print(f"Starting n8n process...")

# # Start n8n - this blocks and keeps running
# try:
#     subprocess.run(['n8n', 'start'], check=True)
# except KeyboardInterrupt:
#     print("n8n stopped")
#     sys.exit(0)
# except Exception as e:
#     print(f"Error starting n8n: {e}")
#     sys.exit(1)