def rectangle(w, h):
    print("*" * w)
    for i in range(1, h-1):
        print('*'+' '*(w-2)+'*')
    print("*" * w)

# def rect_char(w, h, ch):
#     print(ch * w)
#     for i in range(1, h-1):
#         print(ch+' '*(w-2)+ch)
#     print(ch * w)

# Или можно всё через циклы сделать
def rect_char(w, h, ch):

    for i in range(h+1):
        if i==0 or i==h:
            print(ch * w)
        else:
            print(ch+' '*(w-2)+ch)


def rect_2d(w, h, f, ch):
    for i in range(f):
        print(ch * w)
    for i in range(1, h-1):
        print(ch*f+' '*(w-f-2)+ch*f)
    for i in range(f):
        print(ch * w)


if __name__ == '__main__':
    rectangle(5,5)
    rect_char(7,5,'@')
    rect_2d(8,4,2,'#')