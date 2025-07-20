# Sahara Crypto Agent

A command-line agent for interacting with cryptocurrency wallets, built in Python.

## Features

- Command-line interface for wallet operations
- Ethereum wallet address input
- (Add more features as you develop them)

## Getting Started

### Prerequisites

- [uv](https://github.com/astral-sh/uv) (Python package/dependency manager)
- Python 3.8+

### Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/sahara-agent.git
cd sahara-agent
```

Install dependencies using uv:

```bash
uv pip install -r requirements.txt
```
_or, if using pyproject.toml:_
```bash
uv pip install -r pyproject.toml
```

### Usage

Run the agent:

```bash
uv run main.py
```

You will be prompted to enter your wallet address.

### Project Structure

- `main.py` — Main entry point for the CLI agent
- `pyproject.toml` — Project metadata and dependencies
- `uv.lock` — uv lockfile for reproducible installs

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License



---

*This README was generated based on the project structure and inferred purpose. Update it as your project evolves!*
