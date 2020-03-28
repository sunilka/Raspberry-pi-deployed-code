import requests      
import os
from gtts import gTTS
import time


def NewsFromBBC(): 
      
    # BBC news api 
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=dc8e4f0486b84d01bf7c18d5d8f06e72"
  
    # fetching data in json format 
    open_bbc_page = requests.get(main_url).json() 
  
    # getting all articles in a string article 
    article = open_bbc_page["articles"] 
  
    # empty list which will  
    # contain all trending news 
    results = [] 
      
    for ar in article: 
        results.append(ar["title"]) 
    
    f= open("/home/pi/Desktop/final_year_project/news_headlines/news_text.txt","w+")
    for i in range(len(results)): 
          
        # printing all trending news 
        s = "headline "+str(i + 1)+": "+ results[i]
        print(s)
        f.write(s+"\n")
        time.sleep(1)
    f.write("Program complete, complete \n")
    f.close()
    
  
# Driver Code 
if __name__ == '__main__': 
      
    # function call 
    NewsFromBBC()  
