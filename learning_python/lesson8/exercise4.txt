
##########

a. Activate your 'test_venv' virtual environment

b. Use pip to uninstall the Netmiko library

c. Verify Netmiko is no longer installed

d. Use pip to install the 'develop' branch of Netmiko.

##########


# Activate your 'test_venv' virtual environment

$ source test_venv/bin/activate
(test_venv) [user@host VENV]$ 



# Use pip to uninstall the Netmiko library

$ pip uninstall netmiko
Uninstalling netmiko-2.1.0:
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko-2.1.0.dist-info/DESCRIPTION.rst
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko-2.1.0.dist-info/INSTALLER
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko-2.1.0.dist-info/METADATA
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko-2.1.0.dist-info/RECORD
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko-2.1.0.dist-info/WHEEL
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko-2.1.0.dist-info/metadata.json
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko-2.1.0.dist-info/top_level.txt
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/__pycache__/base_connection.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/__pycache__/cisco_base_connection.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/__pycache__/netmiko_globals.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/__pycache__/py23_compat.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/__pycache__/scp_functions.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/__pycache__/scp_handler.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/__pycache__/snmp_autodetect.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/__pycache__/ssh_autodetect.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/__pycache__/ssh_dispatcher.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/__pycache__/ssh_exception.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/__pycache__/utilities.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/_textfsm/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/_textfsm/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/_textfsm/__pycache__/_clitable.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/_textfsm/__pycache__/_terminal.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/_textfsm/__pycache__/_texttable.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/_textfsm/_clitable.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/_textfsm/_terminal.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/_textfsm/_texttable.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/a10/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/a10/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/a10/__pycache__/a10_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/a10/a10_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/accedian/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/accedian/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/accedian/__pycache__/accedian_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/accedian/accedian_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/alcatel/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/alcatel/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/alcatel/__pycache__/alcatel_aos_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/alcatel/__pycache__/alcatel_sros_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/alcatel/alcatel_aos_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/alcatel/alcatel_sros_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/arista/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/arista/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/arista/__pycache__/arista_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/arista/arista_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/aruba/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/aruba/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/aruba/__pycache__/aruba_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/aruba/aruba_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/avaya/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/avaya/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/avaya/__pycache__/avaya_ers_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/avaya/__pycache__/avaya_vsp_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/avaya/avaya_ers_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/avaya/avaya_vsp_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/base_connection.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/brocade/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/brocade/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/brocade/__pycache__/brocade_netiron.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/brocade/__pycache__/brocade_nos_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/brocade/brocade_netiron.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/brocade/brocade_nos_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/calix/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/calix/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/calix/__pycache__/calix_b6_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/calix/calix_b6_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/checkpoint/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/checkpoint/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/checkpoint/__pycache__/checkpoint_gaia_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/checkpoint/checkpoint_gaia_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/ciena/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/ciena/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/ciena/__pycache__/ciena_saos_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/ciena/ciena_saos_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/cisco/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/cisco/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/cisco/__pycache__/cisco_asa_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/cisco/__pycache__/cisco_ios.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/cisco/__pycache__/cisco_nxos_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/cisco/__pycache__/cisco_s300.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/cisco/__pycache__/cisco_tp_tcce.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/cisco/__pycache__/cisco_wlc_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/cisco/__pycache__/cisco_xr_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/cisco/cisco_asa_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/cisco/cisco_ios.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/cisco/cisco_nxos_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/cisco/cisco_s300.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/cisco/cisco_tp_tcce.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/cisco/cisco_wlc_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/cisco/cisco_xr_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/cisco_base_connection.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/coriant/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/coriant/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/coriant/__pycache__/coriant_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/coriant/coriant_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/dell/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/dell/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/dell/__pycache__/dell_force10_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/dell/__pycache__/dell_powerconnect.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/dell/dell_force10_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/dell/dell_powerconnect.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/eltex/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/eltex/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/eltex/__pycache__/eltex_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/eltex/eltex_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/enterasys/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/enterasys/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/enterasys/__pycache__/enterasys_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/enterasys/enterasys_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/extreme/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/extreme/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/extreme/__pycache__/extreme_exos.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/extreme/__pycache__/extreme_wing_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/extreme/extreme_exos.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/extreme/extreme_wing_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/f5/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/f5/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/f5/__pycache__/f5_ltm_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/f5/f5_ltm_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/fortinet/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/fortinet/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/fortinet/__pycache__/fortinet_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/fortinet/fortinet_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/hp/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/hp/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/hp/__pycache__/hp_comware_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/hp/__pycache__/hp_procurve_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/hp/hp_comware_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/hp/hp_procurve_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/huawei/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/huawei/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/huawei/__pycache__/huawei_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/huawei/huawei_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/juniper/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/juniper/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/juniper/__pycache__/juniper_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/juniper/juniper_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/linux/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/linux/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/linux/__pycache__/linux_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/linux/linux_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/mellanox/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/mellanox/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/mellanox/__pycache__/mellanox_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/mellanox/mellanox_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/mrv/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/mrv/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/mrv/__pycache__/mrv_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/mrv/mrv_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/netapp/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/netapp/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/netapp/__pycache__/netapp_cdot_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/netapp/netapp_cdot_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/netmiko_globals.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/ovs/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/ovs/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/ovs/__pycache__/ovs_linux_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/ovs/ovs_linux_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/paloalto/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/paloalto/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/paloalto/__pycache__/paloalto_panos_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/paloalto/paloalto_panos_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/pluribus/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/pluribus/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/pluribus/__pycache__/pluribus_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/pluribus/pluribus_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/py23_compat.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/quanta/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/quanta/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/quanta/__pycache__/quanta_mesh_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/quanta/quanta_mesh_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/ruckus/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/ruckus/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/ruckus/__pycache__/ruckus_fastiron.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/ruckus/ruckus_fastiron.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/scp_functions.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/scp_handler.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/snmp_autodetect.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/ssh_autodetect.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/ssh_dispatcher.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/ssh_exception.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/terminal_server/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/terminal_server/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/terminal_server/__pycache__/terminal_server.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/terminal_server/terminal_server.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/ubiquiti/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/ubiquiti/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/ubiquiti/__pycache__/edge_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/ubiquiti/edge_ssh.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/utilities.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/vyos/__init__.py
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/vyos/__pycache__/__init__.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/vyos/__pycache__/vyos_ssh.cpython-36.pyc
  /home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/vyos/vyos_ssh.py
