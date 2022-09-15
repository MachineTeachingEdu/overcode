"""
A população a tem 80.000 indivíduos e cresce 3% ao ano.
A população b tem 200.000 indivíduos e cresce 1.5% ao ano.
Em quantos anos a população 'a' vai alcançar a população 'b'?
"""
def breakeven():
    anos = 0
    pop_a = 80000
    pop_b = 200000
    taxa_a = 1.03
    taxa_b = 1.015
    
    while pop_a < pop_b:
        pop_a *= taxa_a
        pop_b *= taxa_b
        anos += 1
            
    return anos
