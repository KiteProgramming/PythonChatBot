import random
import getpass
import json
import http.client
import requests
import sys
import urllib.parse
listOfTopics = ["SPORTS", "NEWS", "BOOKS", "MOVIES", "WEATHER"]

def userLogin():
    name = ["KANYE", "GEORGE", "BOB", "DAVE", "POGO"]
    userFirstInput = input("Please enter your username: ")
    userFirstInput = userFirstInput.upper()
    if userFirstInput in name:
        print("Welcome " + userFirstInput)
        userPasswordInput = getpass.getpass("Please enter password: ")
        # userPasswordInput = input("Please enter password: ")
        if userFirstInput == "KANYE":
            if userPasswordInput == "kanyeyeast":
                print("You are now able to use the chat bot.")
            else:
                print("You are not allowed here, goodbye.")
                exit()
        elif userFirstInput == "GEORGE":
            if userPasswordInput == "george123":
                print("You are now able to use the chat bot.")
            else:
                print("You are not allowed here, goodbye.")
                exit()
        elif userFirstInput == "BOB":
            if userPasswordInput == "bob123":
                print("You are now able to use the chat bot.")
            else:
                print("You are not allowed here, goodbye.")
                exit()
        elif userFirstInput == ("POGO"):
            if userPasswordInput == "pogo123":
                print("You are now able to use the chat bot.")
            else:
                print("You are not allowed here, goodbye.")
                exit()
        elif userFirstInput == ("DAVE"):
            if userPasswordInput == ("123savage"):
                print("21 21 21")
            else:
                print("I'm disappointed.")
                exit()
    else:
        print("You aren't a valid user.")
        exit()

def Sports():
    favSport = input("Which sport would you like to talk about? ")
    favSport = favSport.upper()
    footie = ["FOOTBALL", "FOOTIE", "FOOTY", "FUTBAL", "FOOTBAL", "FOOTBOLL"]
    tennis = ["TENNIS", "TENIS", "TENNISS"]
    Yes = ["yes", "YES", "yeah", "ye", "yea", "yus"]
    No = ["no", "nah", "noo", "nu", "nope"]
    footballTeams = []
    footballLeagues = {"BUNDESLIGA" : "BL1", "PREMIER LEAGUE" : "PL", "WORLD CUP" : "WC", "CHAMPIONS LEAGUE" : "CL", "LIGUE 1" : "FL1", "SERIE A" : "SA", "LA LIGA" : "PD", "PRIMERA DIVISION" : "PD"}
    if favSport in footie:
        favLeagueInput = input("Which football league is your favourite? My personal favourite is the premier league: ")
        favLeagueInput = favLeagueInput.upper()
        if favLeagueInput in footballLeagues.keys():
            c = footballLeagues.get(favLeagueInput)
            sportConnection = http.client.HTTPConnection('api.football-data.org')
            sportHeaders = { 'X-Auth-Token': "3bb5ce52167545eba1be7e267522a063" }
            sportConnection.request('GET','/v2/competitions/' + c + '/teams', None, sportHeaders)
            sportResponse = json.loads(sportConnection.getresponse().read().decode())
            favLeague = sportResponse["competition"]["name"]
#           print(sportResponse)
            print("Your favourite league is " + favLeague)
            favLeagueID = sportResponse["competition"]["id"]
            print("Your favourite league's ID is " + str(favLeagueID))
            favLeagueCountry = sportResponse["competition"]["area"]["name"]
            print("Your favourite league is in " + favLeagueCountry)
            leagueLen = len(sportResponse["teams"])
            userChoice = input("Would you like to know all the teams in the league you have chosen? ")
            if userChoice in Yes:
                for i in range(leagueLen):
                    print(sportResponse["teams"][i]["name"])
                    footballTeams.append(sportResponse["teams"][i]["name"])
                favTeam = input("Do you have a favourite team in this league? My favourite is Crystal Palace: ")
                if favTeam in footballTeams:
                    for x in range(leagueLen):
                        print(sportResponse["teams"][x]["squad"])
                else:
                    print("WRONG")
            elif userChoice in No:
                input("Would you like to view anything else about sports? ")
                if userChoice in Yes:
                    Sports()
                elif userChoice in No:
                    intialInput()
        else:
            Sports()
                
    elif favSport in tennis:
        #tennisAPI = "https://api.sportradar.com/tennis-t2/en/schedules/" + year + "-" + month + "-" + day "/schedule.json?api_key=" + apiTennisKey
        dateOfInput = input("Input date: ")
        apiTennisKey = "hgp4xaq52zbqtvr5k73hx8j3"
        tennisConnection = http.client.HTTPConnection('api.sportradar.com')
        tennisHeaaders = {'api_key': "hgp4xaq52zbqtvr5k73hx8j3"}
        tennisConnection.request('GET', '/tennis-t2/en/schedules/' + dateOfInput + "/schedule.json?api_key=" + apiTennisKey, None)
        tennisResponse = json.loads(tennisConnection.getresponse().read().decode())
        #print(tennisResponse)
        tennisAmount = len(tennisResponse["sport_events"])
        for o in range(tennisAmount):
            tennisFavPlayer = tennisResponse["sport_events"][o]
            print(tennisFavPlayer)
    else:
        print("Whoops, don't know anything about that sport, can we interest you in another sport?")
        
