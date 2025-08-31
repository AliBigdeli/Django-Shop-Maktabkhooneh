## 📂 Scripts Overview

| Script | Description |
|--------|-------------|
| `scripts/venv.sh` | Create a virtual environment and install all Python dependencies from `requirements.txt`. |
| `scripts/migrate.sh` | Run Django database migrations (`makemigrations` and `migrate`). |
| `scripts/collectstatic.sh` | Collect all static files into the `STATIC_ROOT` directory. |
| `scripts/docker-build.sh` | Build Docker images and start Docker containers using `docker-compose` for the project. |
| `scripts/test.sh` | Run the Django project's test suite to ensure code correctness. |

---

## ⚡ Getting Started

### 1. Make Scripts Executable
Before running the scripts, make sure they are executable:
```bash
chmod +x bash-scripts/*.sh
