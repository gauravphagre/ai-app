# AI Chat Application - Comprehensive Guide

## 📋 Table of Contents

1. [Executive Summary](#executive-summary)
2. [Architecture Overview](#architecture-overview)
3. [Technology Stack](#technology-stack)
4. [System Components](#system-components)
5. [Getting Started](#getting-started)
6. [API Endpoints](#api-endpoints)
7. [Configuration](#configuration)
8. [Observability](#observability)
9. [Security](#security)
10. [Deployment](#deployment)
11. [Troubleshooting](#troubleshooting)
12. [Future Enhancements](#future-enhancements)

---

## Executive Summary

This is a **production-grade, full-stack AI chat application** that demonstrates modern cloud-native development practices. It provides real-time conversational AI capabilities through a three-tier microservices architecture, combining a React frontend, FastAPI backend, and Ollama LLM inference engine.

**Key Features:**
- 🤖 AI-powered chat using Qwen2.5:7B language model
- ⚡ Real-time responses with streaming support
- 📊 Enterprise-grade observability (OpenTelemetry, Prometheus, Grafana)
- 🔒 Built-in security scanning with Trivy
- 📈 Load testing capabilities included
- 🐳 Fully containerized with Docker & Docker Compose
- 🖥️ GPU acceleration support (NVIDIA CUDA)

**Current Status:** ✅ Production-ready

---

## Architecture Overview

### High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER BROWSER                             │
│                    (Running React App)                          │
└─────────────────┬───────────────────────────────────────────────┘
                  │ HTTP/REST (CORS enabled)
                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                     FRONTEND SERVICE                            │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  React 18.2 SPA (Port 3000)                              │  │
│  │  ├─ ModernAIChatUI.jsx (Main component)                  │  │
│  │  ├─ Message history management                           │  │
│  │  ├─ Markdown rendering for AI responses                  │  │
│  │  ├─ Real-time UI updates                                 │  │
│  │  └─ Tailwind CSS styling                                 │  │
│  └──────────────────────────────────────────────────────────┘  │
│  Docker: node-based image, Port 3000                           │
└─────────────────┬───────────────────────────────────────────────┘
                  │ HTTP POST /chat
                  │ {"prompt": "user input"}
                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                     BACKEND SERVICE                             │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  FastAPI Server (Port 8000)                              │  │
│  │  ├─ main.py (App initialization)                         │  │
│  │  ├─ CORS Middleware (localhost:3000)                     │  │
│  │  ├─ routes/chat.py (Chat endpoint)                       │  │
│  │  ├─ services/ollama_client.py (LLM integration)          │  │
│  │  ├─ observability/telemetry.py (OpenTelemetry setup)     │  │
│  │  ├─ observability/metrics.py (Prometheus metrics)        │  │
│  │  └─ observability/logger.py (Structured logging)         │  │
│  │                                                           │  │
│  │  Endpoints:                                              │  │
│  │  ├─ GET  /              (Health check)                   │  │
│  │  ├─ POST /chat          (Main chat endpoint)             │  │
│  │  └─ GET  /metrics       (Prometheus metrics)             │  │
│  └──────────────────────────────────────────────────────────┘  │
│  Docker: Python-based image, Port 8000                         │
└─────────────────┬───────────────────────────────────────────────┘
                  │ HTTP POST /api/generate
                  │ (model, prompt, stream=false)
                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                   OLLAMA SERVICE                                │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Ollama LLM Inference (Port 11434)                        │  │
│  │  ├─ Model: Qwen2.5:7B (7-billion parameters)             │  │
│  │  ├─ GPU Acceleration (NVIDIA CUDA)                        │  │
│  │  ├─ Model Caching (/root/.ollama)                         │  │
│  │  └─ Response Generation                                   │  │
│  │                                                           │  │
│  │  Request Processing:                                      │  │
│  │  1. Receive prompt                                        │  │
│  │  2. Tokenize input                                        │  │
│  │  3. Forward pass through model                            │  │
│  │  4. Generate response tokens                              │  │
│  │  5. Return complete response                              │  │
│  └──────────────────────────────────────────────────────────┘  │
│  Docker: Ubuntu-based image with GPU support                   │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼ (Parallel Processing)
┌─────────────────────────────────────────────────────────────────┐
│              OBSERVABILITY & MONITORING STACK                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  OpenTelemetry Collector (Port 4318)                      │  │
│  │  ├─ Receives traces from backend                          │  │
│  │  ├─ Batches and processes traces                          │  │
│  │  └─ Exports to Jaeger/Tempo                               │  │
│  └──────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Prometheus (Port 9090)                                   │  │
│  │  ├─ Scrapes /metrics endpoint every 15s                   │  │
│  │  ├─ Stores time-series data                               │  │
│  │  └─ Provides query interface                              │  │
│  └──────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Grafana (Port 3001)                                      │  │
│  │  ├─ Connects to Prometheus datasource                      │  │
│  │  ├─ Visualizes metrics in dashboards                       │  │
│  │  └─ Alerts on anomalies                                    │  │
│  └──────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Tempo (Port 3100)                                        │  │
│  │  ├─ Stores distributed traces                             │  │
│  │  └─ Integrates with Grafana for trace visualization       │  │
│  └──────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Loki (Port 3100)                                         │  │
│  │  ├─ Log aggregation system                                │  │
│  │  └─ Integrates with Grafana for log search                │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼ (Security)
┌─────────────────────────────────────────────────────────────────┐
│              SECURITY & SCANNING STACK                          │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Trivy Scanner (Runs hourly)                              │  │
│  │  ├─ Scans container images                                │  │
│  │  ├─ Detects CVE vulnerabilities                           │  │
│  │  ├─ Generates JSON reports                                │  │
│  │  └─ Stores in security/trivy/reports/                     │  │
│  └──────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Security Exporter (Port 9110)                            │  │
│  │  ├─ Parses Trivy reports                                  │  │
│  │  ├─ Generates Prometheus metrics                          │  │
│  │  └─ Exposes vulnerability counts                          │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘

Network: Docker Network (ai-net) - enables service-to-service communication
```

### Request Flow (Step-by-Step)

```
1. User inputs message in React UI
   │
   ├─ Message stored in React state
   ├─ UI shows user message immediately
   └─ Sends HTTP POST /chat with {"prompt": "message"}
   
2. Request reaches FastAPI backend
   │
   ├─ CORS middleware validates origin
   ├─ Request logged: event="request_received"
   ├─ OpenTelemetry span created: "chat-request"
   └─ Span attributes set with prompt data
   
3. Backend calls Ollama LLM
   │
   ├─ Services/ollama_client.py makes HTTP POST
   ├─ Endpoint: http://ollama:11434/api/generate
   ├─ Payload: {"model": "qwen2.5:7b", "prompt": "...", "stream": false}
   └─ Awaits complete response
   
4. Ollama processes prompt
   │
   ├─ Loads Qwen2.5:7B model (if not already loaded)
   ├─ Tokenizes user prompt
   ├─ GPU computation (if available)
   ├─ Generates response tokens iteratively
   └─ Returns complete response as JSON
   
5. Backend enriches response
   │
   ├─ Calculates latency: time.time() - start_time
   ├─ Counts tokens in response
   ├─ Logs event: "response_sent" with metrics
   ├─ Exports telemetry span to OTEL Collector
   └─ Returns JSON: {"response": "...", "latency": 2.34, "tokens": 128}
   
6. Frontend receives response
   │
   ├─ JSON parsed successfully
   ├─ Assistant message added to history
   ├─ Response rendered as markdown
   ├─ Latency/token count displayed
   └─ Loading state cleared
   
7. Observability collection (background)
   │
   ├─ Metrics exported to Prometheus
   ├─ Traces stored in Tempo
   ├─ Structured logs sent to Loki
   ├─ Grafana dashboards updated
   └─ Alerts evaluated if configured
```

---

## Technology Stack

### Backend
| Component | Version | Purpose |
|-----------|---------|---------|
| FastAPI | 0.104+ | Async Python web framework |
| Uvicorn | 0.24+ | ASGI application server |
| Python | 3.11+ | Programming language |
| Requests | 2.31+ | HTTP client library |
| python-dotenv | 1.0+ | Environment variable management |

### Frontend
| Component | Version | Purpose |
|-----------|---------|---------|
| React | 18.2.0 | UI library |
| React DOM | 18.2.0 | React rendering |
| React Markdown | 10.1.0 | Markdown rendering |
| Tailwind CSS | 3.4.19 | Utility-first CSS framework |
| PostCSS | 8.5.14 | CSS transformation |
| Autoprefixer | 10.5.0 | CSS vendor prefixes |

### LLM & Inference
| Component | Version | Purpose |
|-----------|---------|---------|
| Ollama | Latest | LLM orchestration platform |
| Qwen2.5:7B | 7B | Language model (7-billion parameters) |
| NVIDIA CUDA | Latest | GPU acceleration |
| NVIDIA cuDNN | Latest | Deep learning primitives |

### Observability
| Component | Version | Purpose |
|-----------|---------|---------|
| OpenTelemetry SDK | 1.15+ | Tracing & metrics collection |
| OpenTelemetry API | 1.15+ | Instrumentation interface |
| OpenTelemetry Exporter OTLP | 1.15+ | Trace export protocol |
| OpenTelemetry Instrumentation FastAPI | 0.36+ | Auto-instrumentation |
| OpenTelemetry Instrumentation Requests | 0.36+ | HTTP client tracing |
| Prometheus Client | 0.18+ | Metrics exposure |
| Prometheus | 2.45+ | Metrics storage & query |
| Grafana | 10.0+ | Metrics visualization |
| Tempo | 2.1+ | Distributed trace storage |
| Loki | 2.8+ | Log aggregation |
| Jaeger | Latest | Trace backend (optional) |

### Security & Scanning
| Component | Version | Purpose |
|-----------|---------|---------|
| Trivy | Latest | Container vulnerability scanner |
| Docker | 24+ | Container runtime |
| Docker Compose | 2.20+ | Container orchestration |

### Development Tools
| Tool | Purpose |
|------|---------|
| Git | Version control |
| Docker | Containerization |
| Docker Compose | Multi-container orchestration |
| NVIDIA Docker | GPU support in containers |
| VS Code / JetBrains IDE | Code editing |
| Postman/curl | API testing |

---

## System Components

### 1. Frontend Service (React)

**Location:** `./frontend/`

**Purpose:** User-facing web application for chat interface

**Key Files:**
- `src/components/ModernAIChatUI.jsx` - Main chat component
- `src/App.js` - Root React component
- `public/index.html` - HTML entry point
- `tailwind.config.js` - Tailwind configuration

**Key Features:**
- Message history management
- Real-time UI updates
- Markdown rendering for AI responses with syntax highlighting
- Loading states and error handling
- Responsive design with Tailwind CSS
- CORS-enabled API calls to backend

**Environment:**
- **Port:** 3000
- **Build:** `npm install && npm run build`
- **Start:** `npm start` (development with hot reload)
- **Docker Build:** `docker build -t ai-frontend ./frontend`

**Dependencies Flow:**
```
ModernAIChatUI.jsx
├── Manages chat state (messages array)
├── Handles user input
├── Makes fetch POST to http://localhost:8000/chat
├── Parses JSON response
├── Renders messages with react-markdown
└── Displays latency/token metrics
```

### 2. Backend Service (FastAPI)

**Location:** `./backend/`

**Purpose:** REST API server handling business logic and LLM coordination

**Key Files:**
- `app/main.py` - FastAPI application entry point
- `app/routes/chat.py` - Chat endpoint handler
- `app/services/ollama_client.py` - Ollama integration
- `app/observability/telemetry.py` - OpenTelemetry setup
- `requirements.txt` - Python dependencies

**Key Endpoints:**

#### GET /
Health check endpoint for deployment verification
```
Request:  GET http://localhost:8000/
Response: {"status": "ok"}
Status:   200
```

#### POST /chat
Main chat endpoint - accepts user prompt and returns AI response
```
Request:  POST http://localhost:8000/chat
Body:     {"prompt": "What is machine learning?"}
Response: {
  "response": "Machine learning is a subset of AI...",
  "latency": 2.456,  // seconds
  "tokens": 128      // token count
}
Status:   200
```

Error Response (if Ollama unreachable):
```
Status:   500
Body:     {"detail": "Internal Server Error"}
```

#### GET /metrics
Prometheus-format metrics endpoint
```
Request:  GET http://localhost:8000/metrics
Response: 
# HELP request_latency_seconds Request latency in seconds
# TYPE request_latency_seconds histogram
request_latency_seconds_bucket{le="0.1"} 5
request_latency_seconds_bucket{le="0.5"} 12
...
Status:   200
Media Type: text/plain; version=0.0.4
```

**Architecture Components:**

**routes/chat.py:**
```python
POST /chat workflow:
1. Receive {"prompt": "user input"}
2. Start OpenTelemetry span "chat-request"
3. Log event "request_received" with prompt
4. Call ask_llm(prompt) to Ollama
5. Measure latency and token count
6. Log event "response_sent" with metrics
7. Return response JSON
```

**services/ollama_client.py:**
```python
ask_llm(prompt) function:
1. Constructs HTTP POST request to ollama:11434/api/generate
2. Payload: {"model": "qwen2.5:7b", "prompt": prompt, "stream": false}
3. Sends request via requests library
4. Parses JSON response
5. Extracts response field
6. Returns generated text
```

**observability/telemetry.py:**
```python
setup_telemetry(app) function:
1. Creates TracerProvider
2. Sets up OTLP exporter (otel-collector:4318)
3. Configures BatchSpanProcessor
4. Activates FastAPIInstrumentor for auto-tracing
5. Registers tracer globally
```

**Environment:**
- **Port:** 8000
- **Build:** `python -m pip install -r requirements.txt`
- **Start:** `uvicorn app.main:app --host 0.0.0.0 --port 8000`
- **Docker Build:** `docker build -t ai-backend ./backend`

### 3. Ollama Service (LLM Engine)

**Location:** `./ollama/`

**Purpose:** Language model inference and generation

**Key Files:**
- `Dockerfile` - Container definition
- `start.sh` - Startup script
- `./data/ollama/` - Model data and configuration

**Model Details:**
- **Model Name:** Qwen2.5:7B
- **Parameters:** 7 billion (7B)
- **Context Window:** 2048 tokens (default, configurable)
- **Size:** ~5GB (model weights)
- **Architecture:** Transformer-based language model
- **License:** Check Qwen model license

**API Endpoint:**
```
POST http://ollama:11434/api/generate

Request:
{
  "model": "qwen2.5:7b",
  "prompt": "Hello, how are you?",
  "stream": false
}

Response:
{
  "response": "I'm doing well, thank you for asking!",
  "model": "qwen2.5:7b",
  "created_at": "2024-05-17T10:30:00Z",
  "done": true,
  "total_duration": 2345000000,      // nanoseconds
  "load_duration": 123000000,
  "prompt_eval_count": 12,
  "prompt_eval_duration": 456000000,
  "eval_count": 15,
  "eval_duration": 1766000000
}
```

**Environment:**
- **Port:** 11434
- **GPU:** NVIDIA GPU with CUDA support (optional)
- **Model Cache:** `/root/.ollama` (Docker volume)
- **Startup:** Automatically loads model on container start

**Performance Characteristics:**
- **CPU Mode:** 1-3 seconds per response (7B model)
- **GPU Mode:** 0.5-1.5 seconds per response (NVIDIA GPU)
- **Memory (RAM):** 8GB+ recommended
- **GPU Memory:** 6GB+ recommended (for 7B model)

### 4. Observability Stack

**Location:** `./observability/`

**Components:**

#### OpenTelemetry Collector
- **Port:** 4318 (OTLP HTTP receiver)
- **Config:** `otel-collector.yml`
- **Purpose:** Receives and processes traces from backend
- **Function:** Batches traces, exports to Prometheus/Jaeger/Tempo

#### Prometheus
- **Port:** 9090
- **Config:** `prometheus.yml`
- **Purpose:** Time-series metrics database
- **Function:** Scrapes `/metrics` endpoint, stores data, provides query API
- **Retention:** Default 15 days

#### Grafana
- **Port:** 3001
- **Purpose:** Metrics and logs visualization
- **Function:** Connects to Prometheus/Tempo/Loki, creates dashboards
- **Dashboards Included:**
  - `ai_app_obs.json` - Application metrics
  - `ai_logs_dashboard.json` - Structured logs
  - `ai_observability_dashboard.json` - Comprehensive view
  - `ai_vulnerability_dashboard.json` - Security findings

#### Tempo
- **Port:** 3100
- **Purpose:** Distributed trace storage
- **Function:** Stores traces from OTEL Collector, provides trace search

#### Loki
- **Port:** 3100
- **Purpose:** Log aggregation
- **Function:** Aggregates structured logs, provides log search interface

### 5. Security Stack

**Location:** `./security/`

**Components:**

#### Trivy Scanner
- **Tool:** Aquasec Trivy
- **Purpose:** Container vulnerability scanning
- **Frequency:** Hourly (configurable via `scan.sh`)
- **Scans:**
  - ai-backend image
  - ai-frontend image
  - ai-ollama image
- **Output:** JSON reports in `security/trivy/reports/`

#### Security Exporter
- **Language:** Python
- **Port:** 9110
- **Purpose:** Converts Trivy reports to Prometheus metrics
- **Metrics Exposed:**
  - Vulnerability count by severity (CRITICAL, HIGH, MEDIUM, LOW)
  - Container-specific metrics
  - Trends over time

### 6. Load Testing

**Location:** `./load-test/`

**Purpose:** Performance testing and load validation

**Tool:** Node.js load testing script

**Configuration:**
- **Default Concurrent Users:** 100
- **Default Total Requests:** 1000
- **Prompt Variation:** Multiple prompts for realistic simulation

**Metrics Collected:**
- Throughput (requests/second)
- Response times (average, p50, p95, p99)
- Success rate (%)
- Error rate (%)
- Total duration

**Usage:**
```bash
docker-compose run load-tester
```

---

## Getting Started

### Prerequisites

Before running the application, ensure you have:

1. **Docker & Docker Compose**
   ```bash
   # Check installation
   docker --version       # >= 24.0
   docker-compose --version  # >= 2.20
   ```

2. **NVIDIA GPU Support (Optional but Recommended)**
   ```bash
   # For GPU acceleration
   nvidia-docker --version
   # If not installed:
   # Ubuntu: sudo apt-get install nvidia-docker2
   # OR use nvidia-docker runtime in docker-compose
   ```

3. **Available System Resources**
   - **RAM:** 16GB minimum (8GB for model + 8GB for services)
   - **Disk:** 50GB free (5GB for Ollama model + buffer)
   - **CPU:** 4 cores minimum (8+ cores recommended)
   - **GPU:** Optional but recommended for fast inference

### Installation Steps

#### Step 1: Clone Repository

```bash
git clone <repository-url>
cd ai-app
```

#### Step 2: Create Environment File

```bash
# Create .env file with default settings
cat > .env << EOF
DEBUG=True
LOG_LEVEL=INFO
OLLAMA_KEEP_ALIVE=-1
OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4318
OTEL_SERVICE_NAME=ai-backend
EOF
```

#### Step 3: Build Docker Images

```bash
# Build all services
docker-compose build

# Or build specific services
docker-compose build backend
docker-compose build frontend
docker-compose build ollama
```

#### Step 4: Start Services

```bash
# Start all services in background
docker-compose up -d

# Or start in foreground to see logs
docker-compose up

# Check service status
docker-compose ps
```

**Expected Output:**
```
NAME              IMAGE           STATUS            PORTS
ollama            ai-ollama       Up 2 minutes      11434/tcp
backend           ai-backend      Up 1 minute       8000/tcp
frontend          ai-frontend     Up 1 minute       3000/tcp
load-tester       load-test:latest  Exited
trivy             trivy:latest    Exited
security-exporter security:latest  Up 1 minute       9110/tcp
```

#### Step 5: Verify Installation

```bash
# Health check - backend
curl http://localhost:8000/

# Access frontend
open http://localhost:3000

# Check metrics
curl http://localhost:8000/metrics | head -20

# Test chat endpoint
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Hello, how are you?"}'
```

### Quick Test

```bash
# Test the complete flow
echo "Testing AI Chat Application..."

# 1. Check health
echo "1. Health Check:"
curl http://localhost:8000/

# 2. Send chat message
echo -e "\n2. Chat Request:"
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt":"What is AI?"}' | jq .

# 3. Access frontend
echo -e "\n3. Frontend URL: http://localhost:3000"

# 4. Check metrics
echo "4. Prometheus Metrics: http://localhost:8000/metrics"

# 5. View Grafana dashboards
echo "5. Grafana: http://localhost:3001"
```

---

## API Endpoints

### Health & Status

#### GET /
Health check endpoint
```bash
curl http://localhost:8000/

# Response (200 OK)
{"status": "ok"}
```

### Chat API

#### POST /chat
Main chat endpoint

**Request:**
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "What is machine learning?"
  }'
```

**Response (200 OK):**
```json
{
  "response": "Machine learning is a subset of artificial intelligence that focuses on enabling systems to learn and improve from experience without being explicitly programmed...",
  "latency": 2.456,
  "tokens": 128
}
```

**Error Response (500 Internal Server Error):**
```json
{
  "detail": "Internal Server Error - Ollama service unreachable"
}
```

**Request Parameters:**
- `prompt` (string, required): The user's input message

**Response Fields:**
- `response` (string): The AI-generated response
- `latency` (float): Time taken to generate response (seconds)
- `tokens` (integer): Number of tokens in the response

**Example Use Cases:**

1. Simple Question
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt":"How to learn Python?"}'
```

2. Multi-turn Context (managed by frontend)
```bash
# First turn
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt":"I want to learn web development"}'

# Second turn (frontend includes context)
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt":"What frameworks should I use?"}'
```

3. Code Generation
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Write a Python function to calculate fibonacci numbers"}'
```

### Metrics & Observability

#### GET /metrics
Prometheus-format metrics endpoint

```bash
curl http://localhost:8000/metrics

# Response (200 OK, text/plain)
# HELP request_latency_seconds Request latency in seconds
# TYPE request_latency_seconds histogram
request_latency_seconds_bucket{le="0.1"} 0
request_latency_seconds_bucket{le="0.5"} 2
request_latency_seconds_bucket{le="1.0"} 5
request_latency_seconds_bucket{le="2.5"} 12
request_latency_seconds_bucket{le="5.0"} 15
request_latency_seconds_bucket{le="+Inf"} 20
request_latency_seconds_sum 45.23
request_latency_seconds_count 20
...
```

**Key Metrics Exposed:**
- `request_latency_seconds` - Response time histogram
- `request_tokens_total` - Token count counter
- `http_requests_total` - HTTP request counter
- `vulnerability_count` - Security vulnerabilities count

---

## Configuration

### Environment Variables (.env)

**File Location:** `.env` (root directory)

**Default Configuration:**
```bash
DEBUG=True
LOG_LEVEL=INFO
OLLAMA_KEEP_ALIVE=-1
OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4318
OTEL_SERVICE_NAME=ai-backend
```

**Configuration Options:**

| Variable | Default | Options | Purpose |
|----------|---------|---------|---------|
| DEBUG | True | True/False | Enable debug logging |
| LOG_LEVEL | INFO | DEBUG, INFO, WARNING, ERROR, CRITICAL | Logging verbosity |
| OLLAMA_KEEP_ALIVE | -1 | -1 (forever) or seconds | Keep model loaded |
| OTEL_EXPORTER_OTLP_ENDPOINT | http://otel-collector:4318 | Any OTLP endpoint | Trace export URL |
| OTEL_SERVICE_NAME | ai-backend | Any string | Service identifier |

### Production Configuration

For production deployment, modify `.env`:

```bash
DEBUG=False
LOG_LEVEL=WARN
OLLAMA_KEEP_ALIVE=300  # Unload model after 5 minutes of inactivity
OTEL_EXPORTER_OTLP_ENDPOINT=http://production-collector:4318
OTEL_SERVICE_NAME=ai-backend-prod
```

### Docker Compose Configuration

**File Location:** `docker-compose.yml`

**Key Sections:**

1. **Service Definitions:**
   - ollama - LLM service
   - backend - FastAPI service
   - frontend - React service
   - trivy - Security scanner
   - security-exporter - Metrics exporter
   - load-tester - Load testing

2. **Network Configuration:**
   ```yaml
   networks:
     ai-net:
       driver: bridge
   ```

3. **Volume Mapping:**
   ```yaml
   volumes:
     - ./data/ollama:/root/.ollama  # Model persistence
   ```

4. **Environment File:**
   ```yaml
   env_file:
     - .env  # Loaded into backend service
   ```

### Service Dependencies

```
frontend
  └── depends_on: backend

backend
  └── depends_on: ollama

load-tester
  └── depends_on: backend

trivy
  └── no dependencies (runs independently)

security-exporter
  └── no dependencies (runs independently)
```

---

## Observability

### OpenTelemetry Tracing

**Setup Location:** `backend/app/observability/telemetry.py`

**Instrumentation:**
1. **Auto-instrumentation** (automatic span creation for all HTTP requests)
   - All FastAPI routes automatically traced
   - Request duration recorded
   - Status codes tracked

2. **Manual Instrumentation** (explicit span creation for specific operations)
   ```python
   with tracer.start_as_current_span("chat-request"):
       # Custom code execution
       response = ask_llm(prompt)
   ```

**Trace Attributes:**
- `http.method` - HTTP method (GET, POST, etc.)
- `http.url` - Request URL
- `http.status_code` - Response status
- `http.request.body.size` - Request body size
- `http.response.body.size` - Response body size

**Trace Export:**
- **Exporter:** OpenTelemetry Protocol (OTLP)
- **Collector:** otel-collector:4318
- **Protocol:** HTTP/protobuf
- **Batching:** BatchSpanProcessor (efficient)

### Prometheus Metrics

**Metrics Types:**

1. **Histogram Metrics (for latency)**
   ```
   request_latency_seconds
   - Buckets: 0.1s, 0.5s, 1s, 2.5s, 5s, +Inf
   - Provides: min, max, avg, sum, count, quantiles
   ```

2. **Counter Metrics (for counts)**
   ```
   request_tokens_total
   - Monotonically increasing
   - Useful for: total tokens generated, request count
   ```

3. **Gauge Metrics (for current values)**
   ```
   active_connections
   - Can increase or decrease
   - Useful for: current active users, memory usage
   ```

**Querying Metrics:**

```promql
# Request rate (requests per second)
rate(request_count_total[5m])

# P95 latency
histogram_quantile(0.95, rate(request_latency_seconds_bucket[5m]))

# Error rate
rate(request_errors_total[5m])

# Total tokens generated
increase(request_tokens_total[1h])
```

### Grafana Dashboards

**Default Dashboards:**

1. **ai_app_obs.json** - Application Metrics
   - Request volume graph
   - Latency distribution
   - Error rate gauge
   - Token usage metrics
   - Service health status

2. **ai_logs_dashboard.json** - Structured Logs
   - Log search interface
   - Event filtering by type
   - Request/response logs
   - Error tracking

3. **ai_observability_dashboard.json** - Comprehensive View
   - Trace visualization
   - Span analysis
   - Service dependency mapping
   - Performance analysis

4. **ai_vulnerability_dashboard.json** - Security
   - Vulnerability count by severity
   - Container breakdown
   - Trend analysis
   - Remediation status

### Distributed Tracing (Tempo)

**Trace Storage:** `observability/tempo.yaml`

**Trace Visualization:**
1. Traces flow through OTEL Collector
2. Stored in Tempo backend
3. Queried through Grafana UI
4. Visualize service dependencies
5. Identify performance bottlenecks

**Example Trace Flow:**
```
User Request
  ├─ Span: HTTP GET /chat
  │  ├─ Span: FastAPI middleware
  │  ├─ Span: chat-request (custom)
  │  ├─ Span: HTTP POST to Ollama
  │  │  └─ Span: Request body serialization
  │  └─ Span: Response serialization
  └─ Event: trace-recorded [timestamp, duration]
```

### Log Aggregation (Loki)

**Structured Logging:** `backend/app/observability/logger.py`

**Log Structure:**
```json
{
  "timestamp": "2024-05-17T10:30:00Z",
  "level": "INFO",
  "service": "ai-backend",
  "event": "request_received",
  "prompt": "What is AI?",
  "trace_id": "abc123def456",
  "span_id": "xyz789"
}
```

**Log Events:**
- `request_received` - When user request arrives
- `response_sent` - When response is sent to user
- `error_occurred` - When exception is raised
- `model_loaded` - When LLM model is loaded

**Querying Logs in Grafana:**
```logql
{job="ai-backend"} | json | event="request_received"
{job="ai-backend"} | json | level="ERROR"
```

---

## Security

### Vulnerability Scanning

**Trivy Scanner Setup:**

1. **Automatic Scanning**
   - Runs every hour (configurable)
   - Scans all container images:
     - ai-backend
     - ai-frontend
     - ai-ollama

2. **Scan Process:**
   ```bash
   ./security/scan.sh
   # Executes:
   # 1. trivy image ai-backend > backend.json
   # 2. trivy image ai-frontend > frontend.json
   # 3. trivy image ai-ollama > ollama.json
   ```

3. **Report Generation:**
   - Location: `security/trivy/reports/`
   - Format: JSON
   - Contains:
     - CVE identifiers
     - Severity levels
     - Affected packages
     - Remediation advice

### CVE Reporting

**Report Structure:**
```json
{
  "SchemaVersion": 2,
  "ArtifactName": "ai-backend",
  "Results": [
    {
      "Type": "library",
      "Class": "pip-requirement",
      "Misconfigurations": [],
      "Vulnerabilities": [
        {
          "VulnerabilityID": "CVE-2024-1234",
          "PkgName": "requests",
          "PkgVersion": "2.28.0",
          "Severity": "HIGH",
          "Title": "Vulnerability in requests library",
          "Description": "...",
          "FixedVersion": "2.31.0",
          "References": ["https://..."]
        }
      ]
    }
  ]
}
```

### Security Best Practices

#### 1. CORS Configuration
```python
CORSMiddleware(
    allow_origins=["http://localhost:3000"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**Production Recommendation:**
```python
allow_origins=["https://yourdomain.com"],  # Specific production domain
```

#### 2. Environment Variables
- Never commit `.env` file to version control
- Use `.gitignore` to exclude sensitive files
- For production: use secret management (AWS Secrets Manager, Kubernetes Secrets)

#### 3. Container Security
- Run with minimal privileges
- Use read-only filesystems where possible
- Regularly update base images
- Implement resource limits

#### 4. API Security
- Enable HTTPS/TLS in production
- Implement authentication (JWT, OAuth2)
- Add rate limiting
- Validate all inputs

#### 5. Data Security
- Encrypt sensitive data at rest
- Encrypt data in transit (TLS)
- Implement audit logging
- Regular backups

### Security Scan Results

**Example Scan Output:**
```
Backend Image Vulnerabilities:
- CRITICAL: 0 issues
- HIGH: 2 issues (requests@2.28.0, urllib3@1.26.5)
- MEDIUM: 5 issues
- LOW: 12 issues
- UNKNOWN: 3 issues

Recommended Actions:
1. Update requests to 2.31.0 or later
2. Update urllib3 to 2.0.0 or later
3. Review remaining MEDIUM severity issues
```

---

## Deployment

### Local Development

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Restart specific service
docker-compose restart backend
```

### Production Deployment

#### Pre-Deployment Checklist

- [ ] Update CORS origins to production domain
- [ ] Set `DEBUG=False` in .env
- [ ] Set `LOG_LEVEL=WARN` in .env
- [ ] Configure production database (if needed)
- [ ] Set up secret management
- [ ] Enable HTTPS/TLS certificates
- [ ] Configure CDN for frontend assets
- [ ] Set up monitoring and alerting
- [ ] Implement authentication/authorization
- [ ] Configure auto-scaling policies
- [ ] Set up backup strategies
- [ ] Run security audit
- [ ] Load test at expected traffic levels

#### Docker Compose Configuration for Production

```yaml
services:
  backend:
    # ... existing config ...
    environment:
      - DEBUG=False
      - LOG_LEVEL=WARN
      - ENVIRONMENT=production
    restart: always
    deploy:
      resources:
        limits:
          memory: 4G
          cpus: 2
```

#### Kubernetes Deployment

**Example Deployment Resource:**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ai-backend
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ai-backend
  template:
    metadata:
      labels:
        app: ai-backend
    spec:
      containers:
      - name: backend
        image: ai-backend:latest
        ports:
        - containerPort: 8000
        env:
        - name: DEBUG
          value: "False"
        - name: LOG_LEVEL
          value: "WARN"
        resources:
          requests:
            memory: "2Gi"
            cpu: "1"
          limits:
            memory: "4Gi"
            cpu: "2"
        livenessProbe:
          httpGet:
            path: /
            port: 8000
          initialDelaySeconds: 10
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
```

#### Cloud Deployment Options

1. **AWS ECS**
   ```bash
   # Push images to ECR
   docker tag ai-backend:latest <account>.dkr.ecr.us-east-1.amazonaws.com/ai-backend:latest
   docker push <account>.dkr.ecr.us-east-1.amazonaws.com/ai-backend:latest
   
   # Create ECS service with task definition
   ```

2. **Google Cloud Run**
   ```bash
   # Build and push to Artifact Registry
   gcloud builds submit --tag gcr.io/PROJECT_ID/ai-backend
   
   # Deploy
   gcloud run deploy ai-backend --image gcr.io/PROJECT_ID/ai-backend
   ```

3. **Azure Container Instances**
   ```bash
   # Push to Azure Container Registry
   az acr build --registry <registry-name> --image ai-backend .
   
   # Deploy
   az container create --resource-group mygroup \
     --name ai-backend --image <registry>.azurecr.io/ai-backend
   ```

---

## Troubleshooting

### Common Issues

#### 1. Frontend Cannot Connect to Backend

**Symptom:** Browser console shows CORS error

**Solution:**
```bash
# Check CORS configuration in backend/app/main.py
# Verify backend is running
docker-compose ps

# Check backend logs
docker-compose logs backend

# Verify connectivity
curl http://localhost:8000/

# Update CORS if needed:
# allow_origins=["http://localhost:3000"]  # for local dev
# allow_origins=["https://yourdomain.com"]  # for production
```

#### 2. Ollama Model Not Loading

**Symptom:** Backend returns error calling Ollama

**Solution:**
```bash
# Check Ollama service status
docker-compose logs ollama

# Verify Ollama is running
curl http://localhost:11434/

# Check if model exists
docker-compose exec ollama ollama list

# Manually pull model if needed
docker-compose exec ollama ollama pull qwen2.5:7b

# Check disk space
docker system df

# Increase timeout if model is loading
# In docker-compose.yml, add:
# environment:
#   - OLLAMA_LOAD_TIMEOUT=600
```

#### 3. Out of Memory Error

**Symptom:** Container OOM killed (exit code 137)

**Solution:**
```bash
# Check current memory usage
docker stats

# Increase Docker memory limit (varies by platform)
# Docker Desktop: Settings > Resources > Memory

# Reduce Ollama model size (use smaller model)
# Or implement response caching

# Increase server RAM
# Upgrade host machine if on cloud
```

#### 4. No Metrics in Grafana

**Symptom:** Prometheus has no data

**Solution:**
```bash
# Check if backend /metrics endpoint is working
curl http://localhost:8000/metrics

# Verify Prometheus is scraping
docker-compose logs prometheus

# Check Prometheus targets
curl http://localhost:9090/api/v1/targets

# Verify service name matches config
# Check prometheus.yml scrape_configs

# Restart Prometheus
docker-compose restart prometheus
```

#### 5. Traces Not Appearing in Grafana

**Symptom:** Grafana Tempo shows no traces

**Solution:**
```bash
# Verify OpenTelemetry is initialized
# Check backend startup logs
docker-compose logs backend

# Ensure OTEL_EXPORTER_OTLP_ENDPOINT is correct
# Should point to: http://otel-collector:4318

# Test OTEL Collector connectivity
docker-compose exec backend curl http://otel-collector:4318/

# Restart OTEL Collector
docker-compose restart otel-collector

# Generate trace by making chat request
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt":"test"}'
```

#### 6. Load Test Hangs or Fails

**Symptom:** Load test doesn't complete or has errors

**Solution:**
```bash
# Check backend responsiveness
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt":"test"}'

# Check resource constraints
docker stats

# Reduce concurrent users in load-test.js
# Or increase server resources

# Check load-test container logs
docker-compose logs load-tester
```

### Debug Mode

**Enable Debug Logging:**
```bash
# Update .env
DEBUG=True
LOG_LEVEL=DEBUG

# Restart services
docker-compose restart backend

# View detailed logs
docker-compose logs -f backend
```

**Collect Diagnostics:**
```bash
# Generate diagnostics report
{
  # 1. Service status
  echo "=== Service Status ===" 
  docker-compose ps
  
  # 2. Resource usage
  echo -e "\n=== Resource Usage ==="
  docker stats --no-stream
  
  # 3. Network connectivity
  echo -e "\n=== Network Connectivity ==="
  docker-compose exec backend curl http://ollama:11434/
  
  # 4. Recent logs
  echo -e "\n=== Recent Backend Logs ==="
  docker-compose logs --tail=50 backend
  
  # 5. Metrics
  echo -e "\n=== Metrics Endpoint ==="
  curl http://localhost:8000/metrics | head -30
} > diagnostics.txt

# Share diagnostics.txt for support
```

### Performance Optimization

**If responses are slow:**

1. **Check GPU Utilization**
   ```bash
   # On host machine
   nvidia-smi
   
   # Watch in real-time
   watch nvidia-smi
   ```

2. **Optimize Model Loading**
   ```bash
   # Set keep-alive to longer period
   OLLAMA_KEEP_ALIVE=3600  # 1 hour
   ```

3. **Enable Response Caching**
   - Implement Redis cache layer
   - Cache identical prompts

4. **Increase Resources**
   ```bash
   # docker-compose.yml
   deploy:
     resources:
       limits:
         memory: 8G
         cpus: 4
   ```

---

## Future Enhancements

### Short-term (1-3 months)

1. **Chat History Persistence**
   - Add PostgreSQL/MongoDB
   - Store conversations per user
   - Implement pagination

2. **User Authentication**
   - JWT-based auth
   - User profiles
   - Session management

3. **Streaming Responses**
   - Server-sent events (SSE)
   - Real-time response streaming
   - Progressive UI updates

4. **Rate Limiting**
   - Per-user limits
   - Configurable thresholds
   - Rate limit headers

5. **Response Caching**
   - Redis implementation
   - Cache similar prompts
   - TTL configuration

### Medium-term (3-6 months)

1. **Multi-Model Support**
   - Model selection UI
   - Load different models
   - Model comparison

2. **Advanced Observability**
   - Custom dashboards
   - Anomaly detection
   - Predictive alerts

3. **Batch Processing**
   - Process multiple prompts
   - Async job queue
   - Results storage

4. **Voice Interface**
   - Speech-to-text
   - Text-to-speech
   - Voice chat UI

5. **Export Capabilities**
   - PDF export
   - Markdown export
   - Chat history download

### Long-term (6-12 months)

1. **Advanced AI Features**
   - Fine-tuning on custom data
   - Model ensembles
   - Retrieval-augmented generation (RAG)

2. **Enterprise Features**
   - SAML/OAuth integration
   - Role-based access control
   - Audit logging

3. **Integration Ecosystem**
   - Slack integration
   - Microsoft Teams integration
   - Webhook support
   - REST API marketplace

4. **Scalability**
   - Horizontal scaling
   - Load balancing
   - Database sharding
   - Distributed inference

5. **Advanced Analytics**
   - User engagement metrics
   - Query analytics
   - Response quality scores
   - Cost attribution

### Research & Innovation

1. **Experiment with New Models**
   - Evaluate emerging models
   - Benchmark performance
   - Cost-benefit analysis

2. **Safety & Ethics**
   - Content filtering
   - Bias detection
   - Jailbreak prevention
   - Responsible AI practices

3. **Performance Research**
   - Model quantization
   - Distillation
   - Prompt optimization
   - Inference acceleration

---

## Contributing

### Code Style

- Python: PEP 8
- JavaScript: Prettier
- YAML: 2-space indentation

### Testing

```bash
# Run backend tests
docker-compose exec backend pytest

# Run frontend tests
docker-compose exec frontend npm test

# Run integration tests
./test-integration.sh
```

### Commit Guidelines

```
Format: [Type] Brief description

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation
- test: Test files
- refactor: Code refactoring
- perf: Performance improvement
- chore: Build/dependencies

Example:
feat: Add streaming responses to chat endpoint
fix: Resolve CORS issue with frontend
docs: Update deployment guide
```

---

## Support & Resources

### Documentation
- [API Documentation](./API.md)
- [Deployment Guide](./DEPLOYMENT.md)
- [Architecture Deep Dive](./ARCHITECTURE.md)

### Community
- GitHub Issues: Report bugs and request features
- Discussions: Ask questions and share ideas

### External Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Ollama Documentation](https://github.com/ollama/ollama)
- [OpenTelemetry Docs](https://opentelemetry.io/docs/)
- [Prometheus Docs](https://prometheus.io/docs/)
- [Grafana Docs](https://grafana.com/docs/)

---

## License

This project is licensed under the [MIT License](./LICENSE)

---

## Changelog

### Version 1.0.0 (Current)
- ✅ Full-stack AI chat application
- ✅ OpenTelemetry integration
- ✅ Prometheus metrics
- ✅ Grafana dashboards
- ✅ Trivy security scanning
- ✅ Load testing included
- ✅ Docker containerization

### Planned Versions
- v1.1.0: Chat history persistence
- v1.2.0: User authentication
- v1.3.0: Streaming responses
- v2.0.0: Multi-model support

---

## FAQ

**Q: Does this work without a GPU?**
A: Yes, but it will be slower (1-3 seconds per response vs 0.5-1.5 seconds with GPU)

**Q: Can I use a different LLM model?**
A: Yes, modify the model in the Ollama service and update references in the code

**Q: How much disk space is needed?**
A: Approximately 5GB for the Qwen2.5:7B model + 10GB for system, so 15GB minimum

**Q: Is this suitable for production?**
A: Yes, with proper configuration for your environment and security hardening

**Q: How do I scale this for multiple users?**
A: Use Kubernetes with horizontal pod autoscaling or load balancing on cloud platforms

---

## Contact & Questions

For questions or support:
- GitHub Issues: [Report an issue](https://github.com/yourusername/ai-app/issues)
- Email: support@yourdomain.com
- Documentation: [Full docs](./DOCS.md)

---

**Last Updated:** May 17, 2024
**Version:** 1.0.0
**Status:** Production-Ready ✅


