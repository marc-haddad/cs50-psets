from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    lista = a.split("\n")
    listb = b.split("\n")
    linesims = [i for i in lista + listb if i in lista and i in listb]
    linesims_no_dup = list(set(linesims))
    print(linesims_no_dup)
    return linesims_no_dup


def sentences(a, b):
    """Return sentences in both a and b"""

    lista = sent_tokenize(a)
    listb = sent_tokenize(b)
    sentsims = [i for i in lista + listb if i in lista and i in listb]
    sentsims_no_dup = list(set(sentsims))
    return sentsims_no_dup


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    lista = []
    listb = []
    for i in range(len(a)):
        sub = a[i: n + i]
        if len(sub) < n:
            break
        lista.append(sub)
    for i in range(len(b)):
        sub = b[i: n + i]
        if len(sub) < n:
            break
        listb.append(sub)

    subsims = [i for i in lista + listb if i in lista and i in listb]
    subsims_no_dup = list(set(subsims))
    return subsims_no_dup
