# AI Chat Application

A full-stack AI-powered chat application with containerized microservices, built with **FastAPI**, **React**, **Ollama**, and comprehensive observability through OpenTelemetry, Prometheus, and Trivy security scanning.

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Observability & Monitoring](#observability--monitoring)
- [Security & Vulnerability Scanning](#security--vulnerability-scanning)
- [Load Testing](#load-testing)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This is a containerized AI chat application that leverages **Ollama** (local LLM inference engine) to provide intelligent conversational capabilities. The application features:

- **Modern React Frontend** with real-time chat interface
- **FastAPI Backend** for high-performance API endpoints
- **Ollama Integration** using the Qwen2.5 7B language model
- **End-to-End Observability** with distributed tracing and metrics collection
- **Continuous Security Scanning** with Trivy vulnerability assessment
- **Load Testing** capabilities for performance evaluation

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Client Browser                            │
│                    (React Frontend - Port 3000)                  │
└────────────────────────────┬────────────────────────────────────┘
                             │ HTTP/REST
┌────────────────────────────▼────────────────────────────────────┐
│                      FastAPI Backend                              │
│                      (Port 8000)                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Routes: /chat, /metrics, /                              │   │
│  │ Observability: OpenTelemetry, Prometheus Metrics        │   │
│  │ CORS: Configured for frontend communication             │   │
│  └──────────────────────────────────────────────────────────┘   │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                    Ollama LLM Engine                              │
│                      (Port 11434)                                │
│  Model: Qwen2.5:7B                                              │
│  GPU Support: NVIDIA CUDA enabled                               │
└────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│                   Observability Stack                             │
├──────────────────────────────────────────────────────────────────┤
│ • OpenTelemetry Collector (Traces, Metrics, Logs)               │
│ • Prometheus (Metrics Scraping & Storage)                       │
│ • Tempo (Distributed Tracing Backend)                           │
│ • Grafana Dashboards (Visualization & Analytics)                │
└──────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│                    Security Stack                                │
├──────────────────────────────────────────────────────────────────┤
│ • Trivy (Vulnerability Scanner)                                 │
│ • Security Exporter (Metrics for Trivy findings)                │
│ • Continuous Scanning (Hourly)                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework for building APIs
- **Uvicorn** - ASGI web server
- **Requests** - HTTP client library
- **OpenTelemetry** - Distributed tracing and metrics collection
- **Prometheus Client** - Metrics exposure

### Frontend
- **React 18.2** - UI library
- **React Markdown** - Markdown rendering for chat responses
- **Tailwind CSS** - Utility-first CSS framework
- **PostCSS** - CSS processing

### LLM & ML
- **Ollama** - Local LLM inference engine
- **Qwen2.5:7B** - Language model

### Observability
- **OpenTelemetry SDK & API** - Distributed tracing
- **OpenTelemetry OTLP Exporter** - Export traces to collector
- **Prometheus** - Metrics collection and storage
- **Tempo** - Distributed tracing backend
- **Grafana** - Visualization and dashboards

### Security & DevOps
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **Trivy** - Container vulnerability scanning
- **NVIDIA CUDA** - GPU acceleration for Ollama

### Testing
- **Node.js Load Tester** - Performance testing

---

## ✨ Features

### Core Functionality
✅ **Real-time AI Chat** - Interact with Qwen2.5 language model  
✅ **Streaming Responses** - Non-blocking API calls  
✅ **Token Counting** - Track token usage per request  
✅ **Latency Tracking** - Monitor response times  

### Observability
✅ **Distributed Tracing** - End-to-end request tracing  
✅ **Metrics Collection** - Prometheus metrics exposure  
✅ **Structured Logging** - Event-based logging system  
✅ **Performance Monitoring** - Response latency and token metrics  
✅ **Grafana Dashboards** - Multiple specialized dashboards  

### Security
✅ **Container Scanning** - Trivy vulnerability detection  
✅ **Continuous Scans** - Hourly vulnerability assessment  
✅ **Security Metrics** - Vulnerability metrics export  
✅ **Network Isolation** - Docker network segregation  

### DevOps
✅ **Docker Containerization** - All services containerized  
✅ **Docker Compose Orchestration** - Easy multi-service deployment  
✅ **GPU Support** - NVIDIA CUDA integration for acceleration  
✅ **Load Testing** - Built-in performance testing  

---

## 📁 Project Structure

```
ai-app/
├── README.md                           # This file
├── docker-compose.yml                  # Main orchestration file
│
├── backend/
│   ├── Dockerfile                      # Backend container definition
│   ├── requirements.txt                # Python dependencies
│   └── app/
│       ├── __init__.py
│       ├── main.py                     # FastAPI application entry point
│       ├── routes/
│       │   └── chat.py                 # Chat endpoint with tracing
│       ├── services/
│       │   └── ollama_client.py        # Ollama API integration
│       └── observability/
│           ├── __init__.py
│           ├── logger.py               # Structured logging
│           ├── metrics.py              # Prometheus metrics
│           ├── otel.py                 # OpenTelemetry tracer
│           └── telemetry.py            # Telemetry setup & initialization
│
├── frontend/
│   ├── Dockerfile                      # Frontend container definition
│   ├── package.json                    # Node.js dependencies
│   ├── tailwind.config.js              # Tailwind CSS configuration
│   ├── postcss.config.js               # PostCSS configuration
│   ├── public/
│   │   └── index.html                  # HTML entry point
│   └── src/
│       ├── App.js                      # Main React component
│       ├── index.js                    # React DOM render
│       ├── App.css                     # Application styles
│       ├── index.css                   # Global styles
│       └── components/
│           └── ModernAIChatUI.jsx      # Chat UI component
│
├── ollama/
│   ├── Dockerfile                      # Ollama container definition
│   └── start.sh                        # Ollama startup script
│
├── security/
│   ├── Dockerfile                      # Security tools container
│   ├── scan.sh                         # Trivy scanning script (runs hourly)
│   ├── trivy_metrics.py                # Convert Trivy reports to metrics
│   └── trivy/
│       ├── reports/
│       │   ├── backend.json            # Backend vulnerability report
│       │   ├── frontend.json           # Frontend vulnerability report
│       │   └── ollama.json             # Ollama vulnerability report
│       └── metrics/                    # Metrics from vulnerability scans
│
├── observability/
│   ├── docker-compose.yml              # Observability stack configuration
│   ├── otel-collector.yml              # OpenTelemetry Collector config
│   ├── prometheus.yml                  # Prometheus scrape configuration
│   ├── tempo.yaml                      # Tempo backend configuration
│   └── dashboards/
│       ├── ai_app_obs.json             # Application observability dashboard
│       ├── ai_logs_dashboard.json      # Logs visualization dashboard
│       ├── ai_observability_dashboard.json # Comprehensive dashboard
│       └── ai_vulnerability_dashboard.json # Security findings dashboard
│
├── load-test/
│   ├── Dockerfile                      # Load testing container
│   └── load-test.js                    # Load testing script
│
└── data/
    └── ollama/
        ├── models/                     # Downloaded model data
        ├── cache/                      # Model cache
        ├── history                     # Interaction history
        ├── config.json                 # Ollama configuration
        └── backup/                     # Configuration backups
```

---

## 📦 Prerequisites

Before running the application, ensure you have:

- **Docker** (v20.10+) - https://www.docker.com/
- **Docker Compose** (v1.29+) - Included with Docker Desktop
- **NVIDIA Docker Runtime** (optional, for GPU acceleration)
  ```bash
  # Install nvidia-docker for GPU support
  distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
  curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
  curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
    sudo tee /etc/apt/sources.list.d/nvidia-docker.list
  sudo apt-get update && sudo apt-get install -y nvidia-docker2
  sudo systemctl restart docker
  ```
- **Minimum System Requirements**:
  - 8GB RAM
  - 20GB disk space (for models and containers)
  - 2+ CPU cores

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-app.git
cd ai-app
```

### 2. Create Environment File
```bash
cat > .env << EOF
# Backend Configuration
DEBUG=False
LOG_LEVEL=INFO

# Ollama Configuration
OLLAMA_KEEP_ALIVE=-1
OLLAMA_GPU=true

# Observability
OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4318
OTEL_SERVICE_NAME=ai-backend
EOF
```

### 3. Create Docker Network
```bash
docker network create ai-net
```

### 4. Build All Services
```bash
docker-compose build
```

---

## 📲 Running the Application

### Start All Services
```bash
# Start all containers
docker-compose up -d

# View logs
docker-compose logs -f

# View specific service logs
docker-compose logs -f backend
docker-compose logs -f frontend
docker-compose logs -f ollama
```

### Verify Services Are Running
```bash
# Check running containers
docker-compose ps

# Test backend health
curl http://localhost:8000/

# Test chat endpoint
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello, how are you?"}'

# Access frontend
open http://localhost:3000
```

### Stop All Services
```bash
docker-compose down

# Remove volumes (careful - deletes data)
docker-compose down -v
```

---

## 📚 API Documentation

### Base URL
```
http://localhost:8000
```

### Endpoints

#### 1. Health Check
```
GET /
```
**Response:**
```json
{
  "status": "ok"
}
```

#### 2. Chat Endpoint
```
POST /chat
Content-Type: application/json
```
**Request Body:**
```json
{
  "prompt": "Your question or message here"
}
```
**Response:**
```json
{
  "response": "AI model's response text",
  "latency": 2.345,
  "tokens": 128
}
```
**Example:**
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is machine learning?"}'
```

#### 3. Metrics Endpoint
```
GET /metrics
```
**Response:** Prometheus metrics in text format
**Available Metrics:**
- `request_latency_seconds` - Request processing time
- `request_tokens_total` - Total tokens processed
- `request_count_total` - Total requests count

---

## 📊 Observability & Monitoring

### Access Points

**Prometheus:**
```
http://localhost:9090
```

**Grafana:**
```
http://localhost:3001
```
- Default credentials: `admin` / `admin`

**Tempo (Traces):**
```
http://localhost:3200
```

### Available Dashboards

1. **AI App Observability Dashboard** - Overall system metrics
2. **AI Logs Dashboard** - Structured logs and events
3. **AI Observability Dashboard** - Comprehensive monitoring
4. **AI Vulnerability Dashboard** - Security findings

### Key Metrics

| Metric | Type | Description |
|--------|------|-------------|
| `request_latency_seconds` | Histogram | Response time per request |
| `request_tokens_total` | Counter | Accumulated tokens processed |
| `http_requests_total` | Counter | Total HTTP requests |
| `http_request_duration_seconds` | Histogram | HTTP request duration |

### Distributed Tracing

All requests are traced end-to-end through OpenTelemetry:

```
Frontend Request
    ↓
FastAPI Handler
    ↓
Chat Route (span: chat-request)
    ↓
Ollama Client
    ↓
Response + Metrics
```

View traces in Grafana → Explore → Select Tempo datasource

---

## 🔒 Security & Vulnerability Scanning

### Trivy Vulnerability Scanner

The application includes continuous vulnerability scanning via Trivy:

**Features:**
- ✅ Scans all container images (backend, frontend, ollama)
- ✅ Runs automatically every hour
- ✅ Generates JSON reports
- ✅ Exports metrics to Prometheus
- ✅ Integrates with Grafana dashboards

**Reports Location:**
```
security/trivy/reports/
├── backend.json
├── frontend.json
└── ollama.json
```

**Manual Scanning:**
```bash
# Scan backend image
trivy image --scanners vuln --format json -o reports/backend.json ai-backend

# Scan with higher severity
trivy image --severity HIGH,CRITICAL ai-backend
```

**Accessing Security Metrics:**
- View in Grafana: Dashboard → "AI Vulnerability Dashboard"
- Query Prometheus: `trivy_vulnerabilities_total`

---

## ⚡ Load Testing

### Run Load Tests
```bash
# Start load tester
docker-compose up load-tester

# View load test logs
docker-compose logs load-tester
```

### Load Test Configuration
```javascript
// Default: 100 concurrent users, 1000 total requests
// Endpoints tested: /chat with varying prompts
// Duration: Configurable in load-test.js
```

### Performance Metrics
- **Throughput** - Requests per second
- **Response Time** - Average, P95, P99 latency
- **Success Rate** - Successful responses %
- **Error Rate** - Failed requests %

---

## 🔧 Environment Variables

### Backend Configuration

```bash
# .env file
DEBUG=False                              # Debug mode (True/False)
LOG_LEVEL=INFO                           # Logging level
OLLAMA_KEEP_ALIVE=-1                     # Keep Ollama model in memory
OTEL_EXPORTER_OTLP_ENDPOINT=...          # OpenTelemetry exporter endpoint
OTEL_SERVICE_NAME=ai-backend             # Service name in traces
```

### Frontend Configuration

The frontend connects to the backend via:
```javascript
BASE_URL: http://localhost:8000
```

Modify in `frontend/src/components/ModernAIChatUI.jsx` if deployed differently.

---

## 🔄 Development Workflow

### Backend Development
```bash
# Install dependencies
pip install -r backend/requirements.txt

# Run FastAPI with auto-reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Development
```bash
# Install dependencies
cd frontend
npm install

# Start React dev server
npm start

# Build for production
npm run build
```

### Adding New Features

1. **Backend Route:**
   ```python
   # backend/app/routes/new_feature.py
   from fastapi import APIRouter
   
   router = APIRouter()
   
   @router.post("/new-endpoint")
   def new_endpoint(req: dict):
       return {"status": "ok"}
   ```

2. **Include in main.py:**
   ```python
   from app.routes.new_feature import router as new_router
   app.include_router(new_router)
   ```

3. **Add Tracing:**
   ```python
   from app.observability.otel import tracer
   
   with tracer.start_as_current_span("operation-name"):
       # Your code here
   ```

---

## 📈 Performance Tuning

### Backend Optimization
- Adjust FastAPI worker processes in Dockerfile
- Enable response caching for repeated queries
- Tune connection pooling for Ollama

### Ollama Optimization
- Adjust `OLLAMA_KEEP_ALIVE` for memory management
- Use GPU acceleration (requires NVIDIA Docker)
- Increase context window for longer conversations

### Frontend Optimization
- Enable Gzip compression in nginx
- Cache static assets
- Implement lazy loading for components

---

## 🐛 Troubleshooting

### Services Won't Start
```bash
# Check logs
docker-compose logs -f

# Rebuild services
docker-compose build --no-cache

# Check network
docker network ls
```

### GPU Not Working
```bash
# Verify NVIDIA Docker runtime
docker run --rm --gpus all nvidia/cuda:11.8.0-base-ubuntu22.04 nvidia-smi

# Check Ollama GPU status
curl http://localhost:11434/api/generate -X POST -H "Content-Type: application/json" \
  -d '{"model": "qwen2.5:7b", "prompt": "Hi"}'
```

### High Memory Usage
```bash
# Check container resource usage
docker stats

# Reduce Ollama memory
export OLLAMA_NUM_PARALLEL=1
```

### Backend Connection Issues
```bash
# Test Ollama connectivity
docker-compose exec backend curl http://ollama:11434

# Check frontend connectivity
curl -i -X OPTIONS http://localhost:8000/chat \
  -H "Access-Control-Request-Method: POST"
```

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

### Code Style
- Python: Follow PEP 8
- JavaScript: Use Prettier configuration
- Commit messages: Use conventional commits

---

## 📜 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 📞 Support & Questions

- **Issues:** GitHub Issues
- **Discussions:** GitHub Discussions
- **Documentation:** See `/docs` folder

---

## 🎓 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [OpenTelemetry Getting Started](https://opentelemetry.io/docs/getting-started/)
- [Ollama Documentation](https://ollama.ai/)
- [Docker Documentation](https://docs.docker.com/)
- [Prometheus Monitoring](https://prometheus.io/docs/)

---

## 📝 Changelog

### Version 1.0.0
- Initial release
- Full-stack AI chat application
- Integrated observability
- Security scanning capabilities

---

**Last Updated:** May 2026  
**Version:** 1.0.0  
**Maintainer:** AI-App Team

