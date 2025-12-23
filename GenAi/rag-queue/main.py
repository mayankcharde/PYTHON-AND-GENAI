from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Query
from .client.rq_client import queue
from .queues.workers import process_query



app = FastAPI()

# DEMO ROUTE
@app.get('/')
def root():
    return {"status": 'Server is up and running'}

# IN THIS ROUTE WE BASICALLY ADDING OUR QUERY AND GIVE IT TO THE PROCESS_QUERY FUNCTION
@app.post('/chat')
def chat(
        query: str = Query(..., description="The chat query of user")
):
    job = queue.enqueue(process_query, query)

#  IT BASICALLY GIVES THE ID OF THE QUERY
    return { "status": "queued", "job_id": job.id }


# 
@app.get('/job-status')
def get_result(
        job_id: str = Query(..., description="Job ID")
):
    #  HERE WE BASICALLY FETCHING THE JOB_ID HENCE RESPONSE
    job = queue.fetch_job(job_id=job_id)
    #  HERE WE RETURN THE RESPONSE GIVEN BY THE RAG MODEL
    result = job.return_value()
    
    return { "result":  result}