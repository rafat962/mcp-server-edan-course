# Use official Python 3.13 slim image
FROM python:3.13-slim-bookworm

# Install uv by copying binaries from official Astral image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Enable bytecode compilation and use copy mode for uv
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Copy dependency definition files first (for Docker layer caching)
COPY pyproject.toml uv.lock* ./

# Install dependencies into virtual environment
RUN uv sync --frozen --no-install-project --no-dev

# Copy application source code
COPY . .

# Run the MCP server
CMD ["uv", "run", "main.py"]
