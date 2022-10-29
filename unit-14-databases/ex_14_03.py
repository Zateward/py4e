import tweepy
import sqlite3

connection = sqlite3.connect('database_03.db')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Twitter')
cursor.execute('CREATE TABLE Twitter (User TEXT, ID INTEGER, Followers INTEGER)')

auth = tweepy.OAuthHandler('oj5v95pKj04tw70yto8VZ7HDq', 'O0akd70THuGoRRFCHw6regvPTZFrPIAALK7idAeRErmjl2EH8A')
auth.set_access_token('1157384166192926726-Q7YzCzMo8XjuUTK5llwD64tldPJaKw', 'QB7OD6uTrJoDrOtV9SqwdTSiSBe7kkrHIfbFDHV8qrcMd')

api = tweepy.API(auth)

while True:
    user = input('Enter an username: ')
    if len(user) < 1: break
    #cursor.execute(INSERT INTO Twitter (User) VALUES (user))
    user_data = api.get_user(user)
    print(api.get_user(user))

    twitter_user = user_data.screen_name
    followers = user_data.followers_count
    id = user_data.id

    cursor.execute('INSERT INTO Twitter (User, ID, Followers) VALUES (?,?,?)',(twitter_user,id,followers))

connection.commit()
cursor.close()
