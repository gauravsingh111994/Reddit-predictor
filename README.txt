Dataset - https://github.com/umbrae/reddit-top-2.5-million
PREREQUISITES :

1. Python version 3.5
2. Flask framework 
2. Python modules :
	- Pandas
	- Praw
	- os
	- math
	- time
	
	
INSTALLATION :

1. Download Python 3.5 from " https://www.python.org/downloads/release/python-350/ "
2. Install Flask using pip install flask or easy_install flask
3. Install all the modules mentioned using pip install or easy_install


RUNNING :

1. Change the url in the 'reddit.py' to url of directory containing all the data (all the 2500 .csv file) in line 10.
2. Run reddit.py from Command Prompt using python reddit.py
3. Go to the url provided in the Command Prompt.
4. Index page will open containing three button to the three task : Basic Task, Intermediate Task, Advance Task


5. Basic Task :
	- Search any word you want.
	- See the progress of search in the Command Prompt window
	- Make sure all files(.csv files) are closed while search is happening otherwise 'keyerror' will occur
	- Search result takes around 1 min.
		
6. Intermediate Task :
	- Upload the file in which you want the score prediction
	- See the progress in Command Prompt Window
	- The result contains Score-Actual, Score-Predicted, Rmse Error
	
7. Advance Task :
	- Search subreddit for which you want to scrap reddit.com for past 24 hr post.
	- The result will contain top 10 post according to score predicted.
	- Don't make too many subreddit search frequently because reddit.com allows 1000 post to be pulled in an hour.
	- If you recieve any error like 'permission denied' or 'http error' then wait for sometime and try again later.
	


INCASE :
	- If there occurs error 'keyword.csv does not exist' change the url of keyword.csv in reddit.py file to the url of the system where keyword.csv is store.
	  keyword.csv is stored in static folder
	- If switching between task takes time, refresh the page or re-run reddit.py.
		
		
 
CONTACT :
	Gaurav: mobile - 8800773457
		email  - gauravsingh111994@gmail.com 
		
	
	
