def toplam(input):
    result=0
    for i in input:
       result =result=result+i
    return result

def boy(input):
        return len(input)
def ortalama(input):
        return float(sum(input))/len(input)

input=[5,2,2,3]
print(toplam(input), boy(input), ortalama(input))

//*bir dizinin içindeki elemanlarının toplamı,ortalaması ve dizi boyunu fonksiyonlarla yazan programı yazınız.
