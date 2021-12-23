from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template, url_for
import index


filtered_list = []
filtered_title = []
indexer = -1
filter_words_one = ["racial equity","social justice",
"black entrepreneurship","racial wealth gap","hcbu",
"entrepreneur","data","initiative", "data justice", "ethical data"]
max = 0


for i in index.link_list:
    url = requests.get(i)
    soup = BeautifulSoup(url.content, 'html.parser')
    items = soup.find_all('p')
    indexer += 1
    for stuff in items:
        item = stuff.text.lower()
        for filterone in filter_words_one:
            if filterone in item:
                if i not in filtered_list and max!= 15:
                    filtered_list.append(i)
                if index.title_list[indexer] not in filtered_title and max!=15:
                    filtered_title.append(index.title_list[indexer])
                    max +=1
                break


app = Flask(__name__)   

@app.route('/')
def index():
    return render_template ("new.html", title1=filtered_title[0], link1=filtered_list[0], 
    title2=filtered_title[1],link2=filtered_list[1],
    title3=filtered_title[2],link3=filtered_list[2],
    title4=filtered_title[3],link4=filtered_list[3],
    title5=filtered_title[4],link5=filtered_list[4],
    title6=filtered_title[5],link6=filtered_list[5],
    title7=filtered_title[6],link7=filtered_list[6],
    title8=filtered_title[7],link8=filtered_list[7],
    title9=filtered_title[8],link9=filtered_list[8],
    title10=filtered_title[9],link10=filtered_list[8],
    title11=filtered_title[10],link11=filtered_list[10],
    title12=filtered_title[11],link12=filtered_list[11],
    title13=filtered_title[12],link13=filtered_list[12],
    title14=filtered_title[13],link14=filtered_list[13],
    title15=filtered_title[14],link15=filtered_list[14],
    )
    
        
if __name__ == '__main__':
    app.run(debug=True)

