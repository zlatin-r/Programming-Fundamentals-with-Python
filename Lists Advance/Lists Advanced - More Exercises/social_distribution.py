population = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())
counter = 0
result = ""

for number in population:
    if number < minimum_wealth:
        wealth_needed = minimum_wealth - number
        max_wealth = max(population)
        index_max_wealth = population.index(max_wealth)
        if max_wealth - wealth_needed < minimum_wealth:
            result = "No equal distribution possible"
            break
        else:
            population[counter] = number + wealth_needed
            population[index_max_wealth] = max_wealth - wealth_needed
            counter += 1
    result = population

print(result)
