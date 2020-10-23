#Create a story
story_string="One afternoon %(boy_name:)s was %(verb:)s to the train and he heard %(adjective:)s noises behind him. %(noun:)s also saw a %(adjective2:)s balloon and a clown in the bushes. %(boy_name:)s knew it was straight out of the movie IT and began to %(verb2:)s for his life. He was 2 hours late to Adelphi University."
#Define the function madlibs
def madlibs():
#Create dict() so the words can be stored
    new= dict()
#Replace old characters with new ones
    replace("boy_name:", new)
    replace("verb:", new)
    replace("adjective:", new)
    replace("noun:", new)
    replace("adjective2:", new)
    replace("verb2:", new)
#Print the new string
    print(story_string % new)
#Set old strings to be replaced
def replace(old,new):
    new[old]= input("Enter a %s" % old)
#Print entire new story
madlibs()

    
