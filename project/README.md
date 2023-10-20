Holy Book Comparison
#### Video Demo:  <URL HERE>
    You can visit this website at http://www.holybookcompare.com/.
    This website lets you compare the three major holy books from the world's three biggest religions: Christianity, Islam, and Hinduism.
These books are the Bible, the Quran, and the Bhagavad Gita. There are two major sections: You can search for a keyword or you can search
for a specific book/chapter/verse.
    Let's look at the former. If you search for the word "dog", it will print out all the verses in these books that contain that word.
If you so wish, you can select just the results from one of the specific books. Notice that the results are paginated, with a default of
20 results per page, or rpp. You can change that number to whichever you wish. So if you have 10,000 results and you want to view one per page,
well, nobody is going to stop you. Also, you have a highlighter, which will highlight your query in the results. Click to highlight and
click again to dehighlight. Finally, you will receive an error if your query or rpp is blank or invalid.
    Let's look at the latter. You can get results for the Bible by inputting: a book, a book and a chapter, or a book, chapter, and verse.
You can get results for the Quran by inputting: a surah or a surah and a verse. You can get results for the Bhagavad Gita by inputting:
a chapter or a chaper and a verse. Any query that does not make sense will result in an error. For example, if you search for surah 1 and
verse 3, your query is valid. However, if you search for a bible chapter of 6 and a bible verse of 10, your query is invalid. This section
includes the pagination and highlighting functions contained above.
    Now let's look at the files. Cache-dir stores the cached files. In my databases folder, I have the csv for the Bhagavad Gita
which I converted into a sqlite file. I also have the sqlite files for the other two books. Flask_session supports the server-side session.
My static folder contains all the pictures and the stylesheet. App.py lets me run python scripts. Common.py lets me enable caching.
    Now let's look at the templates folder. About.html repeats much of what is stated here. Layout.html contains the elements shared by
the entire project. Home.html contains elements that are displayed or removed depending on the situation. It can display the
starting message page as well as the search results for all three books. Bible.html displays the Bible search results, Quran.html
does the same for the Quran, and Bhagavad.html does the same for the Bhagavad Gita. Search.html lets you search for a keyword.
Verse.html lets you search for a specific book/chapter/verse.
    Why did I choose this project? At first, I wanted to make a site similar to BibleGateway, where you search for a verse and you get
results from 20 different Bibles. I thought that such a site had already been made multiple times and probably better than I could.
So I decided to do something more unique. I have not seen something like this on the Internet. I hope that it is useful.