from langchain_openai import OpenAI 

llm = OpenAI(temperature=0.8)
#print(llm("The dog was barking loudly when "))
print(llm("Le chian cours dans la route "))