cpaital = {
    "France" : "Paris",
    "Germany" : "Berlin"
}

###   Nesting a list in a Dictionary

travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin" ,"Hamburg", "Stuttgart"] 
}

####  Nesting Dictionary in a Dictionary

travel_log1 = {
    "France" : {
    "cities visited" : ["Paris", "Lille", "Dijon"],
    "total visits" : 12
    },
    "Germany" : {
    "cities visites" : ["Berlin" ,"Hamburg", "Stuttgart"],
    "total visits" : 5
    } 
}

###  Nesting a dictionary in a list

travel_list = [
    {
    "Countery" : "France",
    "cities visited" : ["Paris", "Lille", "Dijon"],
    "total visits" : 12
    },
    {
    "Country" : "Germany", 
    "cities visites" : ["Berlin" ,"Hamburg", "Stuttgart"],
    "total visits" : 5
    } 
]