def news():
    UserRequest1 = input(": ")
      
    encoded = urllib.parse.quote(UserRequest1)

    apiAdd2 = "https://newsapi.org/v2/everything?"
    keywords2 = 'q='+ encoded
    apikey = "&apikey=9430b58b162f4318bf862402d40a634d"
    url2 = apiAdd2 + keywords2 + apikey
    jsonData2 = requests.get(url2).json()
    print(url2)
    
    for i in range(5):
        _a_ = jsonData2['articles'][i]['author']
        print(_a_)
        _b_ = jsonData2['articles'][i]['title']
        print(_b_)
        _c_ = jsonData2['articles'][i]['description']
        print(_c_)
        _d_ = jsonData2['articles'][i]['url']
        print(_d_)
        #_e_ = jsonData2['articles'][i]['urlToImage']
        #print(_e_)
        
        _g_ = jsonData2['articles'][i]['publishedAt']
        print(_g_)
        _h_ = jsonData2['articles'][i]['content']
        print(_h_)
        i +=1
        
def WeatherA():
    message = input()
    x = message
    x = x.lower()
    weather = ['weather','rainy','sunny','sun','clouds','rain']
    if message in weather:        
        api_adress = 'http://api.openweathermap.org/data/2.5/weather?appid=ca46285711e4bdc2f488e0089eac4758&q='
        city = input('Please enter the name of the city that you want to know the weather')
        city = city.capitalize()
        url = api_adress + city
        json_data = requests.get(url).json()
        formatted_data = json_data['weather'][0]['description']
        formatted2_Data = json_data['main']['temp'] - 272.15
        print('It\'s' , round(formatted2_Data),'Celsius Degrees','and I can see',formatted_data,'in',city) 
    else:
        print('Not available feature but i will pop a suggestion to my programmer :)')

def books():
    check_for_isbn=["ISBN"]
    check_for_book=["BOOK","NAME"]
    user_choice=input("Do you want to enter the name of the book or the ISBN number? --->")
    user_choice=user_choice.upper()
    l=user_choice.split()
    print(l)
    for s in check_for_isbn:
        for item in l:
            if item in s:
                x=1
    for s in check_for_book:
        for item in l:
            if item in s:
                x=2
    if x==1:
        user_input=input("Input the ISBN number of the book --->")
        isbn=user_input
        res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "PqNAvSvH8oJusnUrHiqcgg", "isbns": isbn}) 
        file=res.json()
        print(file) 
    elif x==2:
        user_input=input("Input the name of the book --->")
        user_input=user_input.upper()
        user_input_list=user_input.split()
        x3=len(user_input_list)
        for i in range(x3):
            x4=str(user_input_list[i])
            x4=x4.upper() 
            user_input_list[i]=x4
        pickle_in = open("dict.pickle","rb")
        long_dict = pickle.load(pickle_in)
        isbn=long_dict[user_input]
        res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "PqNAvSvH8oJusnUrHiqcgg", "isbns": isbn}) 
        file=res.json()
        print(user_input_list)
    else:
        print("Input KEYWORD 'Book' or 'Name', to search by name")
        print("Input KEYWORD 'ISBN' to search by ISBN number")
        books()
    print("This book has a rating of: ",file["books"][0]["average_rating"]) 
    av_rating=float(file["books"][0]["average_rating"])
    no_review=(file["books"][0]["work_text_reviews_count"])
    no_rating=(file["books"][0]["work_ratings_count"])  
    if av_rating <=1:
        print("I would not recommend this book, \nIt doesnt have great reviews")
    elif av_rating <=2:
        print("This book does not have great reviews")
    elif av_rating <=3:
        print("This book is alright, it has decent reviews")
    elif av_rating <=4:
        print("This book has pretty good reviews")
    else:
        print("This book has great reviews, \nI would definitely recommend it")
        print("This book has,",no_review,"reviews")
        print("This book has,",no_rating,"ratings")
    '''work_ratings_count = All ratings submitted for all versions of the book
    ratings_count = Ratings submitted for this edition of the book
    work_text_reviews_count = All text reviews written for all versions of the book
    text_reviews_count = All text reviews written for this edition of the book
    reviews_count = Number of people who added any input on goodreads for this edition of the book
    work_reviews_count = Number of people who added any input on goodreads for all versions of the book
    average_rating = The average rating for the book for all versions of the book'''
    
userLogin()
intialInput = input("What would you like to talk about? ")
intialInput = intialInput.upper()

if intialInput in listOfTopics:
    if intialInput == "SPORTS":
        Sports()
    elif intialInput == "NEWS":
        news()
    elif intialInput == "VIDEO GAMES":
        videoGames()
    elif intialInput == "WEATHER":
        WeatherA()
    elif intialInput == "BOOKS":
        books()
else:
    randomNum = randint(1,5) 
    if randomNum == 1:
        randomTopic = "Sports"
    elif randomNum == 2:
        randomTopic = "News"
    elif randomNum == 3:
        randomTopic = "Video Games"
    elif randomNum == 4:
        randomTopic = "Weather"
    elif randomNum == 5:
        randomTopic = "Books and Movies"
    print("We don't know much about that, maybe I can interest you in something we do know about, like: " + randomTopic)

