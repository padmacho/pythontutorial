def add_spider(heros=None):
    if(heros is None):
        heros = []
    heros.append("spider")
    return heros

print(add_spider())
print(add_spider(['mario', 'dora']))
print(add_spider())   
