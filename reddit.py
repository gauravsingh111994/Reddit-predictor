import pandas as pd
import os,math
from flask import Flask, render_template, request
import time,praw


app = Flask(__name__)

# Change the url to the directory in which data is stored (Make sure to use double backward slash('\\') and end with double backward slash('\\')
Urldata="C:\\Users\\Gaurav\\Downloads\\reddit-top-2.5-million-master\\reddit-top-2.5-million-master\\data\\"


#Url for keyword file
Urlkeyword="static/keyword.csv"


@app.route('/')
def index():
    return render_template('/index.html')


#-------------------Basic task---------------


@app.route('/search')
def e():
    return render_template('/search.html')

@app.route('/task1',methods=['GET','POST'])

def task1():
    df1 = pd.DataFrame(
        columns=["created_utc", "score", "domain", "title", "author", "ups", "downs", "num_comments", "permalink",
                 "selftext", "link_flair_text", "over_18", "thumbnail", "subreddit_id", "edited",
                 "link_flair_css_class", "author_flair_css_class", "is_self", "name", "url", "distinguished",
                 "category"])
    dffinal=pd.DataFrame(columns=['Title','Subreddit','Selftext','Ups','Downs','Score'])
    if request.method == 'POST':
        search = request.form['search']
        for root, dirs, files in os.walk(Urldata):

            i=1
            for file in files:
                f=Urldata+file
                cat=file.split('.')

                print(i," File scanned out of ",len(files))
                i += 1

                df=pd.read_csv(f)
                df['category'] = cat[0]
                df.fillna("-1",inplace=True)
                df1=df1.append(df[(df['title'].str.contains(search)) | (df['selftext'].str.contains(search)) |(df['author'].str.contains(search)) | (df['domain'].str.contains(search))| (df['url'].str.contains(search))])
                #df1 = df1.append(df[df['selftext'].str.contains(search)])

                #df1 = df1.append(df[(df['author']==search) | (df['domain']==search) | (df['url']==search)])


    df1=df1.drop_duplicates()
    dffinal['Title']=df1['title']
    dffinal['Subreddit']=df1['category']
    dffinal['Ups']=df1['ups']
    dffinal['Downs']=df1['downs']
    dffinal['Score']=df1['score']
    dffinal['Selftext']=df1['selftext']
    dffinal=dffinal.sort_values(by='Score', ascending=False).reset_index(drop=True)
    return render_template('/view1.html', tables=[dffinal.to_html()], data=len(df1), sitem=search)




#------------------- Intermediate task-------------------


@app.route('/uploadfile')
def upload_file():
    return render_template('/upload.html')




@app.route('/task2',methods=['GET','POST'])

def prediction():
    if request.method == 'POST':
        file = request.files['file']
        df=pd.read_csv(file)
        df1 = pd.DataFrame(columns=["Title", "Score-Actual", "Score-Predicted", "SquareError"])
        dfk=pd.read_csv(Urlkeyword)
        for i in range(0, len(df)):
            s = str(df['title'][i]) + " " + str(df['selftext'][i])
            s1 = s.split(" ")
            count = 0
            totale=0
            for j in range(0, len(s1)):
                count = count + (len(dfk[dfk['keyword'] == s1[j]]))

            pscore = abs(df['ups'][i] - df['downs'][i] - (0.041 * count) + 0.0190)
            print(i+1," Score Predicted out of ",len(df))


            pscore = round(pscore,0)
            error=(df['score'][i] - pscore) * (df['score'][i] - pscore)
            df1.loc[i, 'Title'] = df['title'][i]
            df1.loc[i, 'Score-Actual'] = df['score'][i]
            df1.loc[i, 'Score-Predicted'] = pscore
            df1.loc[i, 'SquareError'] = error
            totale += error

    meansquare=totale/(len(df))
    rmse=math.sqrt(meansquare)
    rmse=round(rmse,2)
    df1 = df1.sort_values(by='Score-Predicted', ascending=False).reset_index(drop=True)
    return render_template('/view.html',tables=[df1.to_html()],data=rmse)


#-------------Advance Task-----------------------

@app.route('/bot')

def bot():
    return render_template('/bot.html')

@app.route('/task3', methods=['GET','POST' ])

def tast3():
    if request.method == 'POST':
        search = request.form['search']
        df = pd.DataFrame(columns=['Title', 'SelfText', 'Ups', 'Downs'])
        YESTERDAY = time.time() - (24 * 60 * 60)
        i = 0
        r = praw.Reddit(user_agent='get_last_day_of_posts')
        sub = r.get_subreddit(search)

        for post in sub.get_new(limit=100):
            if post.created_utc < YESTERDAY:
                break
            else:
                df.loc[i, 'Title'] = post.title
                df.loc[i, 'SelfText'] = post.selftext
                df.loc[i, 'Ups'] = post.ups
                df.loc[i, 'Downs'] = post.downs
                df.loc[i, 'Score-Actual'] = post.score
                i = i + 1
        df = df.sort_values(by='Ups', ascending=False)[:10].reset_index(drop=True)
        dfk = pd.read_csv(Urlkeyword)
        for i in range(0, len(df)):
            s = str(df['Title'][i]) + " " + str(df['SelfText'][i])
            s1 = s.split(" ")
            count = 0
            for j in range(0, len(s1)):
                count = count + (len(dfk[dfk['keyword'] == s1[j]]))

            pscore = abs(df['Ups'][i] - df['Downs'][i] - (0.041 * count) + 0.0190)
            pscore = round(pscore, 0)
            df.loc[i,'Score-Predicted']=pscore



    return render_template('/view2.html',tables=[df.to_html()],data=search)



if __name__ == '__main__':
    app.run(debug="true")
