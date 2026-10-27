# Second Most Frequently Occurring Character


text = input("Enter a string: ")
count = {}
for ch in text:
    count[ch] = count.get(ch, 0) + 1
frequencies = sorted(set(count.values()), reverse=True)
if len(frequencies) < 2:
    print("Second most frequent character does not exist")
else:
    second_freq = frequencies[1]
    for ch in count:
        if count[ch] == second_freq:
            print("Second most frequent character:", ch)
            print("Frequency:", second_freq)
            break
