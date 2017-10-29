#!/usr/bin/python

import cgi, cgitb 

tweet=""

file = open('tweets.txt', 'r')
text = file.read()
file.close()

tweet=text

print(text)

print ("Content-type:text/html\r\n\r\n")


print ("""

	<!DOCTYPE html>
<html>
<head>
	<title>Sentiment Analysys</title>
</head>
<body style="background-color:#4ab3f4">
<div id="header-image" style="position:absolute;top:0">
<img src="twitter.png">
</div>
<div id="bar-graph" style="position:absolute;top:10vw;left:0.6vw;">
<img src="bar.png" height=500px>
</div>
<div id="pie-graph" style="position:absolute;top:10vw;right:12vw;">
<img src="pie.png"  height=500px>
</div>
<div id="hashtag" style="position:fixed;top:60%;left:40%; transform: translateX(-50%) translateY(-50%);height: 100px;width: 500px;">
<img src="Hashtag Bar Graph.png"  height=500px>
</div>


<div id="tweet" style="position:fixed;top:25%;left:45%; transform: translateX(-50%) translateY(-50%);height: 100px;width: 500px;">
<strong>
<span style="text-decoration: underline;">Some random tweets: </span> <br><br>
""")

print(tweet)

print("""</strong></div>
</body>
</html>

""")

