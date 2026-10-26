import sys
from pathlib import Path

# The plugin's root, as Dify runs it: `tools.common` and `provider.pidgeon` import from there.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
