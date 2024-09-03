# import csv
#
# with open('emp.csv', 'r') as fp:
#     csvreaderobj = csv.reader(fp)
#     for csvreaders in csvreaderobj:
#         print(csvreaders)
#         for csvreader in csvreaders:
#             print(csvreader, end='  ')
#             print()



import csv

with open('emp.csv', 'r') as fp:
    csvreaderobj = csv.DictReader(fp)
    for csvreaders in csvreaderobj:
        act_cstreaders = dict(csvreaders)
        print(csvreaders)
        for k, v in act_cstreaders.items():
            print(f"{k}     {v}")
        print("======================")

