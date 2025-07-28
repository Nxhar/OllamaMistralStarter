from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama  # Updated import

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert SQL assistant."),
    ("user", "{input}")
])

llm = ChatOllama(model="local-mistral")
chain = prompt | llm

# Streaming response token by token
for chunk in chain.stream({"input": "What are the problems with undocumented stored procedures?"}):
    print(chunk.content, end="", flush=True)
print()