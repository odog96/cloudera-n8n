 # Use CML base runtime image
FROM docker.repository.cloudera.com/cloudera/cdsw/ml-runtime-pbj-workbench-python3.10-standard:2025.09.1-b5
# Install Node.js (required for n8n)
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs

# Install n8n globally
RUN npm install -g n8n

# Create n8n data directory
RUN mkdir -p /home/cdsw/.n8n && \
    chown -R cdsw:cdsw /home/cdsw/.n8n

# Set environment variables
ENV N8N_PORT=8080
ENV N8N_HOST=0.0.0.0
ENV N8N_PROTOCOL=http
ENV N8N_PATH=/
ENV WEBHOOK_URL=https://your-cml-domain.com

# Expose port
EXPOSE 8080

# Set working directory
WORKDIR /home/cdsw

# Override CML metadata labels to make this a unique custom runtime
LABEL com.cloudera.ml.runtime.edition="Custom-n8n"
LABEL com.cloudera.ml.runtime.full-version="1.0.0-n8n"
LABEL com.cloudera.ml.runtime.short-version="1.0"
LABEL com.cloudera.ml.runtime.maintenance-version="0"
LABEL com.cloudera.ml.runtime.description="Custom n8n Automation Runtime"