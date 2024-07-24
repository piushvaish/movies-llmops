from openai import OpenAI
import streamlit as st
import os
from mem0 import Memory

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

system_prompt = """
You are a multi-lingual movie enthusiast. You will receive:
- A question about a movie
- The preferred language for the answer
Your task is to provide concise and relevant information in the specified language. If the language is not provided or is unsupported, respond in English.

## Guidelines:
- If the question is ambiguous, choose the most common interpretation or offer multiple interpretations.
- If the question cannot be answered, politely explain why.
- If the query is not about movies, explain that this tool is only for movie-related queries.
- Verify that the requested language is supported and appropriate for the context.

## Response Requirements:
- Use simple, clear language.
- Do not reference follow-up questions; respond as if the conversation ends after your reply.

"""

st.set_page_config(page_title="Multilingual Movie Information Chatbot", page_icon="🎆")
# Title
st.markdown(
    f"""
    <h1 style="color: blue; text-align: center; 
        font-size: 30px; 
        text-shadow: 1px 1px 1px LightBlue;">Multilingual Movie Information Chatbot</h1> 
    <hr/>
    """,
    unsafe_allow_html=True,
)


config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "url": QDRANT_URL,
            "api_key": QDRANT_API_KEY
        }
    },
}
try:
    memory = Memory.from_config(config)
except Exception as e:
    st.error(f"Failed to initialize memory: {str(e)}")

try:
    with st.chat_message("assistant"):
        user_id = st.text_input("What's your name?", "")
        submit_button = st.button(label='Submit')
except Exception as e:
    st.error('Please enter your name')

st.divider()

st.markdown(
    f"""
    <h2 style="color: blue; text-align: center; 
        font-size: 20px; 
        text-shadow: 1px 1px 1px LightBlue;">Guess the Movie</h2> 
    <hr/>
    """,
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)

with col1:
   st.text("Movie 1")
   st.image('images/ps.jpeg')
   st.caption("""In a city where the buildings touch the sky,
A couple's love story starts with "goodbye."
Messages arrive, penned from the past,
A husband’s love that will always last.

Though winter took him from her side,
His words guide her through the changing tide.
Friends bring joy, new paths appear,
In what tale do these characters hold dear?""")

with col2:
    st.text("Movie 2")
    st.image('images/com.jpeg')
    st.caption("""In Dublin's northside, a music fan dreams,
Of a soul and rock band with harmonious themes.
He gathers his friends, each one with a role,
To mimic the sounds of Motown soul.

With Deco up front and Joey's tall tales,
A roller disco, and gigs that entail,
Arguments rise, the band falls apart,
But who kept his commitment from the start?""")

st.divider()
col3, col4 = st.columns(2)

with col3:
    st.text("Movie 3")
    st.image('images/r2.jpeg')
    st.caption("""I am a tale of growth and change,
Where a hairdresser seeks something strange.
From routine life, she longs to part,
With books and knowledge, she makes a start.

She meets a tutor, weary and old,
Whose passion for words is once more told.
But as she learns and starts to transform,
She finds her new world not quite warm.

A sabbatical ends the tale's way,
Who are the two that meet and stray?""")

with col4:
    st.text("Movie 4")
    st.image('images/t3.jpeg')
    st.caption("""In the world of spies, where secrets are sold,
Two agents meet, a tale unfolds.
One is named "Tiger," a fierce RAW hand,
The other, a dancer, from a rival land.

In Dublin's shadows, their love takes flight,
Yet loyalties pull them into the night.
With clever moves, they dodge their fate,
But in which city do they plan to elate?

Can you guess their escape, far and wide,
From a place where two worlds collide?""") # your caption here
    
st.divider()

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini"

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_prompt}]

for message in st.session_state.messages:
    # with st.chat_message(message["role"]):
    #     st.markdown(message["content"])
    # Check the role to determine how to display the message
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    elif message["role"] == "assistant":
        st.chat_message("assistant").write(message["content"])
    else:  # Default case, for system messages or any other type
        st.title("Chatbot")
# Using st.text for system messages or other roles

if user_id:
    if prompt := st.chat_input("Ask me about a movie in a language of your choice"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            memory.add(prompt, user_id=user_id)

        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
                temperature=0.2,
                max_tokens=100
            )
            response = st.write_stream(stream)
            
            memory.add(response, user_id=user_id)

        st.session_state.messages.append({"role": "assistant", "content": response})
else:
    st.text("Please submit your name.")

        
st.cache_data.clear()
st.cache_resource.clear()