class Movies:
    def __init__(self, title, year, genre, viewnumber = 0):
        self.title = title
        self.year = year
        self.genre = genre
        self.viewnumber = viewnumber

    def play(self, step=1):
        self.viewnumber += step

    def __str__(self):
        return f'{self.title} {self.year}'

class Series(Movies):
    def __init__(self, episodenumber, seasonnumber, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.episodenumber = episodenumber
        self.seasonnumber = seasonnumber

    def __str__(self):
        return f'{self.title} {self.year} {self.genre} {self.seasonnumber:02}E{self.seasonnumber:02} Liczba odtworzeń: {self.viewnumber}'

m1 = Movies(title="The Shawshank Redemption", year="1994", genre="Drama")
m2 = Movies(title="Intouchables", year="2011", genre="Comedy/Biographical/Drama")
m3 = Movies(title="The Green Mile", year="1999", genre="Drama")
m4 = Movies(title="The Godfather", year="1972", genre="Drama/Gangster")
m5 = Movies(title="12 Angry Men", year="1957", genre="Court drama")
s1 = Series(title="Our Planet", year="2019", genre="Documentary, Nature", episodenumber="01", seasonnumber="01")
s2 = Series(title="Chernobyl", year="2019", genre="Drama",  episodenumber="05", seasonnumber="01")
s3 = Series(title="Game of Thrones", year="2013", genre="Drama, Fantasy, Adventure", episodenumber="01", seasonnumber="03")
s4 = Series(title="Breaking Bad", year="2012", genre="Drama, Crime", episodenumber="01", seasonnumber="01")
s5 = Series(title="Band of Brothers", year="2001", genre="War drama", episodenumber="09", seasonnumber="01")
