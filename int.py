#!/usr/bin/env python3

def main():
    text = input("Напиши текст:")

    int = text.replace('и', 'ы').replace('И', 'Ы').replace('Е', 'Э').replace('е', 'э').replace('Й', 'Ӹ').replace('й', 'ӹ').replace('Ю', 'Ў').replace('ю', 'ў').replace('Ё', 'Ӭ').replace('ё', 'ӭ').replace('Ь', 'ѣ').replace('ь', 'ѣ').replace('Ъ', 'ѣ').replace('ъ', 'ѣ').replace('Я', 'Ӑ').replace('я', 'ӑ')

    print("\n\nТекст на интинском:", int)
    input()
pass

if __name__ == '__main__':
    while True:
        main()