Proceed (y/n)? y
  Successfully uninstalled netmiko-2.1.0




# Verify Netmiko is no longer installed

$ python
Python 3.6.2 (default, Feb 19 2018, 21:58:17) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-11)] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> import netmiko
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'netmiko'




# Use pip to install the 'develop' branch of Netmiko.

$ pip install git+https://github.com/ktbyers/netmiko.git@develop
Collecting git+https://github.com/ktbyers/netmiko.git@develop
  Cloning https://github.com/ktbyers/netmiko.git (to develop) to /tmp/pip-ta2vu2uf-build
Requirement already satisfied: paramiko>=2.0.0 in ./test_venv/lib/python3.6/site-packages (from netmiko==2.1.0)
Requirement already satisfied: scp>=0.10.0 in ./test_venv/lib/python3.6/site-packages (from netmiko==2.1.0)
Requirement already satisfied: pyyaml in ./test_venv/lib/python3.6/site-packages (from netmiko==2.1.0)
Requirement already satisfied: pyserial in ./test_venv/lib/python3.6/site-packages (from netmiko==2.1.0)
Requirement already satisfied: textfsm in ./test_venv/lib/python3.6/site-packages (from netmiko==2.1.0)
Requirement already satisfied: bcrypt>=3.1.3 in ./test_venv/lib/python3.6/site-packages (from paramiko>=2.0.0->netmiko==2.1.0)
Requirement already satisfied: pynacl>=1.0.1 in ./test_venv/lib/python3.6/site-packages (from paramiko>=2.0.0->netmiko==2.1.0)
Requirement already satisfied: cryptography>=1.5 in ./test_venv/lib/python3.6/site-packages (from paramiko>=2.0.0->netmiko==2.1.0)
Requirement already satisfied: pyasn1>=0.1.7 in ./test_venv/lib/python3.6/site-packages (from paramiko>=2.0.0->netmiko==2.1.0)
Requirement already satisfied: six>=1.4.1 in ./test_venv/lib/python3.6/site-packages (from bcrypt>=3.1.3->paramiko>=2.0.0->netmiko==2.1.0)
Requirement already satisfied: cffi>=1.1 in ./test_venv/lib/python3.6/site-packages (from bcrypt>=3.1.3->paramiko>=2.0.0->netmiko==2.1.0)
Requirement already satisfied: asn1crypto>=0.21.0 in ./test_venv/lib/python3.6/site-packages (from cryptography>=1.5->paramiko>=2.0.0->netmiko==2.1.0)
Requirement already satisfied: idna>=2.1 in ./test_venv/lib/python3.6/site-packages (from cryptography>=1.5->paramiko>=2.0.0->netmiko==2.1.0)
Requirement already satisfied: pycparser in ./test_venv/lib/python3.6/site-packages (from cffi>=1.1->bcrypt>=3.1.3->paramiko>=2.0.0->netmiko==2.1.0)
Installing collected packages: netmiko
  Running setup.py install for netmiko ... done
Successfully installed netmiko-2.1.0



# Verify Netmiko has been installed again

$ python
Python 3.6.2 (default, Feb 19 2018, 21:58:17) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-11)] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> import netmiko

>>> netmiko.__file__
'/home/gituser/VENV/test_venv/lib/python3.6/site-packages/netmiko/__init__.py'

>>> netmiko.__version__
'2.1.0'

