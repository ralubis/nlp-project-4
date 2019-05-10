import random
from urllib.request import urlopen

NUM = "{:03}"

def generate_stories():
    # There are 209 stories that you can get from https://www.cs.cmu.edu/~spok/grimmtmp/
    # URL in the format https://www.cs.cmu.edu/~spok/grimmtmp/###.txt, where ### is a 3 digit number
    # from 1 to 209. For example, 030 or 189.
    for i in range(1, 210):
        story_url = "https://www.cs.cmu.edu/~spok/grimmtmp/" + NUM.format(i) + ".txt"
        data = urlopen(story_url)
        print("Writing story " + "{:03}".format(i) + "...")
        with open("{:03}".format(i) + ".txt", "w") as f:
            for line in data:
                f.write(line.decode("utf-8"))
            f.close()
        print("Finished story " + "{:03}".format(i) + ".", "\n")

def get_random_paragraph(story_number=None):
    if story_number is None:
        story_number = random.randint(1,209)
    with open("stories/" + NUM.format(story_number) + ".txt", "r") as f:
        data = [x.strip() for x in f.readlines()]
        story = []
        paragraph = []
        for line in data:
            if line.endswith('.') and len(paragraph) >= 16:
                paragraph.append(line)
                story.append(' '.join(paragraph))
                paragraph = []
            elif line != '':
                paragraph.append(line)
        if len(paragraph) > 0:
            story.append(' '.join(paragraph))
    return story[random.randint(0,len(story)) - 1]

def main():
    print(get_random_paragraph())
    
if __name__ == "__main__":
    main()