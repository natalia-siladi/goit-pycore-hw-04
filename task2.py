
with open('cats_file.txt', 'w') as fh:
    fh.write("60b90c1c13067a15887e1ae1,Tayson,3\n60b90c2413067a15887e1ae2,Vika,1\n60b90c2e13067a15887e1ae3,Barsik,2\n60b90c3b13067a15887e1ae4,Simon,12\n60b90c4613067a15887e1ae5,Tessi,5")

def get_cats_info(path):
    with  open('cats_file.txt', 'r') as fh:
        lines = [el.strip() for el in fh.readlines()]
        cats_info = []
        cat = {}

        for line in lines:
            new_line = line.split(",")
            cat["id"] = new_line[0]
            cat["name"] = new_line[1]
            cat["age"] = new_line[2]
            cats_info.append(cat)

    return cats_info

cats_info = get_cats_info('cats_file.txt')
print(cats_info)



