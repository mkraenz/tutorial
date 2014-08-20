from threading import Thread
def naehere_pi_an(n): 
    pi_halbe = 1 
    zaehler, nenner = 2.0, 1.0 
 
    for i in range(n): 
        pi_halbe *= zaehler / nenner 
        if i % 2: 
            zaehler += 2 
        else: 
            nenner += 2 
 
    print("Annaeherung mit %d Faktoren: %.16f" % (n, 2*pi_halbe))
    
naehere_pi_an(1000000)