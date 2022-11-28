# დაწერე პროგრამა რომელიც ფაილიდან წაიკითხავს 10
# რიცხვს და ამავე ფაილში ჩაწერს მხოლოდ მაქსიმალურს
# წაკითხული რიცხვებიდან
f=open("data.txt","r+")
lst=[line[:-1] for line in f]
f.write(max(lst[0:11]))



# დაწერე ფუნქცია, რომელსაც გადაეცემა Dictionary და
# დააბრუნებს რიცხვით value -ებს შორის მინიმალურს

def get_min(dict):
    return(min(dict.values()))

dict1 = {
    "mariam":20,
    "sopo":10,
    "gvantsa":23,
    "nino":7
}
print(get_min(dict1))

# დაწერე ფუნქცია, რომელიც ფაილიდან წაიკითხავს
# ინფორმაციას, შეავსებს სეტს მხოლოდ უნიკალური
# ელემენტებით და დააბრუნებს ამ სეტს
def unique1(file_name):
    file=open(file_name,"r")
    lst1=[]
    for i in file:
        if i not in lst1:
           lst1.append(i)
    return(lst1)

print(unique1("data.txt"))