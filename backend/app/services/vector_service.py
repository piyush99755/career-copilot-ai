import chromadb

class VectorService:
    
    def __init__(self):
        
        
        self.client = chromadb.PersistentClient(
            path="./data/chromadb"
        )

        self.collection = self.client.get_or_create_collection(
            name="resume_chunks"
        )
        
    def get_all_chunks(self):
        return self.collection.get()
     
          
    def store_chunk(
        self,
        chunk_id:str,
        chunk_text:str,
        embedding: list
    ):
        self.collection.add(
            ids=[chunk_id],
            documents=[chunk_text],
            embeddings=[embedding]
            
        )
        
    def count_chunks(self):
        return self.collection.count()
    
    def search_chunks(
        self,
        query_embedding,
        n_results=3
    ):
        return self.collection.query(
            query_embeddings = [query_embedding],
            n_results=n_results
            
        )
        
        