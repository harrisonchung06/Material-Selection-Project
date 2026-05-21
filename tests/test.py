import utils
import consts

def main():
    # buckles
    #des_buckle = utils.Circ_Design(mat=utils.Material(rho=2700.0, E=69000000000.0, nu=0.33, Sy=276000000.0), d_o=0.010, t=0.0012)

    # yields
    #des_yield = utils.Circ_Design(mat=utils.Material(rho=2700.0, E=69000000000.0, nu=0.33, Sy=276000000.0), d_o=0.015, t=0.0005)

    # passes all tests
    #des_pass = utils.Circ_Design(mat=utils.Material(rho=2700.0, E=69000000000.0, nu=0.33, Sy=276000000.0), d_o=0.020, t=0.0010)

    #des_pso = utils.Circ_Design(mat=utils.Material(rho=7700.0, E=210000000000.0, nu=0.28, Sy=620422000.0), d_o=0.02995300397358228, t=0.0008382417450813412)
    #designs = [des_buckle, des_yield, des_pass, des_pso]
    #des = utils.Circ_Design(mat=utils.Material(rho=7858.000032, E=204999998381.83875, nu=0.29, Sy=282685049.019888), d_o=0.028960740032408474, t=0.0004484753443850196)
    #des = utils.Rect_Design(mat=utils.Material(rho=7300.0, E=190000000000.0, nu=0.26, Sy=241275200.0), a_o=0.028616937922240973, b_o=0.029834367310087154, a_i=0.025718967283053017, b_i=0.02657515019133697)
    #des =  utils.Circ_Design(mat=utils.Material(rho=7700.0, E=210000000000.0, nu=0.28, Sy=620422000.0), d_o=0.02995300397358228, t=0.0008382417450813383)
    #des = utils.Circ_Design(mat=utils.Material(rho=7700.0, E=210000000000.0, nu=0.28, Sy=620422000.0), d_o=0.02995300397358228, t=0.0008382417450813383)
    des = utils.Rect_Design(mat=utils.Material(rho=7700.0, E=210000000000.0, nu=0.28, Sy=620422000.0), a_o=0.028259956582776732, b_o=0.029063255394729575, a_i=0.025064632155511992, b_i=0.026188745721446957)
    designs = [des]
    for des in designs:
        crit_load = des.critical_load()
        crit_stress = des.critical_stress()
        buckling = des.buckling_condition()
        yielding = des.yielding_condition()
        score = utils.score(des)
        print(f'Moment of Inertia: {des.inertia()} ')
        print(f'Area: {des.area()}')
        print(f'Vol {des.vol()}')
        print(f'Score: {score}') 
        print(f'Crit Load: {crit_load}') 
        print(f'Crit Stress: {crit_stress}') 
        print(f'Conditions: {buckling}, {yielding}') 

if __name__ == '__main__':
    main()