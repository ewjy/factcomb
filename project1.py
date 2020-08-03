import csv
with open("C:\\python\\台大code\\project 1\\project.csv", newline = "") as test:

    rows = csv.DictReader(test)
    cin = [row for row in rows]
class test:
    def init(self,hour,minute,second):
        self.hour = int(hour)
        self.second = int(second)
    def isvalidtime(self,t_start,t_last):
        if (t_start.hour == t_last.hour):#先判斷測資 是同一個小時 or not
            if self.hour == t_start.hour:
                if (self.minute > t_start.minute) and (self.minute < t_last.minute):#同一個小時 只有last會大於start的分鐘的情況
                    return True
                elif (self.minute == t_start.minute):#那如果分鐘數相同，要比秒數
                    if (t_start.second == t_last.second):#秒數相同，回傳True
                        if (self.second == t_start.second):
                            return True
                    elif(t_last.second > t_start.second):#秒數last一定會比start大
                        if (self.second >= t_start.second):
                            return True 
        elif(t_last.hour > t_start.hour):#如果有幾個小時，就要分成在t_start小時內 ，之間 ， 和t_last小時內
            if (self.hour == t_start.hour):#情況一
                if self.minute > t_start.minute:
                    return True
                elif (self.minute == t_start.minute) :
                    if t_last.second  == t_start.second:
                        if self.second == t_start.second:
                            return True
                    else:
                        if self.second >= t_start.second:
                            return True

            elif (self.hour == t_last.hour):#情況三
                if self.minute < t_last.minute:
                    return True
                elif self.minute == t_last.minute:
                    if self.second <= t_last.second:
                        return True
            elif (self.hour > t_start.hour) and (self.hour < t_last.hour):#情況二
                return True
                
            return False


def strtotime(time):
    [time1 , time2] = time.split(" ")
    [hour1 , minute1, second1] = time1.split(":")
    [hour2 , minute2, second2] = time2.split(":")
    t1 = test()
    t2 = test()
    t1.init(hour1 , minute1, second1)
    t2.init(hour2 , minute2, second2)
    return t1,t2
def strtofuck(fuck):
    t3 = test()
    [hour,minute,second] = fuck.split(":")
    t3.init(hour,minute,second)
    return t3



count1_A = 0
count1_C = 0
count1_R = 0
count1_T = 0
count1_W = 0
count2_A = 0
count2_C = 0
count2_R = 0
count2_T = 0
count2_W = 0
count3_A = 0
count3_C = 0
count3_R = 0
count3_T = 0
count3_W = 0
count4_A = 0
count4_C = 0
count4_R = 0
count4_T = 0
count4_W = 0
time = input()
time = strtotime(time)
for i in cin:
    
    if strtofuck(i['SubmissionTime']).isvalidtime(time[0],time[1]) == True:
        print(i['SubmissionTime'])
        if i['Problem'] == '1':
            if i['Status'] == 'Accepted':
                count1_A += 1
            elif i['Status'] == 'Compile Error':
                count1_C += 1
            elif i['Status'] == 'Runtime Error':
                count1_R += 1
            elif i['Status'] == 'Time Limit Exceed':
                count1_T += 1
            elif i['Status'] == 'Wrong Answer':
                count1_W += 1
        elif i['Problem'] == '2':
            if i['Status'] == 'Accepted':
                count2_A += 1
            elif i['Status'] == 'Compile Error':
                count2_C += 1
            elif i['Status'] == 'Runtime Error':
                count2_R += 1
            elif i['Status'] == 'Time Limit Exceed':
                count2_T += 1
            elif i['Status'] == 'Wrong Answer':
                count2_W += 1
        elif i['Problem'] == '3':
            if i['Status'] == 'Accepted':
                count3_A += 1
            elif i['Status'] == 'Compile Error':
                count3_C += 1
            elif i['Status'] == 'Runtime Error':
                count3_R += 1
            elif i['Status'] == 'Time Limit Exceed':
                count3_T += 1
            elif i['Status'] == 'Wrong Answer':
                count3_W += 1
        elif i['Problem'] == '4':
            if i['Status'] == 'Accepted':
                count4_A += 1
            elif i['Status'] == 'Compile Error':
                count4_C += 1
            elif i['Status'] == 'Runtime Error':
                count4_R += 1
            elif i['Status'] == 'Time Limit Exceed':
                count4_T += 1
            elif i['Status'] == 'Wrong Answer':
                count4_W += 1
list_1 = [count1_A,count1_C,count1_R,count1_T,count1_W] 
list_2 = [count2_A,count2_C,count2_R,count2_T,count2_W]
list_3 = [count3_A,count3_C,count3_R,count3_T,count3_W]
list_4 = [count4_A,count4_C,count4_R,count4_T,count4_W]
print(list_1,list_2,list_3,list_4, sep = ";")