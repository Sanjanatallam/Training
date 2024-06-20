a="f46cgu09@&aRTAEmk0eIbc9465"
UV,UC,lv,lc,d,s=0,0,0,0,0,0
for i in a:
    if (i.isupper()):
        if(i in 'AEIOU'):
            UV=UV+1
        else:
            UC=UC+1
    elif(i.islower()):
        if(i in 'aeiou'):
            lv=lv+1
        else:
            lc=lc+1
    elif(i.isdigit()):
        d=d+1
#     else(not i.isalpnum()):
    else:
        s=s+1
print("UV-",str(UV))
print("UC-",str(UC))
print("lv-",str(lv))
print("lc-",str(lc))
print("d-",str(d))
print("s-",str(sprint("UV-",str(UV))))
    