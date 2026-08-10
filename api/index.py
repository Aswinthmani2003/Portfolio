import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app import app

# Vercel serverless handler
__all__ = ['app']
