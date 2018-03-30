import csv 
import operator

file = open("N:\\ML\\dataset\\Fake_News_Detection\\stop_words.txt")
p = file.read();
stopWords = p.split('\n')

with open('vector.csv','w',newline='') as csvfile:
    fieldnames = ['vector', 'status'] # 0 for fake 1 for real
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    with open('fake_or_real_news.csv',encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        flag = False 
        for row in readCSV:
            FAKE = {}
            REAL = {}
            all_word = {}
            status = 0
            
            try:
                #print(row)

                if flag:
                    if row[3] == "FAKE":
                        words = row[1].split(' ')
                        
                        for word in words:
                            if word in stopWords:
                                continue
                            
                            if word in FAKE :
                                FAKE[word] = FAKE[word] + 2 
                            else:
                                FAKE[word] = 2
                        
                        words = row[2].split(' ')
                        
                        for word in words:
                            if word in stopWords:
                                continue
                            
                            if word in FAKE :
                                FAKE[word] = FAKE[word] + 1 
                            else:
                                FAKE[word] = 1
                        
                        all_word = sorted(FAKE.items(),key = operator.itemgetter(1),reverse = True)
                        
                    elif row[3] == "REAL":
                        status = 1
                        words = row[1].split(' ')
                        
                        for word in words:
                            if word in stopWords:
                                continue
                            
                            if word in REAL :
                                REAL[word] = REAL[word] + 2 
                            else:
                                REAL[word] = 2
                        
                        words = row[2].split(' ')
                        
                        for word in words:
                            if word in stopWords:
                                continue
                            
                            if word in REAL :
                                REAL[word] = REAL[word] + 1 
                            else:
                                REAL[word] = 1
                                
                        all_word = sorted(REAL.items(),key = operator.itemgetter(1),reverse = True)
                        
                    else:
                        continue
                        
                    vector = ""
                    
                    i = 0 
                        
                    for key,value in all_word:
                        i = i+1
                        
                        vector = vector + str(value)
                        vector = vector + " "
                        
                        if i == 50:
                            break
                        
                    for j in range(i,50):
                        vector = vector + "0 "
                        
                    writer.writerow({'vector': vector,'status': status})
                    
                else:
                    flag = True
                
            except:
                 continue   