from bs4 import BeautifulSoup
import requests
import re
'''
 1. Take Input
 2. Create Scraper
 3. Run scraper
 4. Get the data
 5. Process the data
 6. Write the data to a file where it can be read
'''

def First_Layer():
    print("Preparing scraper...")
    print("Hello sir I am a essay generator please enter the topic of your essay below")
    topic = raw_input()
    print("Topic: "+topic)
    return topic

def Scrapy(topic):
    url = "https://en.wikipedia.org/wiki/"+topic
    page = requests.get(url=url)
    print(page.status_code)
    content = page.content
    soup = BeautifulSoup(content, "html.parser")
    text = soup.find_all("p")
    final = text[0:16200]
    return final

def processing_data(data):
    clean = re.compile('<.*?>')
    data = str(data)
    data = re.sub(clean, "", data)
    clean2 = re.compile('\.*?/')
    data = re.sub(clean2, "", data)
    data = data.replace('(', "")
    data = data.replace("\n", "")
    data = data.replace(")", "")
    data = data.replace("[", "")
    data = data.replace("]", "")
    return data

def Softmax(data, topic):
    savefILE = open("writer.txt", "w")
    savefILE.write("Essay")
    savefILE.write("")
    savefILE.write(data)


'''if __name__ == "__main__":
    topic = First_Layer()
    body = Scrapy(topic)
    body = processing_data(body)
    Softmax(body, topic)'''

if __name__ == "__main__":
    topic = First_Layer()
    body = Scrapy(topic)
    body = processing_data(body)
    Softmax(body, topic)