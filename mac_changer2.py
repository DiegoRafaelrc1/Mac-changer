import subprocess
import optparse
import re

def change_mac(interfaz,new_mac):
    print("cambiando direccion mac para interfaz "+ interfaz +'to'+ new_mac)
    subprocess.call(['sudo','ifconfig',interfaz,'down'])
    subprocess.call(['sudo','ifconfig',interfaz,'hw','ether',new_mac])
    subprocess.call(['sudo','ifconfig',interfaz,'up'])

def get_arguments():
    parse = optparse.OptionParser()
    parse.add_option('-i','--interfaz',dest='interface',help='interface para cambiar direaccion mac')
    parse.add_option('-m','--new mac',dest="new_mac",help='this is for change new mac')
    (options,arguments)=parse.parse_args()
    
    if not options.interface:
        print('[-]Error  interface --help for imformation')
    elif not options.new_mac:
        print('[-]Error  interface --help for imformation')

    return options


def get_current_mac(interface):
    ifconfig_results = subprocess.check_output(['ifconfig', options.interface])
    mac_address_search_result = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_results))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print('[-]No se pudo leer la direccion mac')  

options = get_arguments()
current_mac = get_current_mac(options.interface)
print('[+]current_mac'+ str(current_mac) )
change_mac(options.interface,options.new_mac)

    