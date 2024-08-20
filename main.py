import streamlit as st
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(
    page_title="Blog Post Generator",
    page_icon="🔗"
)
st.title("Blog Post Generator")

openai_api_key =st.sidebar.text_input(
    "OpenAI API Key",
    help="Get your API key from https://platform.openai.com/account/api-keys",
    type="password",
)


def generate_blog_post(topic,openai_api_key=openai_api_key):
    try:
        llm = OpenAI(openai_api_key=openai_api_key)
    except Exception as e:
        st.write(f"An error occurred: {e}")
        return  # Exit early
    template = """
        As experienced startup and venture capital writer, 
            generate a 400-word blog post about {topic}
            
            Your response should be in this format:
            First, print the blog post.
            Then, sum the total number of words on it and print the result like this: This post has X words.

        """
    prompt = PromptTemplate(
        input_variables = ["topic"],
        template = template
    )

    query = prompt.format(topic=topic)
    response = llm(query,max_tokens=2048)
    return st.write(response)

topic_text =st.text_input('Enter the topic of the blog post')
if st.button("Generate Blog Post"):
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key")
    else:
        try:
            generate_blog_post(topic_text,openai_api_key)
        except Exception as e:
            st.write(f"An error occurred: {e}")
