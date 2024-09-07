
import csv

def open_file():
    with open('username.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        d = next(reader, None) 
        index = ask_which_col(d)
        print(index)
        for row in reader:
            print(', '.join(row))

def ask_which_col(header):
    for i, v in enumerate(header):
        print(f"{i} : {v}")
    return int(input("Which column? "))


open_file()



# word1 = 'fjdo'

# def find(word:str):
#     data1 = "te;fasdl;jsdfhe;fjdo;hdfe;"
#     data2 = "dfhksdlsdfhks;fkdsjf;hdkfjshdf;hdkdh;" 
    
#     index = None
#     for i, v in enumerate(xl("E2:E2")):
#         if find == v:
#             index =  i
#     if index:
#         print(index)
#         return xl("E3:E3")[index]
             


# def find(word_one, word_2):
    