import webapp2
import media
import fresh_tomatoes

movies = [
  media.Movie(
    'White Chicks',
    'Two police officers who are not at all caucasian or even female go '
    'undercover as caucasian females in order to bring down a crime lord.',
    'http://upload.wikimedia.org/wikipedia/en/2/2b/White_chicks.jpg',
    'https://www.youtube.com/watch?v=p6V25aqQblM'
  ),
  media.Movie(
    'I Am Gonna Git You Sucka',
    'A pure revenge story. A brother returns from the army to find his older '
    'brother dead under mysterious circumstances.',
    'http://upload.wikimedia.org/wikipedia/en/3/3a/I%27m_Gonna_Git_You_Sucka_'
    'film.jpg',
    'https://www.youtube.com/watch?v=E97wjtbiad0'
  ),
  media.Movie(
    'Ace Ventura: Pet Detective',
    'A detective specializing in animal investigation and recovery cases is '
    'drawn into a complex plot and web of intrigue.',
    'http://upload.wikimedia.org/wikipedia/en/8/84/Ace_ventura_pet_'
    'detective.jpg',
    'https://www.youtube.com/watch?v=cXcH0f2B2vA'
  ),
  media.Movie(
    'Double Take',
    'A successful investment banker is framed for the crimes of a Mexican '
    'drug cartel. All of them. He recruits a professional smuggler to get him'
    ' to a safe location. But all is decidedly not as it seems!',
    'http://upload.wikimedia.org/wikipedia/en/f/fd/Double_Take_%282001%29_'
    'film_poster.jpg',
    'https://www.youtube.com/watch?v=3n8cJ6Kl8vc'
  ),
  media.Movie(
    'Snakes on a Plane',
    'A suspenseful tail about one man trying to save a planeful of passengers'
    ' from a slithering, scaly squad of intruders.',
    'http://upload.wikimedia.org/wikipedia/en/4/41/SOAP_poster.jpg',
    'https://www.youtube.com/watch?v=u6Squ9a2kO4'
  ),
  media.Movie(
    'Deuce Bigalow Male Gigolo',
    'A lonely man, on the cusp of middle-age and bordering on depression, '
    'seizes an unexpected opportunity to live out his fantasies.',
    'http://upload.wikimedia.org/wikipedia/en/8/82/Deucebigalowmale'
    'gigolotp.jpg',
    'https://www.youtube.com/watch?v=wk_19DT6y9Y'
  )
]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(fresh_tomatoes.open_movies_page(movies))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
