#Evaluate the postfix expression
s="15,5,+,7,2,-,*"
l=s.split(',')
res=0
st=[]
for i in l:
    if i.isdigit():
        st.append(i)
    else:
        op1=int(st.pop())
        op2=int(st.pop())
        if i=="+":
            res=op2+op1
            st.append(res)
        elif i=="-":
            res=op2-op1
            st.append(res)
        elif i=="/":
            res=op2/op1
            st.append(res)
        elif i=="*":
            res=op2*op1
            st.append(res)
print(*st)
    