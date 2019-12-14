import sortingvisualizer as sv

def insertion_sort(l):
    k = 0
    for i in range(1, len(l)):
        sorted_iter = [x for x in range(i)]
        fname = str(k)
        sv.display(l, fname, i, i-1, sorted=sorted_iter)
        k += 1
        while i > 0 and l[i-1] > l[i]:
            l[i], l[i-1] = l[i-1], l[i]
            fname = str(k)
            sv.display(l, fname, i, i-1, sorted=sorted_iter)
            k += 1
            i -= 1
        fname = str(k)
        sv.display(l, fname, sorted=sorted_iter)
        k += 1
    fname = str(k)
    sv.display(l, fname, sorted=sorted_iter)
    k += 1
    return l, k

random_l = sv.create_random_list(10)
sorted_l, length_l = insertion_sort(random_l)
sv.make_gif(length_l, fname='insertion.gif')