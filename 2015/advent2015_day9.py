from pprint import pprint
import re
from debug import debug_open

INI_FILE="2015\\advent2015_day9-input.txt"

debug_open(INI_FILE )
total_encoded=0
total_code=0



city_src='(?P<src>\\w+)'
city_dst='(?P<dst>\\w+)'
distance='(?P<dist>\\d+)'
regex=re.compile(rf"{city_src}\s+to\s+{city_dst}\s+=\s+{distance}")

def init_graph( graf:dict, src, dst, dist ):
    tmp= int(dist)
    if src in graph:
        graf[src][dst]=tmp
    else:
        graf[src]={dst:tmp}
    return tmp


def generate_travel ( dist_graph:dict, cities_available:list ,  record_dist:int):
    best_travel = None 
    cache={}
    for first_city in cities_available:
        cities=cities_available.copy()
        cities.remove(first_city)
        (full_dist, full_travel) = generate_city_next( dist_graph, cache, [first_city], cities,  record_dist, 0 )
        if ( full_dist < record_dist ):
            print(f" Changing {full_dist=} {record_dist=}")
            record_dist = full_dist
            best_travel=full_travel
    
    return (record_dist, best_travel)


def generate_city_next(  dist_graph:dict,cache:dict,cities_visited:list, cities_available:list,  record_dist:int, current_dist:int):
    best_travel=None 
    current_city =  cities_visited[-1]
    #first_city=cities_visited[1]
    
    for next_city in cities_available :
        #mesure the dist addition
        add_dist=dist_graph[current_city][next_city]
        new_dist = current_dist+add_dist 

        if ( new_dist < record_dist ):
            cities=cities_available.copy()
            cities.remove(next_city)

            count=len(cities)
            if count>0:  #verifier  la condition d'arret 
                travel = cities_visited.copy()
                travel.append(next_city)
                (full_dist, full_travel) = generate_city_next(dist_graph,cache, travel, cities, record_dist, new_dist )
                if ( full_dist < record_dist ) :
                    record_dist=full_dist
                    best_travel = full_travel
                    print(f" changing {full_dist=} {record_dist=}")
                    pprint(  full_travel)
            

    return (record_dist, best_travel)







graph={}
horizon=0
with open(INI_FILE, "r") as f:
    for line in f:
        string = line.strip()
        match = regex.fullmatch( string )
        if not match:
            print ("line ignored ", string)
            continue

        capture=match.groupdict()
        horizon+=init_graph(graph,capture['src'],capture['dst'],capture['dist'])
        horizon+=init_graph(graph,capture['dst'],capture['src'],capture['dist'])

    pprint( graph )
    keys = graph.keys()
    visit=[]
    cities =list(graph.keys())

    (distance, travel)=generate_travel( graph , cities,horizon )
        
    print(f"{distance=}")
    pprint(travel )

        






        



















