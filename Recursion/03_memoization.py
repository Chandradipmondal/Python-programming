#memoization means when new value come then store it for reusing this value ,so in this program space consuming is high but time is low consuming
def memo(m,d):
    if m in d:
        return d[m]
    else:
        d[m]=memo(m-1,d)+memo(m-2,d)
    return d[m]
d={0:1,1:1}
print(memo(4,d))