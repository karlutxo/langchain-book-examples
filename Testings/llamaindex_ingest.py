from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings

# global default
Settings.embed_model = OpenAIEmbedding()

documents = SimpleDirectoryReader("./data").load_data()

index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

response = query_engine.query("cual es el nombre, dni, la categoria profesional y el tipo de contrato del cod_empleado JDC ?")

print(response)







""" from llama_index.core.node_parser import JSONNodeParser
from llama_index.readers.file import FlatReader
from pathlib import Path

reader = FlatReader()
document = reader.load_data(Path("./data/contratos.json"))

json_parser = JSONNodeParser.from_defaults()
nodes = json_parser.get_nodes_from_documents(document)
 """
# for node in nodes:
#     print(f"Metadata {node.metadata} \nText: {node.text}")


