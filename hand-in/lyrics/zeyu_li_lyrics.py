""" Lyrics Extracter 0.1

Course: CS 30
Period: 3
Date created: April 29, 2019
Date completed: April 30, 2019
By: Andrew Li
Extracting song lyrics from string and out outputting as a text file
"""


def main():

    lyrics = """
Yo listen up, here's the story
About a little guy that lives in a blue world
And all day and all night and everything he sees is just blue
Like him, inside and outside
Blue his house with a blue little window
And a blue Corvette
And everything is blue for him
And himself and everybody around
'Cause he ain't got nobody to listen
I'm blue da ba dee da ba daa
Da ba dee da ba daa, da ba dee da ba daa, da ba dee da ba daa
Da ba dee da ba daa, da ba dee da ba daa, da ba dee da ba daa
I'm blue da ba dee da ba daa
Da ba dee da ba daa, da ba dee da ba daa, da ba dee da ba daa
Da ba dee da ba daa, da ba dee da ba daa, da ba dee da ba daa
I have a blue house with a blue window
Blue is the color of all that I wear
Blue are the streets and all the trees are too
I have a girlfriend and she is so blue
Blue are the people here that walk around
Blue like my Corvette, it's in and outside
Blue are the words I say and what I think
Blue are the feelings that live inside me
I'm blue da ba dee da ba daa
Da ba dee da ba daa, da ba dee da ba daa, da ba dee da ba daa
Da ba dee da ba daa, da ba dee da ba daa, da ba dee da ba daa
I'm blue da ba dee da ba daa
Da ba dee da ba daa, da ba dee da ba daa, da ba dee da ba daa
Da ba dee da ba daa, da ba dee da ba daa, da ba dee da ba daa
I have a blue house with a blue window
Blue is the color of all that I wear
Blue are the streets and all the trees are too
I have a girlfriend and she is so blue
Blue are the people here that walk around
Blue like my Corvette, it's in and outside
Blue are the words I say and what I think
Blue are the feelings that live inside me
I'm blue da ba dee da ba daa
Da ba dee da ba daa, da ba dee da ba daa, da ba dee da ba daa
Da ba dee da ba daa, da ba dee da ba daa, da ba dee da ba daa
I'm blue da ba dee da ba daa
Da ba dee da ba daa, da ba dee da ba daa, da ba dee da ba daa
Da ba dee da ba daa, da ba dee da ba daa, da ba dee da ba daa
"""
    with open('lyrics.txt', 'w') as f:
        f.writelines(lyrics)


# system calls name
if __name__ == "__main__":
    main()
