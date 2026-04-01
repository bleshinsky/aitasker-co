"""Test configuration for MCP server tests."""
import sys
from pathlib import Path

# Add src directory so tests can import the package
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
# Also keep root for backwards compat (tests import `from server import ...`)
sys.path.insert(0, str(Path(__file__).parent.parent))
