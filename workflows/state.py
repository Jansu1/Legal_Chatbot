from typing import List, Dict, Any
from pydantic import BaseModel, Field

# State model for the legal chatbot
class LegalQueryState(BaseModel):
    query: str = Field(..., description="The legal question asked by the user")
    relevant_documents: List[str] = Field([], description="List of documents retrieved for the query")
    summary: str = Field("", description="Summary of the legal documents")
    query_timestamp: str = Field(..., description="Timestamp of when the query was made")
    errors: List[str] = Field([], description="List of any errors encountered during processing")
