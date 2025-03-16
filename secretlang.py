# st=input("Enter the message:")
# words=st.split()
# coding=input("Enter 1 for coding anf 0 for decoding:")
# coding=True if (coding=="1") else False
#
# if coding:
#  nwords=[]
#  for word in words:
#      if len(word)>=3:
#         r1="str"
#         r2="dge"
#         stnew=r1+word[1:]+word[0]+r2
#         nwords.append(stnew)
#      else:
#         nwords.append(word[::-1])
#  print(" ".join(nwords))
# else:
#     nwords=[]
#     for word in words:
#        if len(word)>=3:
#                 stnew=word[3:-3]
#                 stnew=stnew[-1]+stnew[:-1]
#                 nwords.append(stnew)
#        else:
#           nwords.append(word[::-1])
#     print(" ".join(nwords))
to_do=input("Enter 1 for coding and 0 for decoding:")
st=input("Enter the message:")
words=st.split()
to_do=True if (to_do=="1") else False
if to_do:
    queue=[]
    for word in words:
        var = int(len(word) / 2)
        if len(word)>=3:
            if len(word)%2==0:
                temp=word[var:]+word[:var]
                queue.append(temp)
            else:
                q1="we"
                q2="si"
                temp=word[-1]+q1+word[:-1]+q2
                queue.append(temp)
        else:
            lemp=word[1]+word[0]
            queue.append(lemp)
    print(" ".join(queue))
else:
    queue = []
    for word in words:
        if len(word) >= 3:
            var = int(len(word) / 2)
            if len(word) % 2 == 0:
                temp = word[var:] + word[:var]
                queue.append(temp)
            else:
                temp=word[3:-2]+word[0]
                queue.append(temp)
        else:
            lemp= word[1]+word[0]
            queue.append(lemp)
    print(" ".join(queue))
