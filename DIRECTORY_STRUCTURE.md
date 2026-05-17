# AI Chat Application - Complete Directory Structure

```
ai-app/
├── .env                                    # Environment variables for configuration
├── .git/                                   # Git repository metadata
├── .gitignore                              # Git ignore rules
├── .idea/                                  # IntelliJ IDEA IDE configuration
│   ├── .gitignore
│   ├── ai-app.iml
│   ├── copilot.data.migration.ask2agent.xml
│   ├── dictionaries/
│   │   └── project.xml                     # Project-specific dictionary
│   ├── inspectionProfiles/
│   │   └── profiles_settings.xml
│   ├── misc.xml
│   ├── modules.xml
│   ├── vcs.xml
│   └── workspace.xml
├── CODEBASE_SUMMARY.md                     # Comprehensive codebase overview (100+ lines)
├── DIRECTORY_STRUCTURE.md                  # This file - complete directory mapping
├── README.md                               # Project documentation and setup guide
│
├── backend/                                # FastAPI backend service
│   ├── Dockerfile                          # Docker configuration for backend
│   ├── requirements.txt                    # Python dependencies
│   └── app/
│       ├── __init__.py                     # Package initialization
│       ├── main.py                         # FastAPI application entry point
│       │   ├── FastAPI app initialization
│       │   ├── CORS middleware configuration
│       │   ├── Lifespan context manager (startup/shutdown)
│       │   ├── Health check endpoint (GET /)
│       │   └── Metrics endpoint (GET /metrics)
│       │
│       ├── observability/                  # Telemetry and monitoring
│       │   ├── __init__.py
│       │   ├── logger.py                   # Structured logging utilities
│       │   │   └── log_event() - logs key-value pairs for observability
│       │   ├── metrics.py                  # Prometheus metrics collection
│       │   │   ├── request_latency_seconds histogram
│       │   │   ├── request_tokens_total counter
│       │   │   └── count_tokens() - token counting function
│       │   ├── otel.py                     # OpenTelemetry tracer setup
│       │   │   └── tracer - global tracer instance
│       │   └── telemetry.py                # Telemetry initialization
│       │       ├── setup_telemetry() - initializes OTEL
│       │       ├── TracerProvider setup
│       │       ├── OTLPSpanExporter configuration
│       │       └── FastAPIInstrumentor activation
│       │
│       ├── routes/                         # API endpoint handlers
│       │   └── chat.py                     # Chat endpoint implementation
│       │       └── POST /chat
│       │           ├── Accepts: {"prompt": "user_message"}
│       │           ├── Returns: {"response": "text", "latency": 1.23, "tokens": 45}
│       │           ├── OpenTelemetry span creation
│       │           ├── Event logging (request_received, response_sent)
│       │           └── Latency and token tracking
│       │
│       └── services/                       # Business logic and integrations
│           ├── __init__.py
│           └── ollama_client.py            # Ollama LLM integration
│               ├── ask_llm(prompt) - calls Ollama API
│               ├── HTTP POST to ollama:11434/api/generate
│               ├── Model: qwen2.5:7b
│               └── Response parsing and return
│
├── frontend/                               # React frontend application
│   ├── Dockerfile                          # Docker configuration for frontend
│   ├── package.json                        # NPM dependencies and scripts
│   │   ├── React 18.2.0
│   │   ├── react-dom 18.2.0
│   │   ├── react-markdown 10.1.0
│   │   ├── react-scripts 5.0.1
│   │   ├── remark-gfm 4.0.1
│   │   ├── tailwindcss 3.4.19
│   │   ├── autoprefixer 10.5.0
│   │   └── postcss 8.5.14
│   ├── package-lock.json                   # Dependency lock file
│   ├── postcss.config.js                   # PostCSS configuration
│   ├── tailwind.config.js                  # Tailwind CSS configuration
│   ├── public/
│   │   └── index.html                      # HTML entry point
│   ├── src/
│   │   ├── index.js                        # React app entry point
│   │   ├── index.css                       # Global styles
│   │   ├── App.js                          # Root component
│   │   ├── App.css                         # App component styles
│   │   └── components/
│   │       └── ModernAIChatUI.jsx          # Main chat UI component
│   │           ├── Message display
│   │           ├── Input field for prompts
│   │           ├── Send button
│   │           ├── Markdown rendering for responses
│   │           ├── Loading state management
│   │           ├── Message history state
│   │           └── HTTP POST fetch to /chat endpoint
│   └── node_modules/                       # NPM dependencies (auto-generated)
│       └── [hundreds of package folders]
│
├── data/                                   # Application data persistence
│   └── ollama/                             # Ollama model data
│       ├── config.json                     # Ollama configuration
│       ├── history                         # Interaction history
│       ├── id_ed25519                      # SSH private key
│       ├── id_ed25519.pub                  # SSH public key
│       ├── backup/
│       │   └── config.json.1778256119      # Configuration backup with timestamp
│       ├── cache/
│       │   └── model-recommendations.json  # Cached model recommendations
│       └── models/
│           ├── blobs/
│           │   ├── sha256-2bada8a7450677000f678be90653b85d364de7db25eb5ea54136ada5f3933730
│           │   ├── sha256-2f15b3218f0552c60647ce60ada83632d2c09755b16259b13e3e4458e9ae419d
│           │   ├── sha256-66b9ea09bd5b7099cbb4fc820f31b575c0366fa439b08245566692c6784e281e
│           │   ├── sha256-832dd9e00a68dd83b3c3fb9f5588dad7dcf337a0db50f7d9483f310cd292e92e
│           │   └── sha256-eb4402837c7829a690fa845de4d7f3fd842c2adee476d5341da8a46ea9255175
│           │       └── Model weight blobs (SHA256 hashed)
│           │
│           └── manifests/
│               └── registry.ollama.ai/
│                   └── library/
│                       └── qwen2.5/
│                           └── 7b                # Qwen2.5:7B model manifest
│
├── load-test/                              # Load testing service
│   ├── Dockerfile                          # Docker configuration for load tests
│   └── load-test.js                        # Load test script
│       ├── Concurrent user simulation (default 100)
│       ├── Total request count (default 1000)
│       ├── Varied prompt generation
│       ├── Metrics collection:
│       │   ├── Throughput (requests/second)
│       │   ├── Response times (avg, p95, p99)
│       │   ├── Success rate
│       │   └── Error rate
│       └── Results reporting
│
├── observability/                          # Observability and monitoring stack
│   ├── docker-compose.yml                  # Observability services composition
│   │   ├── otel-collector service
│   │   ├── prometheus service
│   │   ├── grafana service
│   │   ├── tempo service (trace storage)
│   │   └── loki service (log aggregation)
│   ├── otel-collector.yml                  # OpenTelemetry Collector configuration
│   │   ├── Receiver: OTLP (port 4318)
│   │   ├── Processor: Batch
│   │   └── Exporter: Prometheus, Jaeger
│   ├── prometheus.yml                      # Prometheus scrape configuration
│   │   ├── Global settings
│   │   ├── Scrape configs:
│   │   │   ├── Backend metrics (port 8000)
│   │   │   ├── Security exporter (port 9110)
│   │   │   └── Collector metrics
│   │   └── Alert rules
│   ├── tempo.yaml                          # Tempo trace storage configuration
│   │   ├── Trace ingestion settings
│   │   ├── Storage backend
│   │   └── Query configuration
│   └── dashboards/                         # Grafana dashboards
│       ├── ai_app_obs.json                 # Application observability dashboard
│       │   ├── Request rate graph
│       │   ├── Latency histogram
│       │   ├── Error rate gauge
│       │   ├── Token count metrics
│       │   └── Service health status
│       ├── ai_logs_dashboard.json          # Structured logs dashboard
│       │   ├── Log search interface
│       │   ├── Event filtering
│       │   ├── Request/response logs
│       │   └── Error tracking
│       ├── ai_observability_dashboard.json # Comprehensive observability
│       │   ├── Traces visualization
│       │   ├── Span analysis
│       │   ├── Dependency mapping
│       │   └── Performance analysis
│       └── ai_vulnerability_dashboard.json # Security vulnerabilities
│           ├── Vulnerability count by severity
│           ├── Container vulnerability breakdown
│           ├── Trending vulnerabilities
│           └── Remediation tracking
│
├── ollama/                                 # Ollama LLM service configuration
│   ├── Dockerfile                          # Docker configuration for Ollama
│   │   ├── Base image: ollama (official)
│   │   ├── GPU support via NVIDIA base
│   │   └── Model preloading
│   └── start.sh                            # Startup script
│       ├── Ollama service initialization
│       ├── Model loading (qwen2.5:7b)
│       ├── Port binding (11434)
│       └── Shutdown handling
│
├── security/                               # Security scanning and compliance
│   ├── Dockerfile                          # Docker configuration for security exporter
│   ├── scan.sh                             # Trivy vulnerability scanning script
│   │   ├── Continuous scanning loop
│   │   ├── Container image scanning
│   │   │   ├── ai-backend scan
│   │   │   ├── ai-frontend scan
│   │   │   └── ai-ollama scan
│   │   ├── Report generation (JSON)
│   │   ├── Report storage to trivy/reports/
│   │   └── Scheduling (hourly)
│   ├── trivy_metrics.py                    # Trivy to Prometheus metrics exporter
│   │   ├── JSON report parsing
│   │   ├── Vulnerability counting
│   │   ├── Metrics generation:
│   │   │   ├── Vulnerability count by severity
│   │   │   ├── Container-specific metrics
│   │   │   └── Trends over time
│   │   └── Prometheus endpoint (port 9110)
│   ├── trivy/
│   │   ├── metrics/                        # Prometheus metrics output
│   │   │   └── [Auto-generated metrics files]
│   │   └── reports/                        # Vulnerability scan reports
│   │       ├── backend.json                # Backend image scan results
│   │       │   ├── Image layers scanned
│   │       │   ├── CRITICAL vulnerabilities
│   │       │   ├── HIGH vulnerabilities
│   │       │   ├── MEDIUM vulnerabilities
│   │       │   ├── LOW vulnerabilities
│   │       │   └── Remediation recommendations
│   │       ├── frontend.json               # Frontend image scan results
│   │       │   └── [Same structure as backend]
│   │       └── ollama.json                 # Ollama image scan results
│   │           └── [Same structure as backend]
│   └── trivy/
│       └── [Additional Trivy configuration]
│
└── docker-compose.yml                      # Main orchestration file
    ├── Services:
    │   ├── ollama (LLM inference engine)
    │   │   ├── Build: ./ollama
    │   │   ├── Port: 11434:11434
    │   │   ├── Volume: ./data/ollama:/root/.ollama
    │   │   ├── GPU support: NVIDIA
    │   │   ├── Network: ai-net
    │   │   └── Restart: unless-stopped
    │   ├── backend (FastAPI server)
    │   │   ├── Build: ./backend
    │   │   ├── Port: 8000:8000
    │   │   ├── Depends on: ollama
    │   │   ├── Env file: .env
    │   │   ├── Network: ai-net
    │   │   └── Restart: unless-stopped
    │   ├── frontend (React app)
    │   │   ├── Build: ./frontend
    │   │   ├── Port: 3000:3000
    │   │   ├── Depends on: backend
    │   │   ├── Network: ai-net
    │   │   └── Restart: unless-stopped
    │   ├── trivy (Security scanner)
    │   │   ├── Image: aquasec/trivy:latest
    │   │   ├── Volume: ./security/trivy/reports:/reports
    │   │   ├── Volume: /var/run/docker.sock:/var/run/docker.sock
    │   │   ├── Entrypoint: /scan.sh
    │   │   └── Network: ai-net
    │   ├── security-exporter (Metrics exporter)
    │   │   ├── Build: ./security
    │   │   ├── Port: 9110:9110
    │   │   ├── Volume: ./security/trivy/reports:/reports
    │   │   └── Network: ai-net
    │   └── load-tester (Load testing)
    │       ├── Build: ./load-test
    │       ├── Depends on: backend
    │       └── Network: ai-net
    └── Networks:
        └── ai-net (custom bridge network)

## Key Statistics

- **Total Directories**: 40+
- **Total Files**: 150+
- **Python Backend**: ~200 lines of code
- **React Frontend**: ~500 lines of code
- **Configuration Files**: 20+
- **Data Volume Size**: ~5GB (for Ollama model)
- **Docker Images**: 6 (ollama, backend, frontend, trivy, security-exporter, load-tester)

## Technology Stack Summary

### Backend
- FastAPI (async Python web framework)
- Uvicorn (ASGI server)
- OpenTelemetry (distributed tracing)
- Prometheus (metrics collection)
- Python 3.11+

### Frontend
- React 18.2
- React Markdown
- Tailwind CSS
- PostCSS
- Node.js (build time)

### LLM & Inference
- Ollama (LLM orchestration)
- Qwen2.5:7B (language model)
- NVIDIA GPU support

### Observability
- OpenTelemetry SDK/API
- OTLP Exporter
- Prometheus
- Grafana
- Tempo (traces)
- Loki (logs)

### Security
- Trivy (container scanning)
- Security exporter (metrics)

### Containerization
- Docker
- Docker Compose
- NVIDIA Docker Runtime

## Port Mappings

| Service | Port | Purpose |
|---------|------|---------|
| Frontend | 3000 | React web UI |
| Backend | 8000 | FastAPI REST API |
| Ollama | 11434 | LLM inference |
| Prometheus | 9090 | Metrics storage & query |
| Grafana | 3001 | Visualization |
| Tempo | 3100 | Trace storage |
| Loki | 3100 | Log aggregation |
| OTEL Collector | 4318 | Trace ingestion |
| Security Exporter | 9110 | Security metrics |

## Environment Variables (.env)

```
DEBUG=True
LOG_LEVEL=INFO
OLLAMA_KEEP_ALIVE=-1
OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4318
OTEL_SERVICE_NAME=ai-backend
```

## Quick Start Commands

```bash
# Build all services
docker-compose build

# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Check service status
docker-compose ps

# Run load tests
docker-compose run load-tester

# Access endpoints
curl http://localhost:8000/                    # Health check
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Hello"}'                      # Chat API
curl http://localhost:3000/                    # Frontend
curl http://localhost:8000/metrics             # Prometheus metrics
```

## Production Deployment Checklist

- [ ] Update CORS origins to production domain
  - [ ] Set DEBUG=False
  - [ ] Set LOG_LEVEL=WARN
  - [ ] Configure secret management
  - [ ] Enable HTTPS/TLS
  - [ ] Set up database for persistence
  - [ ] Deploy on cloud platform (K8s, ECS, etc.)
  - [ ] Configure CDN for static assets
  - [ ] Set up monitoring alerts
  - [ ] Implement rate limiting
  - [ ] Add authentication/authorization
  - [ ] Configure auto-scaling policies
  - [ ] Set up backup strategies
  - [ ] Document API contracts
  - [ ] Perform security audit


