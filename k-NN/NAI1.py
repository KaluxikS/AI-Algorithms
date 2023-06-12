def readFlowerList(fileName):
    with open(fileName) as source:
        lines = source.readlines()

        flowerList = []

        for line in lines:
            atributes = line.strip().split(",")
            new_flower = {}
            new_flower["vec1"] = atributes[0]
            new_flower["vec2"] = atributes[1]
            new_flower["vec3"] = atributes[2]
            new_flower["vec4"] = atributes[3]
            new_flower["name"] = atributes[4]

            flowerList.append(new_flower)

        return flowerList


def countDistance(flower1, toFindName):
    distance = (float(flower1["vec1"]) - float(toFindName["vec1"])) ** 2 + (
                float(flower1["vec2"]) - float(toFindName["vec2"])) ** 2 + (
                           float(flower1["vec3"]) - float(toFindName["vec3"])) ** 2 + (
                           float(flower1["vec4"]) - float(toFindName["vec4"])) ** 2
    return distance


def classify(k, trainSetFileName, testSetFileName):
    flowerListTrain = readFlowerList(trainSetFileName)
    flowerListTest = readFlowerList(testSetFileName)

    correct = 0
    for i in range(len(flowerListTest)):
        distances = []

        for j in range(len(flowerListTrain)):
            distance = countDistance(flowerListTrain[j], flowerListTest[i])
            distances.append((distance, flowerListTrain[j]["name"]))
        distances.sort(key=lambda x: x[0])
        closest = [x[1] for x in distances[:k]]
        predicting_name = max(set(closest), key=closest.count)
        if predicting_name == flowerListTest[i]["name"]:
            correct += 1
        accuracy = float(correct) / len(flowerListTest)
    print("Accuracy:", int(accuracy * 100), "%")


def userClassify():
    flowerListTrain = readFlowerList("Train-set.txt")
    k = int(input("Enter k: "))
    vec1 = float(input("Enter vec1: "))
    vec2 = float(input("Enter vec2: "))
    vec3 = float(input("Enter vec3: "))
    vec4 = float(input("Enter vec4: "))
    user_flower = {"vec1": vec1, "vec2": vec2, "vec3": vec3, "vec4": vec4}
    distances = []
    for j in range(len(flowerListTrain)):
        distance = countDistance(flowerListTrain[j], user_flower)
        distances.append((distance, flowerListTrain[j]["name"]))
    distances.sort(key=lambda x: x[0])
    closest = [x[1] for x in distances[:k]]
    predicting_name = max(set(closest), key=closest.count)
    print("The predicted name for the given vector is:", predicting_name)


working = True
while working:
    command = input(
        "What would you like to do?\nType 'test' to see the outcome of the test and the accuracy\nType 'myvector' to enter your vector to classify it\nType 'exit' to end the program\n")
    if command == "test":
        k = int(input("Enter k to classify:\n"))
        classify(k, "Train-set.txt", "Test-set.txt")
        continue
    if command == "myvector":
        userClassify()
        continue
    if command == "exit":
        working = False
    else:
        print("Wrong command")
        continue
