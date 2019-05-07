import pos_tagging

if __name__ == "__main__":
    text = ""
    with open("frogking.txt", 'r') as f:
        text = f.read()
    print(text)
    pos_tagging.generate_blanks(text)
    