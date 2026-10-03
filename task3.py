words = ["кот", "пёс", "кот", "кот", "ёж", "пёс", "кот"]
new_words = list(set(words))
ans = []
count = 1
for word in new_words:
    ans.append([word, words.count(x)])
ans = sorted(ans)
for word, ct in ans:
    print(f"{count}. {word} - {ct}")
    count += 1