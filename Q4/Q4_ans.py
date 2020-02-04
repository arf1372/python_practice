def find_mismatch(s0,s1):
    if len(s0)!=len(s1):
        return 2
    firstDiffFounded=False
    for i,j in zip(s0,s1):
        if i!=j and firstDiffFounded:
            return 2
        elif i!=j and not firstDiffFounded:
            firstDiffFounded=True
    if firstDiffFounded:
        return 1
    return 0
if __name__ == '__main__':
    print(find_mismatch("kasra","kasra")) # 0
    print(find_mismatch("kasra","karra")) # 1
    print(find_mismatch("kasa" ,"kasra")) # 2
    print(find_mismatch("krrra","kasra")) # 2
