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
    return sum(map(lambda x, y: abs(x - y)**2, a, b))


def main():
    init()
    name = input('Введите имя файла: ')
    img = Image.open(name)
    a = np.asarray(img)
    size = tuple(map(int, input(
        'Размер картинки {0}x{1}. Введите размер ШxВ (в смайликах):'.format(img.size[0], img.size[1])).split()))
    with open('output.txt', 'w') as fout:
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
