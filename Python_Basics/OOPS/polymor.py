# def rt(a,b):
#     return a+b                                        # the given funtion is returning the 
                                                        # values based on input data types

# print(rt(4,8))                                        # O/p:12
# print(rt("rtx","_3050"))                              # O/p: rtx_3050
# print(rt([1,2,3],[4,5,6]))                            # O/p: [1,2,3,4,5,6]

class engg:
    def syllabus(self):
        print("this is engineering syllabus")
class mbbs:
    def syllabus(self):
        print("this is mbbs syllabus")

def class_parser(class_obj):                         
    for i in class_obj:
        i.syllabus()
engstu=engg()
mbsstu=mbbs()
student=[engstu,mbsstu] 
print(class_parser(student))       # this is engineering syllabus
                                   # this is mbbs syllabus
