from typing import List, Dict, Optional

hits = 0


def countConstruct(target: str, wordBank: List[str], cache: Optional[Dict[str, int]] = None) -> int:
    global hits
    printHits = False
    if cache is None:
        cache = {}
        printHits = True
    if target == "":
        return 1
    if target in cache:
        hits += 1
        return cache[target]
    res = 0
    for word in wordBank:
        if target.startswith(word):
            res += countConstruct(target[len(word):], wordBank, cache)
    cache[target] = res
    if printHits:
        print("HITS", hits)
    return res


print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(countConstruct("skateboard", [
      "bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(countConstruct("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
      ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
