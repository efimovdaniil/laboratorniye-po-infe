#определить средний рост девочек и мальчиков одного класса. В классе учится n учеников


list1 = []
list2 = []
averageboy = 0
averagegirl = 0
while True:
    print('введите кол-во учеников')
    try:
        n = int(input())
        l = 0
        boy = 0
        girl = 0
        while(l<n):
            y = (input('мальчик или девочка?'))
            if (y.lower()== "мальчик"):
                boy += 1
                print('рост')
                x = float(input())
                list1.append(x)

            elif(y.lower()== 'девочка'):
                girl +=1
                print('рост')
                z = float(input())
                list2.append(z)
            else:
                print('введите пожалуйста мальчик или девочка')
                n+=1
            l+=1

        averageboy = sum(list1)/len(list1) if boy > 0 else 0
        averagegirl = sum(list2)/len(list2) if girl >0 else 0
        print("средний рост мальчиков=",round(averageboy,2))
        print("средний рост девочек=",round(averagegirl,2))
        print('кол-во девочек=',girl)
        print('кол-во мальчиков=',boy)
    except ValueError:
        continue

