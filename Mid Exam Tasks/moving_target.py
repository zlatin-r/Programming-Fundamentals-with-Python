targets = [int(x) for x in input().split(" ")]
result_targets = []
result = ""

while True:
    command = input().split(" ")
    action = command[0]
    
    if action == "End":
        break
    elif action == "Shoot":
        index = int(command[1])
        power = int(command[2])
        
        if 0 <= index <= len(targets) - 1:
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
        else:
            result = "Invalid placement!"
        
    elif action == "Add":
        index = int(command[1])
        val = int(command[2])
        
        if 0 <= index <= len(targets) - 1:
            targets.insert(index, val)
        else:
            result = "Invalid placement!"
        
    elif action == "Strike":
        index = int(command[1])
        radius = int(command[2])
        
        if index-radius >= 0 and index+radius <= len(targets) -1:
            for i in range(len(targets)):
                if index-radius <= i <= index+radius:
                    continue
                else:
                    result_targets.append(targets[i])
            targets = result_targets
        else:
            result = "Strike missed!"
            continue            
            
print(result)
print("|".join(str(x) for x in targets))
