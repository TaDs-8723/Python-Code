#Trae Smith 101211905

def checking_matrices(x)->bool:

    if isinstance(x,list):
        count=0
        final=True
        while count<(len(x)-1):
            if isinstance(x[count],list):
                if len(x[count])==len(x[count+1]):
                    check=0
                    while check<len(x[count+1]):
                        if isinstance(x[count][check],int) or isinstance(x[count][check],float):
                           final=True
                           check+=1
                        else:
                            final=False
                            check=len(x[count])
                            count=len(x)
                            break
                    count+=1
                else:
                    final=False
                    count=len(x)
                    break
            else:
                final=False
                count=len(x)
                break
    else:
        final=False

    return final
