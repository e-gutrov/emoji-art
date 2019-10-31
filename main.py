from PIL import Image
import numpy as np


emojis = []
colors = []


def init():
    global emojis, colors
    with open('emojis_clear.txt', 'r') as fin_emojis:
        for i in fin_emojis:
            emojis += i.split()
    with open('cols_for_images.txt', 'r') as fin_colors:
        for i in fin_colors:
            colors.append(list(map(int, i.split()))[1:])


def dist(a, b):
    return sum(map(lambda x, y: (x - y)**2, a, b))


def main():
    init()
    name = input('Enter a filename: ')
    img = Image.open(name)
    a = np.asarray(img)
    operation = input(
        'Image size is {0}x{1} pts.\n'
        'Enter "dec x" to decrease size by x times\n'
        'Enter "man w h" to get image with size w h (in chars): '.format(
            img.size[0], img.size[1]
        )
    )
    if operation[:3] == 'dec':
        times = float(operation.split()[1])
        size = tuple((int(img.size[0] / times), int(img.size[1] / times)))
    else:
        size = tuple(map(int, operation.split()[1:]))

    with open(input('Enter path to output file: '), 'w') as fout:
        print('Wait a bit...')
        for i in range(size[1]):
            for j in range(size[0]):
                x = j * img.size[0] // size[0]
                y = i * img.size[1] // size[1]
    
                ans_dist = 10**9
                ans_id = -1
                for l in range(len(colors)):
                    cur_dist = dist(a[y][x][:3], colors[l])
                    if cur_dist < ans_dist:
                        ans_dist = cur_dist
                        ans_id = l
                print(emojis[ans_id], end='', file=fout)
            print(file=fout)


main()
