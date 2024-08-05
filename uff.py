import psycopg2
from fastapi import FastAPI
import time
from fastapi import responses,HTTPException,status
import random
from pydantic import BaseModel
from psycopg2.extras import RealDictCursor

app=FastAPI()

while True:
      try:
          conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',
                                password='Dhruva2005')
          cursor=conn.cursor()
          print("The database is succefully connected")
          break
      except Exception as error:
          print("error connecting databse")  
          print("Error: ",error)
          time.sleep(3)    

@app.get("/posts/random",status_code=status.HTTP_200_OK)          
def nig():
     cursor.execute("SELECT * FROM jokes ORDER BY RANDOM() LIMIT 1")
     post=cursor.fetchone()
     joke_text=post[1]
     if not post:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid id")
     print(joke_text)
     return{"message":joke_text}

def halo(post:Post):
     cursor.execute("INSERT INTO jokes(joke) VALUES(%s) RETURNING * ",(post.joke))
     new_post=cursor.fetchone()
     conn.commit()
     return{"mes":new_post}'''