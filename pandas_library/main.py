# 원하는 데이터 추출하기
with open("weather_data.csv") as weather:
    data=weather.readlines()
#     print(data)

# csv 활용하여 데이터 추출하기
import csv
with open("weather_data.csv") as data_file:
    data=csv.reader(data_file)
    temperatures=[]
    for row in data:
        num = row[1]
        if num != "temp":
            temperatures.append(int(num))
#     print(temperatures)

# 판다스를 활용한 원하는 데이터 추출하기
import pandas

data= pandas.read_csv("weather_data.csv")

data_dict= data.to_dict()
temp_list=data['temp'].to_list()

# 과제 : 평균 온도 구하기
average =(data['temp'].sum()/len(data['temp']))
#print(average)

# 과제 : 최고 온도 구하기
# print(data['temp'].max())

# 가장 높은 온도의 데이터가 있는 행 구하기
#print(data[data['temp']==data.temp.max()])

# 월요일 온도를 불러오고 섭씨온도를 화씨온도로 변경하기
monday = data[data.day == "Monday"]
monday_temp=int(monday.temp)
f_temp_monday = monday_temp*9/5+32
# print(f_temp_monday)

# 딕셔너리를 데이터프레임으로 만들기
sample_dict={
    "students":['Amy','Max','Jane'],
    "scores":[75,60,87]
}
sample= pandas.DataFrame(sample_dict)
# print(sample)

# 특정 데이터에서 다람쥐 색상 개수 구하기
data_1=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count=len(data_1[data_1["Primary Fur Color"]=="Gray"])
red_squirrels_count=len(data_1[data_1["Primary Fur Color"]=="Cinnamon"])
black_squirrels_count=len(data_1[data_1["Primary Fur Color"]=="Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_1_dict={
    "Fur Color": ["Gray","Cinnamon", "Black"],
    "Count" : [gray_squirrels_count,red_squirrels_count, black_squirrels_count]
}

df=pandas.DataFrame(data_1_dict)
# df.to_csv("squirrel_count.csv")









