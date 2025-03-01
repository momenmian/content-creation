"""
Content Creation Package

This package provides tools for AI-powered content generation
using the Moonshot AI API.
"""

# Import section - runs regardless of how the file is used
try:
    # Try relative import first (when used as a package)
    from .content_generator import (
        generate_social_media_post,
        generate_blog_post,
        get_llm,
        load_environment
    )
except ImportError:
    # Fall back to absolute import (when imported but not as part of package)
    from src.content_generator import (
        generate_social_media_post,
        generate_blog_post,
        get_llm,
        load_environment
    )

# Define what should be available when using 'from src import *'
__all__ = [
    'generate_social_media_post',
    'generate_blog_post',
    'get_llm',
    'load_environment'
]

# Package metadata
__version__ = '0.1.0'
__author__ = 'Abdul Momen Miah'

# Import main function so it can be run with "python -m src"
from .content_generator import (
    generate_social_media_post,
    generate_blog_post,
    get_llm,
    load_environment
)
from .__main__ import main
