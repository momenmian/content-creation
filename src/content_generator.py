import os
from dotenv import load_dotenv
from langchain import PromptTemplate, LLMChain
from langchain_openai import ChatOpenAI

# Load environment variables if not already loaded
def load_environment():
    load_dotenv()
    return {
        "base_url": os.getenv("base_url"),
        "api_key": os.getenv("api_key"),
        "model": os.getenv("model")
    }

def get_llm():
    """Initialize and return the language model with environment settings."""
    env = load_environment()
    
    return ChatOpenAI(
        model=env["model"],
        temperature=0.3,
        max_tokens=8192,
        api_key=env["api_key"],
        base_url=env["base_url"],
    )

def generate_social_media_post(topic):
    """Generate a social media post about the given topic."""
    llm = get_llm()
    
    prompt_template = PromptTemplate(
        input_variables=["topic"],
        template="Create a short, engaging social media post about {topic}"
    )
    
    llm_chain = LLMChain(prompt=prompt_template, llm=llm)
    response = llm_chain.run(topic)
    
    return response

# Add more content generation functions as needed
def generate_blog_post(topic, word_count=500):
    """Generate a blog post about the given topic with approximate word count."""
    llm = get_llm()
    
    prompt_template = PromptTemplate(
        input_variables=["topic", "word_count"],
        template="Write an informative blog post about {topic} in approximately {word_count} words."
    )
    
    llm_chain = LLMChain(prompt=prompt_template, llm=llm)
    response = llm_chain.run(topic=topic, word_count=word_count)
    
    return response
