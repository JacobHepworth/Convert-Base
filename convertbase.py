def ten_to_base(x, new_base,extend=[]):
    """Converts Base10 to BaseX(defined by user). Adding of new bases past Base36 is possible using the extend argument. Each new list item will be the new symbol for that base starting at Base37."""
    import sys
    base_chart={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f',16:'g',17:'h',18:'i',19:'j',20:'k',21:'l',22:'m',23:'n',24:'o',25:'p',26:'q',27:'r',28:'s',29:'t',30:'u',31:'v',32:'w',33:'x',34:'y',35:'z'}
    if not extend:
        pass
    else:
        for i in range(len(extend)):
            base_chart[36+i] = extend[i]
    out = ''
    current = x
    while current is not 0:
        remain = current%new_base
        if new_base > 36 and not extend:
            raise ValueError("Can't exceed base 36 without defining new bases")
        elif remain > 9:
            remain_str=base_chart[remain]
        elif remain is 0:
            return '0'
        else:
            remain_str=str(remain)
        out = remain_str+out
        if int(sys.version[0]) == 2:
            current=current/new_base
        elif int(sys.version[0]) >= 3:
            current=current//new_base
        else:
            raise SystemError('This version of Python is not supported')
    return str(out)
def convert_base(x, original_base, new_base=10):
    """Converts any Base to any Base but is limited to Base2 through Base36. Default new base is set to 10. Extending to a new base is not yet available with this function."""
    if original_base is not 10 and new_base is not 10:
        return ten_to_base(int(str(x),original_base),new_base)
    elif original_base is not 10 and new_base is 10:
        return int(str(x),original_base)
    elif original_base is 10 and new_base is not 10:
        return ten_to_base(int(str(x)), new_base)
    else:
        return x
