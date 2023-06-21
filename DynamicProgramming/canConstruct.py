from typing import List, Dict, Optional


def canConstruct(target: str, wordBank: List[str], cache: Optional[Dict[str, bool]] = None) -> bool:
    if target == "":
        return True
    if cache is None:
        cache = {}
    if target in cache:
        return cache[target]
    res = False
    for word in wordBank:
        if target.startswith(word):
            res = res or canConstruct(target[len(word):], wordBank, cache)
        if res:
            break
    cache[target] = res
    return res


print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("skateboard", [
      "bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(canConstruct("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
      ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
