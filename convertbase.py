def _tentobase(x, new_base):
    base_chart={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f',16:'g',17:'h',18:'i',19:'j',20:'k',21:'l',22:'m',23:'n',24:'o',25:'p',26:'q',27:'r',28:'s',29:'t',30:'u',31:'v',32:'w',33:'x',34:'y',35:'z'}
    out=''
    current = x
    while current is not 0:
        remain = current % new_base
        if 36>remain>9:
            remain_str=base_chart[remain]
        elif remain>=36:
            remain_str='('+str(remain)+')'
        else:
            remain_str=str(remain)
        out = remain_str+out
        current=current/new_base
    return out
def convert_base(x, original_base, new_base=10):
    """Converts any base from 2-36
    Default new base is set to 10"""
    if original_base is not 10 and new_base is not 10:
        return _tentobase(int(str(x),original_base),new_base)
    elif original_base is not 10 and new_base is 10:
        return int(str(x),original_base)
    elif original_base is 10 and new_base is not 10:
        return _tentobase(int(str(x)), new_base)
    elif original_base is 10 and new_base is 10:
        return x
    else:
        raise ValueError('You done messed up something!')
