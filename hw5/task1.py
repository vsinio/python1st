# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 1 способ

#TO DO

text_for_def = "Арава арива братец барашка бред брат вот вон вид абва абв"
symb = (input(),input(), input())



def del_symb(text, what_del):
    new_text = ""
    for i in text:
        if i not in what_del:
            new_text+=i
    return new_text

new_text = del_symb(text_for_def,symb)

print(new_text)

