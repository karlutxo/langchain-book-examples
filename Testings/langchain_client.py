from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:8001/chain/")
response = remote_chain.invoke({"language": "french", "text": "I eat pizza, you eat spaguettis, he eats nogchi, we eat provolone cheese, they eat mascarpone"})

print(response)