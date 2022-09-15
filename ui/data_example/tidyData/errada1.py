def breakeven():
    anos=0
    pop_a=80000
    pop_b=200000
    taxa_a=0.1
    taxa_b=0.015
    while pop_a<pop_b:
        pop_a=pop_a+pop_a*taxa_a
        pop_b=pop_b+pop_b*taxa_b
        anos+=1
    return anos
