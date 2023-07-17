import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Memo1113/Intermedia/main/Picos.csv',header=0, sep=';')

m=len(df)
n=len(df.columns)
Media=[]
Incer=[]
c=0
for j in df:
    c+=1
    sum=df[j].sum()
    media=sum/m
    dif=0
    for i in range(0,m):
        dif= dif + pow(df.loc[i][j]-media,2)
    incer= pow(dif/(m-1),0.5)/pow(m,0.5)
    incer=round(incer,2)
    media=round(media,2)
    Incer.append(incer)
    Media.append(media)

x=[]
for i in range(0,n):
    x.append(i+1)

print('Los voltajes promedio de los picos son:\n',Media)
print('\nSus incertidumbres respectivas son:\n',Incer)
plt.grid()
plt.errorbar(x, Media, yerr=Incer, capsize=2, elinewidth=3, linewidth=0,marker='o', markersize=3, markerfacecolor='0.5',markeredgecolor='k',ecolor='r', label='mediciones')
plt.suptitle(r'$Picos$',fontsize=24,color='r')
plt.xlabel(r'$N°$',fontsize=12,color='blue')
plt.ylabel(r'$U_1/V$',fontsize=12,color='blue')
c=u"\u00B1"
for i in range(1,n):
    a=Media[i-1]
    b=Incer[i-1]
    plt.text(i+0.05, Media[i-1],"{}{}{}". format(a,c,b),va='center',fontsize=8,color='b')
a=Media[n-1]
b=Incer[n-1]
plt.text(n-0.05, Media[n-1],"{}{}{}". format(a,c,b),ha='right',va='center',fontsize=8,color='b')
plt.show()

d=[]
I=[]
for i in range(1,n):
    dif=Media[i]-Media[i-1]
    dif=round(dif,2)
    d.append(dif)
    incer=pow(pow(Incer[i],2)+pow(Incer[i-1],2),0.5)
    incer=round(incer,2)
    I.append(incer)
print('\nLas distancias consecutivas de los picos son:\n',d)
print('\nSus incertisumbres respectivas son:\n',I)

n=len(d)
x=[]
for i in range(0,n):
    x.append(i+1)

plt.grid()
plt.errorbar(x, d, yerr=I, capsize=3, elinewidth=2, linewidth=0,marker='o', markersize=3,markerfacecolor='0.5',markeredgecolor='k',ecolor='r', label='mediciones')
plt.suptitle(r'$Distancias\;entre\;picos$',fontsize=24,color='r')
plt.xlabel(r'$N°$',fontsize=12,color='blue')
plt.ylabel(r'$\Delta\;U_1$',fontsize=12,color='blue')
c=u"\u00B1"
for i in range(1,n):
    a=d[i-1]
    b=I[i-1]
    plt.text(i+0.05, d[i-1],"{}{}{}". format(a,c,b),va='center',fontsize=8,color='b')
a=d[n-1]
b=I[n-1]
plt.text(n-0.05, d[n-1],"{}{}{}". format(a,c,b),ha='right',va='center',fontsize=8,color='b')
plt.show()

n=len(d)
sum1=0
sum2=0
for i in range(n):
    sum1+=d[i]
    sum2+=pow(I[i],2)
prom=sum1/n
prom=round(prom,2)
incer=pow(sum2,0.5)/n
incer=round(incer,2)

r=0
for i in range(n):
    r+=pow(d[i]-prom,2)
s=pow(r/(n-1),0.5)
dy=[]
y=[]
for i in range(n):
    y.append(d[i]-prom)
    p=pow(pow(I[i],2)+pow(incer,2),0.5)
    dy.append(p)
q=0
for i in range(n):
    q=q+pow(y[i]*dy[i],2)

si=pow(p,0.5)/(s*(n-1))
print(si)
s=round(s,3)
si=round(si,3)
print('\nEl promedio de estas distancias es ',prom,' \u00B1 ',incer)
print('\nLa desviación estandar es ',s,' \u00B1 ',si)