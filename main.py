import requests

r = requests.get(' https://stats.nba.com/stats/boxscoremisc')

print(r.text)