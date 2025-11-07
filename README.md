# DockerLens

A modular Docker management dashboard for monitoring, controlling, and visualizing Docker containers easily.

Phase 1: Project Setup
Create your project skeleton with backend, frontend, nginx, and docker-compose.prod.yml.

Prepare backend Flask app and Dockerfile.

Prepare frontend app and Dockerfile.

Prepare Nginx config.

Status: ✅ Completed
Phase 2: Docker Compose Setup & Basic Build
Write Docker Compose with backend, frontend, nginx services.

Fix YAML indentation errors.

Add volume for Docker socket for backend.

Status: ✅ Completed
Phase 3: Backend API and Gunicorn Setup
Setup Gunicorn to run Flask backend.

Build and run backend container with correct platform and volumes.

Confirm /api/health endpoint responds OK.

Status: ✅ Completed
Phase 4: Compose Network & Ports Configuration
Expose backend port to host using ports: - "5000:5000".

Confirm frontend and nginx containers startup.

Status: ✅ Completed
Phase 5: Docker API Client Integration in Backend
Initial integration of Docker Python SDK (docker.from_env()) in backend.

Encountered socket connection errors: "Error while fetching server API version: Not supported URL scheme http+docker".

Status: ⏳ In Progress
Phase 6: Fix Docker SDK Connection Issues
Remove DOCKER_HOST environment variable if set anywhere.

Make sure socket /var/run/docker.sock is mounted and accessible.

Pin compatible requests and docker Python packages if necessary.

Fix Flask app code to recreate Docker client inside API route function with exception handling.

Status: To do (next)
Phase 7: Full Stack Integration & Testing
Confirm backend Docker API returns container list JSON.

Confirm frontend app communicates correctly with backend APIs.

Status: To do
Phase 8: Production Readiness
Add container health checks, logging, auto-restart policies.

Clean up environment variables, secrets management.

Document deployment steps and architecture.

Status: To do
Phase 9: Advanced Features & Scaling
Add databases, caching layers, CI/CD integration.

Deploy on cloud or orchestrators like Kubernetes.

Status: Future work
