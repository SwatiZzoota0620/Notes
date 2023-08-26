dic={101:{'Name':'Ram','DesignationCode':'A','Department':'MCA','Basic':40000,'HRA':5200,'IT':6000},
     102:{'Name':'Sham','DesignationCode':'B','Department':'BCA','Basic':750000,'HRA':4000,'IT':4000},
     103:{'Name':'Mohan','DesignationCode':'C','Department':'BSC','Basic':25000,'HRA':6000,'IT':3500},
     104:{'Name':'Rahul','DesignationCode':'D','Department':'MCA','Basic':65000,'HRA':2000,'IT':4500}}

dic2={'A':{'Designation':'PythonDeveloper','DA':2000},
      'B':{'Designation':'JavaDeveloper','DA':2100},
      'C':{'Designation':'PHPDeveloper','DA':2200},
      'D':{'Designation':'CDeveloper','DA':2300}}

user_id=int(input('Enter the id of employee: '))
print("User Id is: ",user_id)
if(user_id not in dic):
    print('Invalid ID')
    exit(0)
else:
    print('Information of Employee: \n ',dic[user_id])
    user_idd=dic[user_id]
    a = dic2[user_idd['DesignationCode']]
    da = a['DA']
    print('Total Salary:',user_idd['Basic']+user_idd['HRA']-user_idd['IT']+da)