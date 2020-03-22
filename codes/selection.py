import sortingvisualizer as sv

def selection_sort(l):
    k = 0
    for i in range(len(l)):
        min_num = l[i]
        min_index = i
        sorted_iter = [x for x in range(i)]
        # get the minimum number and its index
        for j in range(i+1, len(l)):
            fname = str(k)
            sv.display(l, fname, min_index, j, sorted=sorted_iter)
            k += 1

            if l[j] < min_num:
                min_num = l[j]
                min_index = j

        fname = str(k)
        sv.display(l, fname, min_index, sorted=sorted_iter)
        k += 1
        l[i], l[min_index] = l[min_index], l[i]

        fname = str(k)
        sv.display(l, fname, i, min_index, sorted=sorted_iter, color1='#b41e2c', color2='#b41e2c')
        k += 1
    return l, k

random_l = sv.create_random_list(10)
sorted_l, length_l = selection_sort(random_l)
sv.make_gif(length_l, fname='selection.gif')