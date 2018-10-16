# -*- coding: cp1252 -*-
import media
import fresh_tomatoes

avengers = media.Movie("The Avengers",
                       "https://upload.wikimedia.org/wikipedia/" +
                       "en/thumb/f/f9/TheAvengers2012Poster.jpg/" +
                       "300px-TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

freira = media.Movie("A freira",
                     "http://br.web.img3.acsta.net/" +
                     "c_215_290/pictures/18/07/18/21/53/1348208.jpg",
                     "https://www.youtube.com/watch?v=4V44ew-laC4")

venom = media.Movie("Venom",
                    "http://br.web.img2.acsta.net/" +
                    "c_215_290/pictures/18/04/24/16/26/5909399.jpg",
                    "https://www.youtube.com/watch?v=NuYgCOvs4eU")

velozes = media.Movie("Velozes e fuiosos 7",
                      "http://br.web.img1.acsta.net/cx_120_160/" +
                      "b_1_d6d6d6/pictures/15/03/30/21/19/054397.jpg",
                      "https://www.youtube.com/watch?v=hujU0dw6Erk")

resgate = media.Movie("O resgate do soldado Ryan",
                      "http://br.web.img1.acsta.net/cx_120_160/" +
                      "b_1_d6d6d6/medias/nmedia/18/96/07/36/20443914.jpg",
                      "https://www.youtube.com/watch?v=S7Wnyl-lbeU")

gladiador = media.Movie("Gladiador",
                        "http://br.web.img2.acsta.net/cx_120_160/" +
                        "b_1_d6d6d6/medias/nmedia/18/87/29/07/19873973.jpg",
                        "https://www.youtube.com/watch?v=cXg62-t8BWs")

movies = [avengers, freira, venom, velozes, resgate, gladiador]

# cria a page de filmes a partir da lista movies que foi passada como parametro
fresh_tomatoes.open_movies_page(movies)
 

