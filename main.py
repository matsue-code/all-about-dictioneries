student_data ={'id1':
               {'name':['sara'],
                'class':['v'],
                'sublect_intergration':['english,math,science']
},
'id2':
{'name':['david'],
 'class':['v'],
 'sublect_intergration':['english,math,science']
},
'id3':
{'name':['sara'],
 'class':['v'],
 'sublect_intergration':['english,math,science']
},
'id4':
{'name':['shawn'],
 'class':['v'],
 'sublect_intergration':['english,math,science']
},
}
result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)