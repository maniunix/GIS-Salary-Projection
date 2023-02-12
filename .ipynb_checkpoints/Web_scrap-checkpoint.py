# webbrowser Comes with Python and opens a browser to a specific page.

# requests Downloads files and web pages from the internet.

# bs4 Parses HTML, the format that web pages are written in.

# selenium Launches and controls a web browser. The selenium module is able to fill in forms and simulate mouse clicks in this browser.

import webbrowser
webbrowser.open('https://inventwithpython.com/') #This will open the Web browser page with the specified URL


import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()  #This is just for program to halt if a bad download occurs
playfile = open('RomeoAndJuliet.txt','wb')  #'wb' means write binary

#To write the web page to a file, you can use a for loop with the Response object’s iter_content() method.

#The iter_content() method returns “chunks” of the content on each iteration through the loop. Each chunk is of the bytes data type, and you get to specify how many bytes each chunk will contain. One hundred thousand bytes is generally a good size, so pass 100000 as the argument to iter_content().

for chunk in res.iter_content(100000):
    playfile.write(chunk)

playfile.close()

# #To summarize it 
# Call requests.get() to download the file.
# Call open() with 'wb' to create a new file in write binary mode.
# Loop over the Response object’s iter_content() method.
# Call write() on each iteration to write the content to the file.
# Call close() to close the file.