def short_pattern():
    pattern = {}
    pattern["sequence"] = "101"
    pattern["occurences"] = 5
    return pattern

def medium_pattern():
    pattern = {}
    pattern["sequence"] = "111000"
    pattern["occurences"] = 25
    return pattern

def long_pattern():
    pattern = {}
    pattern["sequence"] = "1100110011001100"
    pattern["occurences"] = 50
    return pattern

def run():
    print("Analysing patterns...")
    dicto = dict()
    dicto["short sequence"] = short_pattern()
    dicto["medium sequence"] = medium_pattern()
    dicto["long sequence"] = long_pattern()
    total = 0
    for i,j in dicto.items():
        print(f"{i}: {j}")
        total += j["occurences"]
    print(f"Total was: {total}")
        
