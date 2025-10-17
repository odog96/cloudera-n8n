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
