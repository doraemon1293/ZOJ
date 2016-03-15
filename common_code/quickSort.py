def QSort(lst):
    return [] if lst==[] else QSort([e for e in lst[1:] if e<=lst[0]])+[lst[0]]+QSort([e for e in lst[1:] if e>lst[0]])