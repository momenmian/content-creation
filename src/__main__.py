"""
Main module to run content generation directly from the command line.
"""
from .content_generator import (
    generate_social_media_post,
    generate_blog_post,
    get_llm,
    load_environment
)

def main():
    """Run content generation demo."""
    print("Content Creation Demo")
    print("====================")
    
    # Load environment variables
    env_vars = load_environment()
    print(f"Using model: {env_vars['model']}")
    
    # Generate a social media post
    topic = "artificial intelligence"
    print("\nGenerating social media post about {topic}...\n")
    social_post = generate_social_media_post(topic)
    print(f"Social Media Post:\n{social_post}\n")
    
    # Generate a short blog post
    print(f"Generating short blog post about {topic}...\n")
    blog_post = generate_blog_post(topic, word_count=200)
    print(f"Blog Post:\n{blog_post}")

if __name__ == "__main__":
    main()