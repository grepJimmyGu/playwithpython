import media_inherited as media
import fresh_tomatoes

toy_story_video = media.Video("Toy Story",
                        "A story of a boy and his toys that come to life")

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

Pirates_of_the_Caribbean = media.Movie("Pirates_of_the_Caribbean",
                                       "Thrust into an all-new adventure, a down-on-his-luck Capt. Jack Sparrow (Johnny Depp) feels the winds of ill-fortune blowing even more strongly when deadly ghost sailors led by his old nemesis, the evil Capt. Salazar (Javier Bardem), escape from the Devil's Triangle. Jack's only hope of survival lies in seeking out the legendary Trident of Poseidon, but to find it, he must forge an uneasy alliance with a brilliant and beautiful astronomer and a headstrong young man in the British navy",
                                       "https://upload.wikimedia.org/wikipedia/en/2/21/Pirates_of_the_Caribbean%2C_Dead_Men_Tell_No_Tales.jpg",
                                       "https://www.youtube.com/watch?v=fdK_vAd0EeI")

Friends = media.TvShow("Friends",
                       "A story about six friends living in a NYC apartment for 10 years",
                       "http://img2.tvtome.com/i/u/0aa3afb3cbe3468fc6e43e50070b0810.png",
                       "https://www.youtube.com/watch?v=8mP5xOg7ijs",
                       "https://en.wikipedia.org/wiki/Friends#Season_1",
                       "https://en.wikipedia.org/wiki/List_of_Friends_episodes",
                       "https://www.youtube.com/channel/UCSnTDhFDmcbB3lkFWrIi8MA")

#print(media.Video.__doc__)
#print(media.Movie.__doc__)
#print(toy_story_video.storyline)
#print(toy_story.storyline)
# print(Pirates_of_the_Caribbean.storyline)
# Pirates_of_the_Caribbean.poster()
# Pirates_of_the_Caribbean.show_trailer()

movies = [toy_story, Pirates_of_the_Caribbean, Friends]
fresh_tomatoes.open_movies_page(movies)


#print(Friends.title)
#print(Friends.storyline)
#Friends.show_trailer()
#Friends.poster()
#Friends.get_local_listings()
#Friends.get_seasons()
#Friends.get_episodes()








