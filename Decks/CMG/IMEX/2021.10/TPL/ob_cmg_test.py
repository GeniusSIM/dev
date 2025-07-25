from ob_cmg import OB_CMG

def read_dat_file(dat_file):
    """
    - Function to read dat file <*.dat>.
    - Executed by an instance of class OB_CMG.
    - Is optional for class OB_CMG.
    """
    return None

def read_simulation_results(sim_data_file):
    """
    - Function to read host data file < root.host.data >.
    - Executed by an instance of class OB_CMG.
    - Class OB_CMG requires this function to accept the host data file name.
    - It may return any number of variables as shown in this sample function.
    - These variables will be passed to function ob_compute by class OB_CMG in
      the same order for further computations and analysis.
    """

    cur_BHP = 0.0
    cur_STO = 0.0
    cur_STG = 0.0
    cur_GOR = 0.0
    cur_Tim = 0.0

    with open(sim_data_file, mode='r') as handle:
        for line in handle:
            lst = line.strip().split()
            if len(lst) == 0:
                continue
            elif lst[0][:2] == '**':
                continue
            elif lst[0][:5] == 'WELL':
                if 'PRODUCER1' in lst[2]:
                    cur_BHP = float( lst[6] )
                    cur_STO = float( lst[9] )
                    cur_STG = float( lst[11] )
                    if cur_STO > 0:
                        cur_GOR = cur_STG / cur_STO
                    else:
                        cur_GOR = 0.0
            elif lst[0][:9] == 'TIMECURR':
                cur_Tim = float( lst[1] )

    return cur_Tim, cur_BHP, cur_STO, cur_STG, cur_GOR

def ob_compute(next_handshake, ob_sgnl_file, ob_data_file, dat_file_data, sim_data):
    """
    - Function to perform outboard computations and analysis.
    - Executed by an instance of class OB_CMG.
    - Class OB_CMG requires this function to accept three MANDATORY arguments:
        > next_handshake
        > ob_sgnl_file: Outboard signal file name
        > ob_data_file: Outboard data file name
    - The remaining arguments will be exactly in the same order as those
      returned by function < read_SimDFile >.
    - It also writes the outboard signal and data files.
    """

    cur_Tim, cur_BHP, cur_STO, Cur_STG, cur_GOR = sim_data
    OB_Constraint = "**EMPTY"
    new_BHP = 0.0

    # Outboard does its computations.
    if cur_GOR > 100.0:
        new_BHP = min( cur_BHP * 1.05, 2500 )
        OB_Constraint = "ALTER 'PRODUCER1'\n\t" + str(new_BHP)
        print( f'   OB Event ({cur_Tim:^10.2f} days ):\tChoking back well to control GOR.' )
    if cur_STO < 50.0:
        OB_Constraint = "SHUTIN 'PRODUCER1'"
        print( f'   OB Event ({cur_Tim:^10.2f} days ):\tShuting in Well due to low oil rate.' )

    # Create outboard signal and data files.
    with open(ob_sgnl_file, mode='w') as handle:
        handle.write( str(next_handshake + 1) + '\t 1' )

    with open(ob_data_file, mode='w') as handle:
        handle.writelines( OB_Constraint )

if __name__ == '__main__':
    ob_imex = OB_CMG(read_simulation_results, ob_compute, read_dat_file, 120.0)
    ob_imex.run()