if __name__ == '__main__':
    love_connections = [("Lysander", "Helena"), ("Hermia", "Lusander"),
                        ("Demetrius", "Hermia"), ("Helena","demetrius"),
    ("Titania","Oberon"),("Oberon", "TItania"),("Puck", None), ("Lysander", "Puck")]

    # directed adjacency lsit
    adj_list = {}

    #{"Lysander":[Helena, puck]}
    for source, target in love_connections:
        if source in adj_list:
            adj_list[source].append(target)
        else:
            adj_list[source] = [target]
    '''
    to print vaues of lysander
    Brute force approach wil be
    '''
    for source, target in love_connections:
        if source == "Lysander":
            print(target)
    '''
    optimal solution will be 
    '''
    for neighbour in adj_list["Lysander"]:
        print(neighbour)