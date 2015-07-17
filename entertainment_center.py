# -*- coding: utf-8 -*-
import front_end_creator
import media

agni2 = media.Movie("অগ্নী ২",
                        "https://fbcdn-sphotos-h-a.akamaihd.net/hphotos-ak-xpf1/v/t1.0-9/11200913_457346227759668_6913624632860949138_n.jpg?oh=1dc0cc4c93155fba715712844699ebd6&oe=561CF74F&__gda__=1443892773_164b7e025cc548c1faf835d1dac7a1c0",
                        "https://www.youtube.com/watch?v=izZU6bI96e8")

warning = media.Movie("ওয়ার্নিং",
                      "https://bdmusiccafe.files.wordpress.com/2014/12/warning-2015-bangla-movie-poster.jpg",
                      "https://www.youtube.com/watch?v=oyg3cTp5KTE")

podmoPatarJol = media.Movie("পদ্ম পাতার জল",
                      "http://podmopatarjol.com/wp-content/uploads/2015/05/movie-gallery-PPJ-21.png",
                      "https://www.youtube.com/watch?v=BkUIP-DGq28")

loveMarrage = media.Movie("লাভ ম্যারেজ",
                      "https://scontent-sin1-1.xx.fbcdn.net/hphotos-xat1/v/t1.0-9/11249021_1753418728218531_340966462253821886_n.jpg?oh=d3940f970f83fcaea1a2b9e48d174f51&oe=561DBCEB",
                      "https://www.youtube.com/watch?v=EI2ZdVPuzPI")

musafir = media.Movie("মুসাফির",
                      "https://scontent-sin1-1.xx.fbcdn.net/hphotos-xtp1/v/l/t1.0-9/11188168_384822508377483_7921731828245799131_n.jpg?oh=5c18a906136f61efeedd99aa1f7a8ed5&oe=56105046",
                      "https://www.youtube.com/watch?v=5zjTBJfx9Mg")

#print (toy_story.storyline)
#Agni2.show_trailer()

chuyedileMon = media.Movie("ছুঁয়ে দিলে মন",
                      "https://scontent-sin1-1.xx.fbcdn.net/hphotos-xpa1/v/t1.0-9/10426331_392150327656857_6590299574975895935_n.png?oh=d957aaaee25dcf1ffc161dbea7f3fcae&oe=561B2B24",
                      "https://www.youtube.com/watch?v=seIFtpSUC-s")

#musafir.show_trailer()

movies = [agni2,podmoPatarJol,loveMarrage, musafir,chuyedileMon, warning]

front_end_creator.open_movies_page(movies)
