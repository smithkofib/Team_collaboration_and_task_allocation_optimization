def locate_card(card, query):
    #Create a variable postion with the value 0
    position = 0
    
    # Set up a loop for repetation
    while position < len(card):

        # Chrck if element at the current position matches the query
        if(card[position] == query):
            print(position)
            # Answer found! return and exist;
            return position
        
        # Increament the position
        position +=1

    # Number not found, return -1
    return -1

    
    
    

test = []
test.append({
    "input":{
        "card" :[12,10,11,10,8,6,4,3,2],
        "query" : 3
    },
    "output": 10
})

test.append({
    "input":{
        "card":[2, 3],
    "query": 3
    },
    "output": 1,
})
print(test)


#locate_card(test[0]['input']['card'], test[0]['input']['position'])
print(locate_card(**test[1]['input']) == test[1]['output'])


