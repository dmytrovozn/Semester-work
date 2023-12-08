# Семестрова робота

with open('text.txt', 'r', encoding='utf-8') as file:
        content = file.read()
while True:        
    word1 = input("Введіть слово для заміни: ")
    if word1 not in content:
        print(f"Слово '{word1}' не знайдено у тексті.")   
    else:
        word2 = input("Введіть нове слово: ")
        content = content.replace(word1, word2)
        break

with open('text.txt', 'w', encoding='utf-8') as file:
        file.write(content)
    
print(f"Слово '{word1}' замінено на '{word2}'.")
