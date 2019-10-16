import wikipedia
while(True):
    input=raw_input("Ask Me Anything:")
    print (wikipedia.summary(input))
