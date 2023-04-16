import csv

def valid(s):
    for i in s:
        if not s.isalnum() and s!="_":
            return False
    return True


def login(username,password,file_path):
    username=username.strip()
    if not valid(username):
        return -1  # not a valid username 
    with open(file_path,"r") as f:
        f.seek(0.0)
        lst=f.readline().split(',')
        #print(type(lst),f.tell())
        csv_reader=csv.DictReader(f,fieldnames=lst)
        for i in csv_reader:
            if i[lst[0]]==username:
                if i[lst[1]]==password:

                    return 0 # username and password verified 
                else:
                    return -2 # wrong password 
        return -3 # Username not found

def add_score(username,time,correct,file_path):
    with open(file_path,"a",newline="") as f:
        csv_writer=csv.writer(f)
        csv_writer.writerow([username,time,correct])
    

def best_score(file_path,func):
    with open(file_path) as f:
        csv_reader=csv.reader(f)
        next(csv_reader)
        highest=0
        u=""
        for i in csv_reader:
            temp=func(i[1],i[2])
            if temp>highest:
                highest=temp
                u=i[0]
    return highest,u   
        


    
