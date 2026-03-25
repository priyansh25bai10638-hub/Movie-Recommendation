import streamlit as st
import random

movie_database = [  
    # Top Tier (9.0+)
    {
        "title": "The Shawshank Redemption",
        "studio": "Castle Rock Entertainment",
        "director": "Frank Darabont",
        "genre": ["Drama"],
        "imdb_rating": 9.3,
        "description": "Two imprisoned men bond over years, finding solace and redemption through acts of common decency."
    },
    {
        "title": "The Godfather",
        "studio": "Paramount Pictures",
        "director": "Francis Ford Coppola",
        "genre": ["Crime", "Drama"],
        "imdb_rating": 9.2,
        "description": "The aging patriarch of a crime dynasty transfers control to his reluctant son."
    },
    {
        "title": "The Dark Knight",
        "studio": "Warner Bros. Pictures",
        "director": "Christopher Nolan",
        "genre": ["Action", "Crime", "Drama"],
        "imdb_rating": 9.0,
        "description": "Batman faces the Joker who wreaks havoc and chaos on Gotham City."
    },
    {
        "title": "The Godfather Part II",
        "studio": "Paramount Pictures",
        "director": "Francis Ford Coppola",
        "genre": ["Crime", "Drama"],
        "imdb_rating": 9.0,
        "description": "Vito Corleone's early life parallels his son Michael's expansion of the family empire."
    },
    {
        "title": "12 Angry Men",
        "studio": "United Artists",
        "director": "Sidney Lumet",
        "genre": ["Crime", "Drama"],
        "imdb_rating": 9.0,
        "description": "A jury holdout forces his colleagues to reconsider evidence in a murder trial."
    },
    {
        "title": "Schindler's List",
        "studio": "Universal Pictures",
        "director": "Steven Spielberg",
        "genre": ["Biography", "Drama", "History"],
        "imdb_rating": 9.0,
        "description": "Oskar Schindler saves his Jewish workforce from the Nazis during WWII."
    },
    {
        "title": "The Lord of the Rings: The Return of the King",
        "studio": "New Line Cinema",
        "director": "Peter Jackson",
        "genre": ["Action", "Adventure", "Drama"],
        "imdb_rating": 9.0,
        "description": "The fellowship makes a final stand against Sauron's army as Frodo nears Mount Doom."
    },
    
    # High Tier (8.5-8.9)
    {
        "title": "Pulp Fiction",
        "studio": "Miramax",
        "director": "Quentin Tarantino",
        "genre": ["Crime", "Drama"],
        "imdb_rating": 8.9,
        "description": "The lives of mob hitmen, a boxer, and diner bandits intertwine in four tales."
    },
    {
        "title": "The Lord of the Rings: The Fellowship of the Ring",
        "studio": "New Line Cinema",
        "director": "Peter Jackson",
        "genre": ["Action", "Adventure", "Drama"],
        "imdb_rating": 8.9,
        "description": "A hobbit and fellowship set out to destroy the One Ring and save Middle-earth."
    },
    {
        "title": "Forrest Gump",
        "studio": "Paramount Pictures",
        "director": "Robert Zemeckis",
        "genre": ["Drama", "Romance"],
        "imdb_rating": 8.8,
        "description": "Forrest Gump recounts his life story across decades of American history."
    },
    {
        "title": "Inception",
        "studio": "Warner Bros. Pictures",
        "director": "Christopher Nolan",
        "genre": ["Action", "Adventure", "Sci-Fi"],
        "imdb_rating": 8.8,
        "description": "A thief plants an idea into a CEO's mind using dream-sharing technology."
    },
    {
        "title": "The Lord of the Rings: The Two Towers",
        "studio": "New Line Cinema",
        "director": "Peter Jackson",
        "genre": ["Action", "Adventure", "Drama"],
        "imdb_rating": 8.8,
        "description": "Frodo and Sam edge closer to Mordor while the fellowship battles Saruman."
    },
    {
        "title": "Fight Club",
        "studio": "20th Century Fox",
        "director": "David Fincher",
        "genre": ["Drama"],
        "imdb_rating": 8.8,
        "description": "An insomniac office worker forms an underground fight club that evolves."
    },
    {
        "title": "Goodfellas",
        "studio": "Warner Bros. Pictures",
        "director": "Martin Scorsese",
        "genre": ["Biography", "Crime", "Drama"],
        "imdb_rating": 8.7,
        "description": "Henry Hill's life in the mob with his wife and partners Jimmy and Tommy."
    },
    {
        "title": "The Matrix",
        "studio": "Warner Bros. Pictures",
        "director": "The Wachowskis",
        "genre": ["Action", "Sci-Fi"],
        "imdb_rating": 8.7,
        "description": "A hacker learns the true nature of reality and his role against its controllers."
    },
    {
        "title": "One Flew Over the Cuckoo's Nest",
        "studio": "United Artists",
        "director": "Milos Forman",
        "genre": ["Drama"],
        "imdb_rating": 8.7,
        "description": "A criminal rebels against oppressive authorities in a mental institution."
    },
    {
        "title": "Se7en",
        "studio": "New Line Cinema",
        "director": "David Fincher",
        "genre": ["Crime", "Drama", "Mystery"],
        "imdb_rating": 8.6,
        "description": "Two detectives hunt a serial killer using the seven deadly sins as motives."
    },
    {
        "title": "Interstellar",
        "studio": "Paramount Pictures",
        "director": "Christopher Nolan",
        "genre": ["Adventure", "Drama", "Sci-Fi"],
        "imdb_rating": 8.7,
        "description": "Explorers travel through a wormhole to ensure humanity's survival."
    },
    {
        "title": "City of God",
        "studio": "Lumen Films",
        "director": "Fernando Meirelles",
        "genre": ["Crime", "Drama"],
        "imdb_rating": 8.6,
        "description": "Two kids' paths diverge in Rio slums - one photographer, one kingpin."
    },
    {
        "title": "Saving Private Ryan",
        "studio": "DreamWorks",
        "director": "Steven Spielberg",
        "genre": ["Drama", "War"],
        "imdb_rating": 8.6,
        "description": "Soldiers go behind enemy lines to retrieve a paratrooper after Normandy."
    },
    {
        "title": "The Silence of the Lambs",
        "studio": "Orion Pictures",
        "director": "Jonathan Demme",
        "genre": ["Crime", "Drama", "Thriller"],
        "imdb_rating": 8.6,
        "description": "An FBI cadet seeks help from Hannibal Lecter to catch a serial killer."
    },
    {
        "title": "Spirited Away",
        "studio": "Studio Ghibli",
        "director": "Hayao Miyazaki",
        "genre": ["Animation", "Adventure", "Family"],
        "imdb_rating": 8.6,
        "description": "A girl wanders into a spirit world and must work to free her parents."
    },
    
    # Great Tier (8.0-8.4)
    {
        "title": "Star Wars: Episode V - The Empire Strikes Back",
        "studio": "Lucasfilm",
        "director": "Irvin Kershner",
        "genre": ["Action", "Adventure", "Fantasy"],
        "imdb_rating": 8.7,
        "description": "Luke trains with Yoda while his friends are pursued across the galaxy."
    },
    {
        "title": "La La Land",
        "studio": "Summit Entertainment",
        "director": "Damien Chazelle",
        "genre": ["Drama", "Music", "Musical", "Romance"],
        "imdb_rating": 8.0,
        "description": "A musician and actress fall in love while pursuing their dreams in LA."
    },
    {
        "title": "It's a Wonderful Life",
        "studio": "RKO Radio Pictures",
        "director": "Frank Capra",
        "genre": ["Drama", "Family", "Fantasy", "Romance"],
        "imdb_rating": 8.6,
        "description": "An angel shows a compassionate but despairing businessman what life would be like without him."
    },
    {
        "title": "Gladiator",
        "studio": "DreamWorks",
        "director": "Ridley Scott",
        "genre": ["Action", "Adventure", "Drama"],
        "imdb_rating": 8.5,
        "description": "A former Roman General sets out to exact vengeance against the corrupt emperor."
    },
    {
        "title": "The Green Mile",
        "studio": "Warner Bros. Pictures",
        "director": "Frank Darabont",
        "genre": ["Crime", "Drama", "Fantasy"],
        "imdb_rating": 8.6,
        "description": "Death row guards discover a prisoner's miraculous healing abilities."
    },
    {
        "title": "Life Is Beautiful",
        "studio": "Miramax",
        "director": "Roberto Benigni",
        "genre": ["Comedy", "Drama", "Romance"],
        "imdb_rating": 8.6,
        "description": "A Jewish father protects his son from the horrors of a Nazi camp."
    },
    {
        "title": "Star Wars: Episode IV - A New Hope",
        "studio": "Lucasfilm",
        "director": "George Lucas",
        "genre": ["Action", "Adventure", "Fantasy", "Sci-Fi"],
        "imdb_rating": 8.6,
        "description": "Luke Skywalker joins forces with a Jedi Knight to save the galaxy."
    },
    {
        "title": "Terminator 2: Judgment Day",
        "studio": "TriStar Pictures",
        "director": "James Cameron",
        "genre": ["Action", "Sci-Fi"],
        "imdb_rating": 8.6,
        "description": "A cyborg is sent back to protect John Connor from a more advanced terminator."
    },
    {
        "title": "Back to the Future",
        "studio": "Universal Pictures",
        "director": "Robert Zemeckis",
        "genre": ["Adventure", "Comedy", "Sci-Fi"],
        "imdb_rating": 8.5,
        "description": "Marty McFly travels back to 1955 in a time machine built by Doc Brown."
    },
    {
        "title": "Psycho",
        "studio": "Paramount Pictures",
        "director": "Alfred Hitchcock",
        "genre": ["Horror", "Mystery", "Thriller"],
        "imdb_rating": 8.5,
        "description": "A Phoenix secretary embezzles money and goes on the run, checking into a remote motel."
    },
    {
        "title": "The Pianist",
        "studio": "Focus Features",
        "director": "Roman Polanski",
        "genre": ["Biography", "Drama", "Music", "War"],
        "imdb_rating": 8.5,
        "description": "A Polish Jewish musician struggles to survive the destruction of the Warsaw ghetto."
    },
    {
        "title": "Parasite",
        "studio": "CJ Entertainment",
        "director": "Bong Joon Ho",
        "genre": ["Drama", "Thriller"],
        "imdb_rating": 8.5,
        "description": "Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan."
    },
    {
        "title": "Whiplash",
        "studio": "Bold Films",
        "director": "Damien Chazelle",
        "genre": ["Drama", "Music"],
        "imdb_rating": 8.5,
        "description": "A promising young drummer enrolls at a cut-throat music conservatory."
    },
    {
        "title": "The Lion King",
        "studio": "Walt Disney Pictures",
        "director": "Roger Allers",
        "genre": ["Animation", "Adventure", "Drama", "Family"],
        "imdb_rating": 8.5,
        "description": "Lion prince Simba and his father are targeted by his bitter uncle."
    },
    {
        "title": "The Departed",
        "studio": "Warner Bros. Pictures",
        "director": "Martin Scorsese",
        "genre": ["Crime", "Drama", "Thriller"],
        "imdb_rating": 8.5,
        "description": "An undercover cop and a mole in the police attempt to identify each other."
    },
    {
        "title": "American History X",
        "studio": "New Line Cinema",
        "director": "Tony Kaye",
        "genre": ["Crime", "Drama"],
        "imdb_rating": 8.5,
        "description": "A former neo-nazi skinhead tries to prevent his younger brother from going down the same wrong path."
    },
    
    # Excellent Tier (8.0-8.4 continued)
    {
        "title": "The Prestige",
        "studio": "Warner Bros. Pictures",
        "director": "Christopher Nolan",
        "genre": ["Drama", "Mystery", "Sci-Fi", "Thriller"],
        "imdb_rating": 8.5,
        "description": "Two stage magicians engage in a battle to create the ultimate illusion."
    },
    {
        "title": "Memento",
        "studio": "Newmarket Films",
        "director": "Christopher Nolan",
        "genre": ["Mystery", "Thriller"],
        "imdb_rating": 8.4,
        "description": "A man with short-term memory loss attempts to track down his wife's murderer."
    },
    {
        "title": "Casablanca",
        "studio": "Warner Bros. Pictures",
        "director": "Michael Curtiz",
        "genre": ["Drama", "Romance", "War"],
        "imdb_rating": 8.5,
        "description": "A cynical expatriate American café owner in Casablanca struggles to decide whether or not to help his former lover and her fugitive husband escape."
    },
    {
        "title": "Grave of the Fireflies",
        "studio": "Studio Ghibli",
        "director": "Isao Takahata",
        "genre": ["Animation", "Drama", "War"],
        "imdb_rating": 8.5,
        "description": "A young boy and his little sister struggle to survive in Japan during WWII."
    },
    {
        "title": "Aliens",
        "studio": "20th Century Fox",
        "director": "James Cameron",
        "genre": ["Action", "Horror", "Sci-Fi"],
        "imdb_rating": 8.4,
        "description": "Ellen Ripley is rescued after drifting in space, only to face more alien terror."
    },
    {
        "title": "Once Upon a Time in the West",
        "studio": "Paramount Pictures",
        "director": "Sergio Leone",
        "genre": ["Western"],
        "imdb_rating": 8.5,
        "description": "Epic tale of a mysterious stranger and revenge against a railroad owner."
    },
    {
        "title": "Cinema Paradiso",
        "studio": "Tiffen",
        "director": "Giuseppe Tornatore",
        "genre": ["Drama", "Romance"],
        "imdb_rating": 8.5,
        "description": "A famous film director remembers his childhood at the Cinema Paradiso."
    },
    {
        "title": "Das Boot",
        "studio": "Bavaria Film",
        "director": "Wolfgang Petersen",
        "genre": ["Drama", "War"],
        "imdb_rating": 8.4,
        "description": "The story of a German U-boat crew during WWII and their desperate mission."
    },
    {
        "title": "The Lives of Others",
        "studio": "Weltfilm",
        "director": "Florian Henckel von Donnersmarck",
        "genre": ["Drama", "Thriller"],
        "imdb_rating": 8.4,
        "description": "In 1984 East Berlin, an agent of the secret police begins to question his assignment."
    },
    {
        "title": "Django Unchained",
        "studio": "Weinstein Company",
        "director": "Quentin Tarantino",
        "genre": ["Drama", "Western"],
        "imdb_rating": 8.5,
        "description": "A freed slave teams with a German bounty hunter to find his wife before her buyer."
    },
    {
        "title": "The Shining",
        "studio": "Warner Bros. Pictures",
        "director": "Stanley Kubrick",
        "genre": ["Drama", "Horror"],
        "imdb_rating": 8.4,
        "description": "A family heads to an isolated hotel for the winter where a sinister presence influences the father into violence."
    },
    {
        "title": "WALL·E",
        "studio": "Pixar",
        "director": "Andrew Stanton",
        "genre": ["Animation", "Adventure", "Family", "Sci-Fi"],
        "imdb_rating": 8.4,
        "description": "In the distant future, a small waste-collecting robot finds a new purpose."
    },
    {
        "title": "Paths of Glory",
        "studio": "United Artists",
        "director": "Stanley Kubrick",
        "genre": ["Drama", "War"],
        "imdb_rating": 8.4,
        "description": "A French general tries to court-martial three soldiers for cowardice during WWI."
    },
    {
        "title": "The Incredibles",
        "studio": "Pixar",
        "director": "Brad Bird",
        "genre": ["Animation", "Action", "Adventure", "Family"],
        "imdb_rating": 8.0,
        "description": "A family of undercover superheroes balance their destroyed lives with their love."
    },
    {
        "title": "Braveheart",
        "studio": "Paramount Pictures",
        "director": "Mel Gibson",
        "genre": ["Biography", "Drama", "History"],
        "imdb_rating": 8.3,
        "description": "Scottish warrior William Wallace leads his countrymen in a rebellion against England."
    },
    {
        "title": "Princess Mononoke",
        "studio": "Studio Ghibli",
        "director": "Hayao Miyazaki",
        "genre": ["Animation", "Action", "Adventure", "Fantasy"],
        "imdb_rating": 8.3,
        "description": "A prince becomes caught in a war between forest gods and an iron mining town."
    },
    {
        "title": "Joker",
        "studio": "Warner Bros. Pictures",
        "director": "Todd Phillips",
        "genre": ["Crime", "Drama", "Thriller"],
        "imdb_rating": 8.4,
        "description": "A mentally troubled stand-up comedian is driven insane and becomes a psychopathic Joker."
    },
    {
        "title": "Avengers: Infinity War",
        "studio": "Marvel Studios",
        "director": "Anthony Russo",
        "genre": ["Action", "Adventure", "Sci-Fi"],
        "imdb_rating": 8.4,
        "description": "The Avengers and their allies must be willing to sacrifice all in an attempt to defeat Thanos."
    },
    {
        "title": "Raiders of the Lost Ark",
        "studio": "Lucasfilm",
        "director": "Steven Spielberg",
        "genre": ["Action", "Adventure"],
        "imdb_rating": 8.4,
        "description": "Archaeologist Indiana Jones races against Nazis to find the Ark of the Covenant."
    },
    {
        "title": "Toy Story",
        "studio": "Pixar",
        "director": "John Lasseter",
        "genre": ["Animation", "Adventure", "Comedy", "Family"],
        "imdb_rating": 8.3,
        "description": "A cowboy doll is profoundly threatened and jealous when a new spaceman toy arrives."
    },
    {
        "title": "Reservoir Dogs",
        "studio": "Miramax",
        "director": "Quentin Tarantino",
        "genre": ["Crime", "Drama", "Thriller"],
        "imdb_rating": 8.3,
        "description": "After a simple jewelry heist goes terribly wrong, the surviving criminals begin to suspect one of them is a police informant."
    },
    {
        "title": "Amadeus",
        "studio": "Orion Pictures",
        "director": "Milos Forman",
        "genre": ["Biography", "Drama", "Music"],
        "imdb_rating": 8.4,
        "description": "The life, success and troubles of Wolfgang Amadeus Mozart, as told by Antonio Salieri."
    },
    {
        "title": "Good Will Hunting",
        "studio": "Miramax",
        "director": "Gus Van Sant",
        "genre": ["Drama", "Romance"],
        "imdb_rating": 8.3,
        "description": "A janitor at MIT with genius mathematical skills has to battle his personal demons."
    },
    {
        "title": "Requiem for a Dream",
        "studio": "Artisan Entertainment",
        "director": "Darren Aronofsky",
        "genre": ["Drama"],
        "imdb_rating": 8.3,
        "description": "The drug-induced utopias of four Coney Island people implode when their addictions become stronger."
    },
    {
        "title": "Inglourious Basterds",
        "studio": "Weinstein Company",
        "director": "Quentin Tarantino",
        "genre": ["Adventure", "Drama", "War"],
        "imdb_rating": 8.4,
        "description": "In Nazi-occupied France during World War II, Jewish soldiers hunt Nazis."
    },
    {
        "title": "Singin' in the Rain",
        "studio": "MGM",
        "director": "Stanley Donen",
        "genre": ["Comedy", "Musical", "Romance"],
        "imdb_rating": 8.3,
        "description": "A silent film star falls for a chorus girl just as he and his studio must transition to talking pictures."
    },
    {
        "title": "2001: A Space Odyssey",
        "studio": "MGM",
        "director": "Stanley Kubrick",
        "genre": ["Adventure", "Sci-Fi"],
        "imdb_rating": 8.3,
        "description": "After discovering a mysterious artifact buried on the Moon, humanity embarks on a quest to Jupiter."
    },
    {
        "title": "Eternal Sunshine of the Spotless Mind",
        "studio": "Focus Features",
        "director": "Michel Gondry",
        "genre": ["Drama", "Romance", "Sci-Fi"],
        "imdb_rating": 8.3,
        "description": "When their relationship turns sour, a couple undergoes a procedure to have each other erased from their memories."
    },
    {
        "title": "The Hunt",
        "studio": "Magnolia Pictures",
        "director": "Thomas Vinterberg",
        "genre": ["Drama"],
        "imdb_rating": 8.3,
        "description": "A teacher lives a lonely life, all the while struggling over his son’s custody, until a lie tears his world apart."
    },
    {
        "title": "Citizen Kane",
        "studio": "RKO Radio Pictures",
        "director": "Orson Welles",
        "genre": ["Drama", "Mystery"],
        "imdb_rating": 8.3,
        "description": "Following the death of a publishing tycoon, reporters scramble to uncover the meaning of his final utterance."
    },
    {
        "title": "Lawrence of Arabia",
        "studio": "Columbia Pictures",
        "director": "David Lean",
        "genre": ["Adventure", "Biography", "Drama", "History"],
        "imdb_rating": 8.3,
        "description": "The story of T.E. Lawrence, the English officer who successfully united and led the diverse, often warring, Arab tribes during World War I."
    },
    {
        "title": "North by Northwest",
        "studio": "MGM",
        "director": "Alfred Hitchcock",
        "genre": ["Action", "Adventure", "Mystery", "Thriller"],
        "imdb_rating": 8.3,
        "description": "A New York City advertising executive goes on the run after being mistaken for a government agent by a group of foreign spies."
    },
    {
        "title": "Full Metal Jacket",
        "studio": "Warner Bros. Pictures",
        "director": "Stanley Kubrick",
        "genre": ["Drama", "War"],
        "imdb_rating": 8.3,
        "description": "A pragmatic U.S. Marine observes the dehumanizing effects the Vietnam War has on his fellow recruits from their brutal boot camp training to the bloody street fighting."
    },
    {
        "title": "The Apartment",
        "studio": "United Artists",
        "director": "Billy Wilder",
        "genre": ["Comedy", "Drama"],
        "imdb_rating": 8.3,
        "description": "A man tries to rise in his company by letting its executives use his apartment for trysts, but complications and a romance of his own ensue."
    },
    {
        "title": "Scarface",
        "studio": "Universal Pictures",
        "director": "Brian De Palma",
        "genre": ["Crime", "Drama"],
        "imdb_rating": 8.3,
        "description": "In 1980s Miami, a determined Cuban immigrant takes over a drug cartel and succumbs to greed."
    },
    {
        "title": "A Beautiful Mind",
        "studio": "Universal Pictures",
        "director": "Ron Howard",
        "genre": ["Biography", "Drama"],
        "imdb_rating": 8.2,
        "description": "Mathematician John Nash battles schizophrenia while making Nobel Prize-winning discoveries."
    },
    {
        "title": "The Wolf of Wall Street",
        "studio": "Paramount Pictures",
        "director": "Martin Scorsese",
        "genre": ["Biography", "Comedy", "Crime", "Drama"],
        "imdb_rating": 8.2,
        "description": "Based on the true story of Jordan Belfort, from his rise to a wealthy stock-broker to his fall."
    },
    {
        "title": "The Great Dictator",
        "studio": "United Artists",
        "director": "Charlie Chaplin",
        "genre": ["Comedy", "Drama", "War"],
        "imdb_rating": 8.4,
        "description": "Dictator Adenoid Hynkel tries to expand his empire while a poor Jewish barber tries to avoid persecution."
    }
]

