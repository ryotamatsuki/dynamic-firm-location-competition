"""Exact selected-equilibrium audit; no unrestricted SPNE claim."""
from fractions import Fraction as Q
from itertools import product
import sympy as S

def auction(bids, eligible, tie=0):
    if len(eligible)==1:return eligible[0],Q(0)
    i=tie if bids[0]==bids[1] else int(bids[1]>bids[0])
    return i,bids[1-i]

def evaluate(a,b,v,p,cap,bids,tie=0,second_tie=0):
    winner,pay=auction(bids,[0,1],tie)
    residual=list(cap);residual[winner]-=1
    eligible=[i for i in range(2) if residual[i]>0]
    j,sub2=auction((v,v),eligible,second_tie)
    local=[Q(0),Q(0)]
    local[winner]+=(a,b)[winner]-pay;local[j]+=p*(v-sub2)
    firm=pay+p*sub2;total=sum(local)+firm
    return winner,tuple(local),firm,total,j

def check_br(a,b,v,p,cap,bids,tie=0):
    result=evaluate(a,b,v,p,cap,bids,tie)
    n=0
    for i in (0,1):
        rival=bids[1-i]
        choices={Q(0),rival,rival+1}
        if rival>0:choices.add(rival/2)
        for x in choices:
            alt=list(bids);alt[i]=x
            assert evaluate(a,b,v,p,cap,alt,tie)[1][i]<=result[1][i]
            n+=1
    return n

a,b,z=S.symbols("a b z");d=b-a
base=S.Matrix([z,b-a+z,a-z,b+z])
switch=S.Matrix([a-b+z,z,b-z,a+z])
stay=S.Matrix([0,b-a,a+z,b+z])
assert S.simplify(switch-base)==S.Matrix([-d,-d,d,-d])
assert S.simplify(stay-base)==S.Matrix([-z,-z,2*z,0])
counts=dict(strict=0,reversal=0,no_reversal=0,ties=0,zero_arrival=0,best_response_cases=0)
for a,b,v,pn in product(range(1,16),range(1,16),range(1,11),range(0,11)):
    p=Q(pn,10);z=p*v;d=b-a
    if not b>a>z:continue
    bids0=(a-z,b-z);bids1=(Q(a),b-z)
    counts["best_response_cases"]+=check_br(a,b,v,p,(1,1),bids0)
    r0=evaluate(a,b,v,p,(1,1),bids0)
    if d==z:
        counts["ties"]+=1
        for t in (0,1):
            r1=evaluate(a,b,v,p,(1,2),bids1,t)
            counts["best_response_cases"]+=check_br(a,b,v,p,(1,2),bids1,t)
            assert r1[1]==(0,d) and r0[3]-r1[3]==(d if t==0 else 0)
    else:
        counts["strict"]+=1
        counts["zero_arrival"]+=int(p==0)
        counts["best_response_cases"]+=check_br(a,b,v,p,(1,2),bids1)
        r1=evaluate(a,b,v,p,(1,2),bids1)
        if d<z:
            counts["reversal"]+=1
            assert r0[0]==1 and r1[0]==0 and r1[3]-r0[3]==-d
            assert tuple(x-y for x,y in zip(r1[1],r0[1]))==(-d,-d)
        else:
            counts["no_reversal"]+=1
            assert r0[0]==r1[0]==1 and r1[3]==r0[3]
            assert tuple(x-y for x,y in zip(r1[1],r0[1]))==(-z,-z)
args=(8,10,5,Q(3,5),(1,2));alt=(Q(0),Q(9))
check_br(*args,alt)
assert evaluate(*args,alt)[:4]==(1,(0,10),3,13)
supports=((Q(0),Q(1)),(Q(9),Q(10)))
for i in (0,1):
    opp=supports[1-i]
    def eu(x):
        return sum(evaluate(*args,(x,y) if i==0 else (y,x))[1][i] for y in opp)/2
    vals=[eu(x) for x in supports[i]]
    tests={Q(0),*opp,opp[0]/2,(opp[0]+opp[1])/2,opp[1]+1}
    assert len(set(vals))==1 and max(eu(x) for x in tests)==vals[0]
print(counts)
