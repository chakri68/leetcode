from typing import List, Dict, Optional

hits = 0


def allConstruct(target: str, wordBank: List[str], cache: Optional[Dict[str, Optional[List[List[str]]]]] = None) -> Optional[List[List[str]]]:
    global hits
    toPrint = False
    if cache is None:
        hits = 0
        toPrint = True
        cache = {}
    if target == "":
        return [[]]
    if target in cache:
        hits += 1
        return cache[target]
    res: Optional[List[List[str]]] = None
    for word in wordBank:
        if target.startswith(word):
            value = allConstruct(target[len(word):], wordBank, cache)
            if value is not None:
                if res is None:
                    res = []
                res.extend([[word, *words] for words in value])
    cache[target] = res
    if toPrint:
        print("HITS", hits)
    return res


print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(allConstruct("aaaaaaaaaaaaaaaaaaaaaf", ["aaaa", "aa", "a"]))
