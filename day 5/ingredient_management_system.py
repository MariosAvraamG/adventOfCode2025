def get_ingredients(filename):
    with open(filename, 'r') as f:
        db = f.readlines()
        splitIndex = db.index('\n')
        freshIngredientsRange = [ingredientRange.strip() for ingredientRange in db[:splitIndex]]
        ingredients = [ingredient.strip() for ingredient in db[splitIndex+1:]]
    return freshIngredientsRange, ingredients


def get_fresh_ingredients(freshIngredientsRange, ingredients):
    fresh = 0
    for ingredientRange in freshIngredientsRange:
        lowerBound, upperBound = map(int, ingredientRange.split('-'))
        toRemove = []
        for ingredient in ingredients:
            ingredientId = int(ingredient)
            
            if ingredientId>=lowerBound and ingredientId<=upperBound:
                fresh+=1
                toRemove.append(ingredient)
        
        for i in toRemove:
            ingredients.remove(i)
    return fresh

def get_fresh_ingredient_ranges(freshIngredientsRange):
    ranges = []
    for ingredientRange in freshIngredientsRange:
        lowerBound, upperBound = map(int, ingredientRange.split('-'))
        ranges.append((lowerBound, upperBound))

    ranges.sort()

    finalisedRanges = [ranges[0]]
    for ingredientRange in ranges[1:]:
        currentLower = ingredientRange[0]
        currentUpper = ingredientRange[1]
        prevLower = finalisedRanges[-1][0]
        prevUpper = finalisedRanges[-1][1]
        if currentLower <= prevUpper:
            upperBound = max(currentUpper, prevUpper)
            finalisedRanges[-1] = (prevLower, upperBound)
        else:
            finalisedRanges.append((currentLower, currentUpper))

    freshIds = 0
    for finalisedRange in finalisedRanges:
        freshIds += (finalisedRange[1]-finalisedRange[0]+1)
    return freshIds


def main():
    freshIngredientsRange, ingredients = get_ingredients('day 5/ingredients_db.txt')
    print(get_fresh_ingredients(freshIngredientsRange, ingredients))
    print(get_fresh_ingredient_ranges(freshIngredientsRange))

if __name__ == '__main__':
    main()