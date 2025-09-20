
def main(): 
    # Dictonary should always be at the top of the main function, becasue we can use it in the various function as we wish. 

    my_detail = dict(
        full_name = 'Pujan Magar',
        first_name = 'Pujan',
        last_name = 'Magar',
        student_id = 10319564,
        birth_place = 'Nepal',
        hobby = ['Rap', 'Singing', 'Dancing', 'Swiming'],
        fav_anime = dict(
            anime_1 = dict( name = 'One Piece',
                           genre = 'Adventure'),
            anime_2 = dict(name = 'Naruto',
                           genre = 'Adventure and action')
        ),  
    )      

    # Let's pring some of the basics sentences 
    print(f'My name is {my_detail["full_name"]}, but you can call me {my_detail["first_name"]}')
    print(f'These are the lists of my hobby: {my_detail["hobby"]}')
    print(f'I like the anime that has the genre: {my_detail["fav_anime"]['anime_1']['genre']}')

    # Let's print the list of movies 
    print(f'{my_detail["fav_anime"]}')

    # Making the new hobby
    new_hobby = ['Playin games']
    my_detail['hobby'].extend(new_hobby)
    print(my_detail['hobby'])

    # Makin the new lovely anime with it's genre and adding to the structur e

    
    # Adding the dictionary is different that the list so, we will do this 

    new_anime = f'anime{len(my_detail['fav_anime']) + 1}'   # I am adding the new anime directly to the dictionary. 

    my_detail['fav_anime'][new_anime] = dict(
        title = 'Bleach',
        genre = 'Fuck up') 
    
    # Print some new items
    print(my_detail['fav_anime'])

if __name__ == '__main__':
    main() 