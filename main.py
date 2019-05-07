import pos_tagging

if __name__ == "__main__":
    text = ""
    with open("frogking.txt", 'r') as f:
        text = f.read()

    #return the paragraph with removed words
    removed, new_text = pos_tagging.generate_blanks(text)
    print("Here is the original text:")
    print(new_text)

    #prompt the user for each black and store all input
    for i in removed:
        pos = i[2]
        prompt = "idk"
        if pos in {"JJ", "JJR", "JJS"}:
            prompt = "Type an adjective: "
        elif pos in {"RB", "RBR", "RBS"}:
            prompt = "Type an adjective: "
        elif pos in {"VB", "VBD", "VBG", "VBN", "VBP", "VBZ"}:
            prompt = "Type a verb: "
        else:
            prompt = "I messed up!"

        response = input(prompt)
        i.append(response)

    print(removed)

    #return completed paragraph
    print(pos_tagging.fillin_blanks(new_text, removed))
    