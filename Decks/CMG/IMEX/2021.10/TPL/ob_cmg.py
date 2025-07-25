import sys
import time
import os
import subprocess
import signal
from pathlib import Path

class OB_CMG:
    """
    - Class implementing the coupling process between outboard and CMG hosts (IMEX, STARS, GEM).
    - To detect the CMG host type, the corresponding executable name must start with letters 'i', 's', 'g', respectively.
    - This class requires two functions playing the outboard roles.
    - This class requires Python 3.8 or later versions.
    """

    def __init__(self, read_sim_results_func, ob_compute_func, read_dat_file_func=None, ob_max_sleep_time=120.0):
        """
        Initialize class instance variables:
            read_simulation_results: Function name to read < root.host.data > file. Must be defined by user and passed
                                     to class constructor when instantiating the class. (Mandatory)
            ob_compute             : Function name to perform outboard computations. Must be defined by user and passed
                                     to class constructor when instantiating the class. (Mandatory)
            read_dat_file          : Function to read data set to extract required information, if any required. (Optional)
            ob_max_sleep_time      : Maximum sleep time for outboard software during which waits for host signal file
                                     to be created. (Optional)
            data                   : A dictionary storing the required information for class instance.
            dat_file_data          : Data read from data set (dat file) by function read_dat_file().
        """

        self.read_simulation_results = read_sim_results_func
        self.ob_compute = ob_compute_func
        self.read_dat_file = read_dat_file_func
        self.ob_max_sleep_time = ob_max_sleep_time

        self.data = dict()
        self.dat_file_data = None

        if sys.platform.lower().startswith('win'):
            self.data['PDelimiter'] = '\\'
            self.data['Platform'] = 'win'
        elif sys.platform.lower().startswith('lin'):
            self.data['PDelimiter'] = '/'
            self.data['Platform'] = 'lin'
        else:
            OB_CMG.print_msg( 0, 'Not supported platform.' )

    @staticmethod
    def print_header():
        """
        Prints header
        """

        c = '*'
        print( '\n' + \
               '\n' + 70*c + \
               '\n' + c + 68*' ' + c + \
               '\n' + c + 'CMG-Outboard Interface'.center(68) + c + \
               '\n' + c + 'Computer Modelling Group Ltd., Calgary, Canada'.center(68) + c + \
               '\n' + c + 68*' ' + c + \
               '\n' + 70*c + \
               '\n' )

    @staticmethod
    def print_msg(itype, msg):
        """
        Prints messages
        """

        if itype == 0:
            print( f'\n > ERROR:\t{msg}' )
            os._exit(1)
        elif itype == 1:
            print( f' > {msg}' )
        elif itype == 2:
            print( f"\n{(' ' + msg + ' ').center(70, '*')}" )
            os._exit(0)

    def check_arg(self):
        """
        - Read the commandline arguments.
        - Determine the host type (IMEX, STARS, GEM) based on host executable name.
        - Determine output files directory which is used to look for host signal and data files.
        - Prepare other required information.
        - Prepare the host command in order to run host.
        - The name of python script using this class will be considered as Outboard Software name. Since,
          CMG hosts do not accept blanks in the name of outboard software in keyword *OUTBOARD, the name
          of python script should NOT also have any blanks.
        """

        # Read commandline arguments.
        args = sys.argv[1:]
        if len(args) < 1:
           OB_CMG.print_msg( 0, 'Script requires host command to execute it.' )

        sim_fname = os.path.basename( args[0] ).lower()
        if '.exe' in sim_fname:
            if sim_fname[0] == 's':
                self.data['host'] = 'stars'
            elif sim_fname[0] == 'g':
                self.data['host'] = 'gem'
            elif sim_fname[0] == 'i' or sim_fname[0] == 'm':
                self.data['host'] = 'imex'
            else:
                OB_CMG.print_msg( 0, 'Simulator cannot be recognized. Please check the input command line.' )
        else:
            OB_CMG.print_msg( 0, 'Simulator cannot be recognized. (.exe) is required in simulator file name.' )

        ob_software_name = Path( sys.argv[0] ).name[:-3].strip().lower()
        if len(ob_software_name.split()) > 1:
            OB_CMG.print_msg( 0, 'No space is allowed in python script file name.' )

        is_dd_given = False
        wd_dir   = ''
        out_dir  = ''
        out_name = ''
        crdat    = ''
        for i, arg in enumerate(args):
            if arg[0:2].lower() == '-f':
                crdat = args[i+1]
                dat_dir = str( Path(crdat).parent )
            elif arg[0:2].lower() == '-o' and arg.lower() != '-obup_debug':
                out_dir  = str( Path(args[i+1]).parent )
                out_name = Path(args[i+1]).name
            elif arg[0:3].lower() == '-wd':
                wd_dir = args[i+1]
            elif arg[0:3].lower() == '-dd':
                is_dd_given = True

        if wd_dir:
            if wd_dir == '.': wd_dir = os.getcwd()
            self.data['wd'] = wd_dir
        elif out_dir:
            if out_dir == '.': out_dir = os.getcwd()
            self.data['wd'] = out_dir
        elif is_dd_given:
            if dat_dir == '.': dat_dir = os.getcwd()
            self.data['wd'] = dat_dir
        else:
            self.data['wd'] = os.getcwd()

        if not out_name:
            self.data['crdat'] = Path(crdat).name[:-4]
        else:
            self.data['crdat'] = out_name

        self.data['Root']  = self.data['wd'] + self.data['PDelimiter'] + self.data['crdat']

        self.data['SimSFile'] = self.data['Root'] + '.' + self.data['host'] + '.sgnl'
        self.data['SimDFile'] = self.data['Root'] + '.' + self.data['host'] + '.data'

        self.data['OBSFile'] = self.data['Root'] + '.' + ob_software_name + '.sgnl'
        self.data['OBDFile'] = self.data['Root'] + '.' + ob_software_name + '.data'

        command = ' '.join(f'"{arg}"' for arg in args)

        if '-LOG' in command.upper():
            self.data['LogExists'] = True
        else:
            self.data['LogExists'] = False
            if self.data['Platform'] == 'win':
                command = '"cmd" "/K" ' + command
            elif self.data['Platform'] == 'lin':
                command += ' -log'

        self.data['HostCommand'] = command

        self.data['HostExeName'] = '"' + args[0] + '"'

        OB_CMG.print_msg( 1, 'Simulator signal file: ' + self.data['SimSFile'] )
        OB_CMG.print_msg( 1, 'Simulator data   file: ' + self.data['SimDFile'] )
        OB_CMG.print_msg( 1, 'Outboard  signal file: ' + self.data['OBSFile'] )
        OB_CMG.print_msg( 1, 'Outboard  data   file: ' + self.data['OBDFile'] )
        OB_CMG.print_msg( 1, 'Commandline arguments parsed.' )

    def initialize(self):
        """
        - Change working directory.
        - Delete host-outboard coupling files from previous runs.
        """

        # Delete already existing host to outboard files.
        if os.path.isfile( self.data['SimSFile'] ):
            os.remove( self.data['SimSFile'] )
        if os.path.isfile( self.data['SimDFile'] ):
            os.remove( self.data['SimDFile'] )

        # Delete already existing outboard to host files.
        if os.path.isfile( self.data['OBSFile'] ):
            os.remove( self.data['OBSFile'] )
        if os.path.isfile( self.data['OBDFile'] ):
            os.remove( self.data['OBDFile'] )

        if self.read_dat_file is not None:
            self.dat_file_data = self.read_dat_file( self.data['Root'] + '.dat' )

        self.last_handshake = -1

        OB_CMG.print_msg( 1, 'Coupling initialization done.' )

    def run_host(self):
        """
        Run host as a separate detached process
        """

        try:
            if self.data['Platform'] == 'win':
                proc = subprocess.Popen( self.data['HostCommand'], \
                                         shell=(not self.data['LogExists']), \
                                         creationflags=subprocess.DETACHED_PROCESS )
            elif self.data['Platform'] == 'lin':
                proc = subprocess.Popen( self.data['HostCommand'].split() )

            OB_CMG.print_msg( 1, 'Host started running (' + f'PID = {proc.pid}'.center(15) + ').' )
            self.data['Host_PROC'] = proc
        except Exception as e:
            OB_CMG.print_msg( 0, f'({sys.exc_info()[0]}): Host could not start running.' )

    def is_SimSFile_exists(self):
        """
        Outboard sleeps and waits for host signal file to be created
        """

        ob_sleep_time_end = time.time() + self.ob_max_sleep_time
        while True:
            if not (self.data['Host_PROC'].poll() is None):
                OB_CMG.print_msg( 0, 'Host is not running. Please check host output files.' )
            elif os.path.isfile( self.data['SimSFile'] ):
                return True
            elif self.last_handshake == -1:
                continue
            elif time.time() >= ob_sleep_time_end:
                break
        return False

    def engage(self):
        """
        Performs the coupling process between host and outboard
        """

        l_host_running = False

        while self.is_SimSFile_exists():
            if not l_host_running:
                OB_CMG.print_msg( 1, 'Coupling process started ...\n' )
                l_host_running = True
            with open(self.data['SimSFile'], mode='r') as handle:
                sim_sgnl_info = handle.read().split()

            if len(sim_sgnl_info) == 0:
                continue
            elif int(sim_sgnl_info[1]) == -100:
                OB_CMG.print_msg( 2, self.data['host'].upper() + ' terminated normally.' )
            elif int(sim_sgnl_info[1]) == -300:
                OB_CMG.print_msg( 0, self.data['host'].upper() + ' terminated abnormally.' )
            elif int(sim_sgnl_info[0]) > self.last_handshake:
                sim_data = self.read_simulation_results( self.data['SimDFile'] )
                self.ob_compute( int(sim_sgnl_info[0]), self.data['OBSFile'], self.data['OBDFile'], self.dat_file_data, sim_data )
                self.last_handshake = int(sim_sgnl_info[0])
            else:
                self.last_handshake = int( sim_sgnl_info[0] )

        OB_CMG.print_msg( 0, 'Not able to find host signal (*.sgnl) file, terminated.' )

    def run(self):
        """
        Main method that should be called by user after instantiation of the class
        """

        OB_CMG.print_header()
        try:
            self.check_arg()
            self.initialize()
            self.run_host()
            self.engage()
        except KeyboardInterrupt as e:
            OB_CMG.print_msg( 1, 'User cancelled the run.' )
        finally:
            if not self.data:
                pass
            elif self.data['Host_PROC'].poll() is None:
                try:
                    if self.data['Platform'] == 'win':
                        completed = subprocess.run('taskkill /f /im '+self.data['HostExeName'], shell=True)
                    elif self.data['Platform'] == 'lin':
                        completed = subprocess.run('kill -9 '+self.data['Host_PROC'].pid, shell=True)
                except:
                    pass
                OB_CMG.print_msg( 2, 'Host run was terminated.' )
            os._exit(0)
