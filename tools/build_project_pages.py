"""Rebuild content while preserving the cosmic design and original Hero."""
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).with_name('update_content.py')),run_name='__main__')
