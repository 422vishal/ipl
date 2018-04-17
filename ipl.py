import urllib.request as urllib2
import re
from bs4 import BeautifulSoup
ipl_page = 'https://www.iplt20.com/stats/2018/player-points'
page = urllib2.urlopen(ipl_page)
soup = BeautifulSoup(page)
player_dict = {}
table = soup.find('table', attrs={'class':'table table--scroll-on-tablet top-players'})
rows = table.find_all('tr')
for row in rows:
    player_info = row.find_all('img',attrs={'js-headshot'})
    player_stats = row.find_all('td',attrs={'class':'top-players__pts'})
    player_name = None
    player_score = None	
    for i in player_info:
       player_name = i["alt"]
    for player in player_stats:
       player_score = player.getText()
       player_score = re.sub("[^0-9.]", "",player_score)
    player_dict[player_name] = player_score


vishal = ["Rohit Sharma Headshot","Sunil Narine Headshot","Sunil Narine Headshot","Jasprit Bumrah Headshot","Andrew Tye Headshot","Kane Williamson Headshot","Jos Buttler Headshot","Shane Watson Headshot","Hardik Pandya Headshot","Aaron Finch Headshot","Jaydev Unadkat Headshot","JP Duminy Headshot","Manan Vohra Headshot","Sanju Samson Headshot","Mohammed Shami Headshot","Dhawal Kulkarni Headshot"]

manav = ["Suresh Raina Headshot","Chris Morris Headshot","Chris Morris Headshot","Bhuvneshwar Kumar Headshot","Chris Lynn Headshot","Joffrey Archer Headshot","Krunal Pandya Headshot","Evin Lewis Headshot","Ravichandran Ashwin Headshot","Umesh Yadav Headshot","Imran Tahir Headshot","Mustafizur Rahman Headshot","Nitish Rana Headshot","Alex Hales Headshot","Amit Mishra Headshot","Karun Nair Headshot"]

tejas = ["Rashid Khan Headshot","AB de Villiers Headshot","AB de Villiers Headshot","Manish Pandey Headshot","Robin Uthappa Headshot","Rishabh Pant Headshot","Glenn Maxwell Headshot","Lokesh Rahul Headshot","Washington Sundar Headshot","Trent Boult Headshot","Shreyas Iyer Headshot","MS Dhoni Headshot","Chris Woakes Headshot","David Miller Headshot","Deepak Hooda Headshot","Basil Thampi Headshot"]

aarjav = ["Ben Stokes Headshot","Yuzvendra Chahal Headshot","Yuzvendra Chahal Headshot","Andre Russell Headshot","Ajinkya Rahane Headshot","Dinesh Karthik Headshot","Marcus Stoinis Headshot","Kieron Pollard Headshot","Kuldeep Yadav Headshot","Faf Du Plesis Headshot","Ishan Kishan Headshot","Mayank Agarwal Headshot","Ravindra Jadeja Headshot","Wriddhiman Saha Headshot","Axar Patel Headshot","Vijay Shankar Headshot"]

rohan = ["Virat Kohli Headshot","Virat Kohli Headshot","Colin Munro Headshot","Gautam Gambhir Headshot","Dwayne Bravo Headshot","Shikhar Dhawan Headshot","D'Arcy Short Headshot","Rabada Headshot","Yuvraj Singh Headshot","Kedar Jadhav Headshot","Chris Gayle Headshot","Ben Cutting Headshot","Shakib Al Hasan Headshot","Klassen Headshot","Parthiv Patel Headshot","Rahul Tripathi Headshot"]

vice_captains = ["Rohit Sharma Headshot","Suresh Raina Headshot","Rashid Khan Headshot","Ben Stokes Headshot","Colin Munro Headshot"]

playing_players = [vishal,manav,tejas,aarjav,rohan]

for players in playing_players:
	final_score =0
	for player in players:
			value = player_dict.get(player.strip())
			if value is not None:
			   print (player,value)
			   if player in vice_captains:
			      value = float(value) * 1.5
			      print(value)
			   final_score = float(final_score) + float(value)
	print('\n'+'Final Score '+str(final_score)+'\n')	


	







			
			
			