# Rest of the code remains exactly the same...
all_genres = set()
for movie in movie_database:
    for genre in movie["genre"]:
        all_genres.add(genre)
dynamic_genre_list = sorted(list(all_genres))
dynamic_studio_list = ["Any"] + sorted(list(set(movie["studio"] for movie in movie_database)))
dynamic_director_list = ["Any"] + sorted(list(set(movie["director"] for movie in movie_database)))

def get_random_recommendation(filtered_list):
    if len(filtered_list) == 0:
        return None
    return random.choice(filtered_list)

def master_movie_filter(database, requested_genres, min_imdb, requested_studio, requested_director):
    matching_movies = []
    
    request_set = set(requested_genres)
    
    for movie in database:
        is_match = True
        
        if len(request_set) > 0:
            movie_genre_set = set(movie["genre"])
            if not request_set.issubset(movie_genre_set):
                is_match = False
                
        if movie["imdb_rating"] < min_imdb:
            is_match = False
         
        if requested_studio != "Any":
            if movie["studio"] != requested_studio:
                is_match = False
                
        if requested_director != "Any":
            if movie["director"] != requested_director:
                is_match = False
            
        if is_match == True:
            matching_movies.append(movie)
            
    return matching_movies

st.title("🎬 Movie Recommender")
st.write("Decision fatigue? Let the algorithm choose your next binge-watch!")

col1, col2 = st.columns(2)

with col1:
    user_genres = st.multiselect("Select Genres:", dynamic_genre_list)
    user_min_rating = st.slider("Minimum IMDb Rating:", 0.0, 10.0, 8.0, 0.1)

with col2:
    user_studio = st.selectbox("Preferred Studio:", dynamic_studio_list)
    user_director = st.selectbox("Specific Director:", dynamic_director_list)

if st.button("🎲 Get Recommendation"):
    results = master_movie_filter(movie_database, user_genres, user_min_rating, user_studio, user_director)
    
    st.divider() 
    
    if len(results) == 0:
        st.error("No movies matched all of those exact filters! Try broadening your search.")
    else:
        final_pick = get_random_recommendation(results)
        
        st.success("Here is your perfect recommendation!")
        st.subheader(f"🎥 {final_pick['title']}")
        st.write(f"**⭐ IMDb Rating:** {final_pick['imdb_rating']}")
        st.write(f"**🏢 Studio:** {final_pick['studio']}")
        st.write(f"**👤 Director:** {final_pick['director']}")
    
        st.write("---")
        st.write(f"**📖 Synopsis:** {final_pick['description']}")
        st.balloons()
