from markov import *


def text_gen():
    num_texts = int(input("Enter the total number of text: "))
    print(
        "\nThis is the list of texts i have:\n\t1 alice_oz.txt\n\t2 anne_oz.txt\n\t3 peter pan_oz.txt\n\t4 wonderful wizard_oz.txt\n\t5 secret garden_oz.txt\n")
    name_of_texts = input("Enter the name of text separated by comma:\n").split(",")
    if len(name_of_texts) != num_texts:
        print("Sorry, the total number of texts and given texts are not the same.")
        return
    data = ""
    for text in name_of_texts:
        data += readdata(text)
    # print(data)
    window_value = int(input("Enter your desire window value: "))
    temperature_value = float(input("Enter your desire temperature value: "))
    word_length = int(input("Enter your desire word length: "))
    rule = makerule(data, window_value)
    stats = countrules(rule)
    generated_text = makestring(stats, word_length, temperature_value)
    return generated_text


def main():
    notdone = True
    while notdone:
        genrated_text = text_gen()
        print(f"\n{genrated_text}\n")
        choice = input("want to restart the process again: ").lower()
        if choice == "y":
            notdone = True
        else:
            notdone = False


if __name__ == '__main__':
    main()
