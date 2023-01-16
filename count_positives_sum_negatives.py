arr = [1, 2, 10, -11, -12]

def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    l = []
    count_positif=0
    sum_negatif=0
    for i in arr:
        if i > 0:
            count_positif=count_positif+1
        if i < 0:
            sum_negatif=sum_negatif+i
    l.append(count_positif)
    l.append(sum_negatif)
    return l
print(count_positives_sum_negatives(arr))

