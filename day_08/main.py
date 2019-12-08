inp_file = open("input.txt", 'r')
pz_inp = list(inp_file.readline())

# pz_inp = list('022211222212')

width = 25
height = 6

img = []
index = 0
while index < len(pz_inp):
    layer = []
    for i in range(0, height):
        row = []
        for j in range(0, width):
            row.append(pz_inp[index])
            index += 1
        layer.append(row)
    img.append(layer)


def count_digit_in_layer(layer, digit):
    count = 0
    for r in layer:
        for i in r:
            if i == digit:
                count += 1
    return count


low_c = count_digit_in_layer(img[0], '0')
low_l = img[0]
for l in img:
    count = count_digit_in_layer(l, '0')
    if count < low_c:
        low_c = count
        low_l = l

count_1 = count_digit_in_layer(low_l, '1')
count_2 = count_digit_in_layer(low_l, '2')

print(f'part 1: {count_1 * count_2}')


def get_pixel_list_for_pos(img, row, column):
    i = len(img) - 1
    p_l = []
    while i >= 0:
        l = img[i]
        # print(f'row: {row}, column: {column}')
        p = l[row][column]
        p_l.append(p)
        i -= 1
    return p_l


list_all = []
for j in range(0, height):
    for k in range(0, width):
        list_all.append(get_pixel_list_for_pos(img, j, k))
    k += 1
j += 1

# print(list_all)

fina_img_p_l = []
for each_p_L in list_all:
    final_p = each_p_L[0]
    for i in range(1, len(each_p_L)):
        if each_p_L[i] == '0' or each_p_L[i] == '1':
            final_p = each_p_L[i]
    fina_img_p_l.append(final_p)

x = str.join("", fina_img_p_l)

pz_inp = x

index = 0
layer = []
while index < len(pz_inp):
    for i in range(0, height):
        row = []
        for j in range(0, width):
            row.append(pz_inp[index])
            index += 1
        layer.append(row)

for r in layer:
    print(str.join(" ", r).replace('0', ' ').replace('1', '*'))
