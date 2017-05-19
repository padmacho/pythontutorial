def add_spider(heros=[]):
    heros.append("spider")
    return heros

print(add_spider())
print(add_spider(['mario', 'dora']))
# This is a potential bug. instead of adding spider once in list we see it twice
print(add_spider())   
