import pyautogui as pg
import webbrowser as wb
import time as t

points = 0
show = pg.prompt("What is your favorite show? ")

if show == "The Vampire Diaries":
    pg.alert("That is a really good show!")
    wb.open("https://www.youtube.com/watch?v=BmVmhjjkN4E")
    t.sleep(5)
    points += 5
elif show == "Riverdale":
    pg.alert("I love Jughead!")
    wb.open("https://www.youtube.com/watch?v=nXZNS1WtWtI")
    t.sleep(5)
    points += 3
elif show == "Gossip Girl":
    pg.alert("I know who the gossip girl is!")
    wb.open("https://www.youtube.com/watch?v=7m4TzZOa4yM")
    t.sleep(5)
    points -= 1
elif show == "Friends":
    pg.alert("I am so much like Pheobe!")
    wb.open("https://www.youtube.com/watch?v=uOBBzBFcbMs")
    t.sleep(5)
    points += 6
elif show == "The Office":
    pg.alert("I do not think that show is funny.")
    wb.open("https://www.youtube.com/watch?v=uyIVAm9PVrI")
    t.sleep(5)
    points -= 7
elif show == "Andi Mack":
    pg.alert("That show is so cringy!")
    wb.open("https://www.youtube.com/watch?v=njZiBspvfDc")
    t.sleep(5)
    points -= 4
else:
    pg.alert("Your favorite show is " + show)


season = pg.prompt("What is your favorite season? ")

if season == "Fall":
    pg.alert("I love fall!")
    wb.open("https://www.youtube.com/watch?v=zbUMXD7ZqTw")
    t.sleep(5)
    points += 6
elif season == "Winter":
    pg.alert("It is so cold in the winter.")
    wb.open("https://www.youtube.com/watch?v=ZwmNfO2LuqI")
    t.sleep(5)
    points -= 2
elif season == "Spring":
    pg.alert("I love when I see flowers blooming!")
    wb.open("https://www.youtube.com/watch?v=cxmIeUmG9Lo")
    t.sleep(5)
    points += 8
elif season == "Summer":
    pg.alert("That is the best season because there is no school!")
    wb.open("https://www.youtube.com/watch?v=NPpM2D2Siik")
    t.sleep(5)
    points += 4
elif season == "love all":
    pg.alert("I love all of them!")
    wb.open("https://www.youtube.com/watch?v=GRxofEmo3HA")
    t.sleep(5)
    points -= 1
elif season == "Do not have a favorite":
    pg.alert("I do not have a favorite because I do not really care!")
    points -= 3
else:
    pg.alert("Your favorite season is " + season)


color = pg.prompt("What is your favorite color?")

if color == "Yellow":
    pg.alert("That is a pretty color!")
    wb.open("https://www.youtube.com/watch?v=9rqPiqwtxx4")
    t.sleep(5)
    points += 9
elif color == "Light Pink":
    pg.alert("I like that color better than yellow.")
    wb.open("https://www.youtube.com/watch?v=VE9yYKL9U6M")
    t.sleep(5)
    points += 4
elif color == "Gold":
    pg.alert("That color is so cool. ")
    wb.open("https://www.youtube.com/watch?v=eco-tKuuS1E")
    t.sleep(5)
    points -= 2
elif color == "Blue":
    pg.alert("That color reminds me of sadness.")
    wb.open("https://www.youtube.com/watch?v=I6ILheTtuq4")
    t.sleep(5)
    points -= 4
elif color == "Green":
    pg.alert("That color is so ugly.")
    wb.open("https://www.youtube.com/watch?v=50Uh9PpbpeM")
    t.sleep(5)
    points -= 8
elif color == "Red":
    pg.alert("That color reminds me of blood.")
    wb.open("https://www.youtube.com/watch?v=sMfkODJw30M")
    t.sleep(5)
    points += 5
else:
    pg.alert("Your favorite color is " + color)

game = pg.prompt("What is your favorite video game?")
if game == "Fortnite":
    pg.alert("A lot of people play that game. ")
    wb.open("https://www.youtube.com/watch?v=NXnTQctk9A8")
    t.sleep(5)
    points += 12
elif game == "Call of Duty Black Ops 4":
    pg.alert("I heard that that game is really fun.")
    wb.open("https://www.youtube.com/watch?v=sZZgenIEL9o")
    t.sleep(5)
    points += 8
elif game == "Mario Kart":
    pg.alert("I get first everytime in that game.")
    wb.open("https://www.youtube.com/watch?v=DZ24U4jl1Hg")
    t.sleep(5)
    points += 1
elif game == "2K19":
    pg.alert("I like fortnite better.")
    wb.open("https://www.youtube.com/watch?v=VoKlNyRDwtY")
    t.sleep(5)
    points -= 10
elif game == "Disney Infinity":
    pg.alert("I used to play that game when I was younger.")
    wb.open("https://www.youtube.com/watch?v=Gpa_PNV9Mk0")
    t.sleep(5)
    points += 3
elif game == "Madden 18":
    pg.alert("That video game is so boring!")
    wb.open("https://www.youtube.com/watch?v=KkHzCBVJH_s")
    t.sleep(5)
    points -= 8
else:
    pg.alert("Your favorite video game is " + game)


song = pg.prompt("What is your favorite song? ")

if song == "Little Do You Know":
    pg.alert("That is a really good song!")
    wb.open("https://www.youtube.com/watch?v=L-lp2bejhm4")
    t.sleep(5)
    points += 3
elif song == "ZeZe":
    pg.alert("That song is fire!")
    wb.open("https://www.youtube.com/watch?v=mjaayCARwro")
    t.sleep(5)
    points += 7
elif song == "FeFe":
    pg.alert("That song is trash compared to other songs.")
    wb.open("https://www.youtube.com/watch?v=kC9pJoM33lM")
    t.sleep(5)
    points -= 6
elif song == "Stop Trying To Be God":
    pg.alert("That is my favorite song!")
    wb.open("https://www.youtube.com/watch?v=AcXp7m1g5yE")
    t.sleep(5)
    points += 4
elif song == "New":
    pg.alert("I love remixes!")
    wb.open("https://www.youtube.com/watch?v=aJVYLXYIl1s")
    t.sleep(5)
    points += 2
elif song == "Mine":
    pg.alert("I used to listen to that song all the time!")
    wb.open("https://www.youtube.com/watch?v=QeUFmGLhI_s")
    t.sleep(5)
    points -= 7
else:
    pg.alert("Your favorite song is " + song)


    
pg.alert("You scored: " + str(points))
          

