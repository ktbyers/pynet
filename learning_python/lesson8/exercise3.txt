
########

a. Using the same 'test_venv' that you created in exercise2. Install netmiko version 2.0.1. Verify
this version is installed by executing the following from the Python shell

>>> import netmiko
>>> netmiko.__version__
'2.0.1'


b. Using pip upgrade your version of Netmiko to the latest version.

c. Deactivate your virtual environment. See 'which python' is now being used.

########



# Install Netmiko 2.0.1

$ pip install netmiko==2.0.1
Collecting netmiko==2.0.1
Requirement already satisfied: scp>=0.10.0 in ./test_venv/lib/python3.6/site-packages (from netmiko==2.0.1)
Requirement already satisfied: paramiko>=2.0.0 in ./test_venv/lib/python3.6/site-packages (from netmiko==2.0.1)
Requirement already satisfied: textfsm in ./test_venv/lib/python3.6/site-packages (from netmiko==2.0.1)
Requirement already satisfied: pyserial in ./test_venv/lib/python3.6/site-packages (from netmiko==2.0.1)
Requirement already satisfied: pyyaml in ./test_venv/lib/python3.6/site-packages (from netmiko==2.0.1)
Requirement already satisfied: pyasn1>=0.1.7 in ./test_venv/lib/python3.6/site-packages (from paramiko>=2.0.0->netmiko==2.0.1)
Requirement already satisfied: cryptography>=1.5 in ./test_venv/lib/python3.6/site-packages (from paramiko>=2.0.0->netmiko==2.0.1)
Requirement already satisfied: bcrypt>=3.1.3 in ./test_venv/lib/python3.6/site-packages (from paramiko>=2.0.0->netmiko==2.0.1)
Requirement already satisfied: pynacl>=1.0.1 in ./test_venv/lib/python3.6/site-packages (from paramiko>=2.0.0->netmiko==2.0.1)
Requirement already satisfied: six>=1.4.1 in ./test_venv/lib/python3.6/site-packages (from cryptography>=1.5->paramiko>=2.0.0->netmiko==2.0.1)
Requirement already satisfied: idna>=2.1 in ./test_venv/lib/python3.6/site-packages (from cryptography>=1.5->paramiko>=2.0.0->netmiko==2.0.1)
Requirement already satisfied: cffi>=1.7; platform_python_implementation != "PyPy" in ./test_venv/lib/python3.6/site-packages (from cryptography>=1.5->paramiko>=2.0.0->netmiko==2.0.1)
Requirement already satisfied: asn1crypto>=0.21.0 in ./test_venv/lib/python3.6/site-packages (from cryptography>=1.5->paramiko>=2.0.0->netmiko==2.0.1)
Requirement already satisfied: pycparser in ./test_venv/lib/python3.6/site-packages (from cffi>=1.7; platform_python_implementation != "PyPy"->cryptography>=1.5->paramiko>=2.0.0->netmiko==2.0.1)
Installing collected packages: netmiko
  Found existing installation: netmiko 2.1.0
    Uninstalling netmiko-2.1.0:
      Successfully uninstalled netmiko-2.1.0
Successfully installed netmiko-2.0.1


# Verify Netmiko version

$ python
Python 3.6.2 (default, Feb 19 2018, 21:58:17) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-11)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import netmiko
>>> netmiko.__version__
'2.0.1'



# Using pip upgrade your version of Netmiko to the latest version.

$ pip install --upgrade netmiko
Collecting netmiko
Requirement already up-to-date: paramiko>=2.0.0 in ./test_venv/lib/python3.6/site-packages (from netmiko)
Requirement already up-to-date: pyyaml in ./test_venv/lib/python3.6/site-packages (from netmiko)
Requirement already up-to-date: scp>=0.10.0 in ./test_venv/lib/python3.6/site-packages (from netmiko)
Requirement already up-to-date: pyserial in ./test_venv/lib/python3.6/site-packages (from netmiko)
Requirement already up-to-date: textfsm in ./test_venv/lib/python3.6/site-packages (from netmiko)
Requirement already up-to-date: cryptography>=1.5 in ./test_venv/lib/python3.6/site-packages (from paramiko>=2.0.0->netmiko)
Requirement already up-to-date: pyasn1>=0.1.7 in ./test_venv/lib/python3.6/site-packages (from paramiko>=2.0.0->netmiko)
Requirement already up-to-date: bcrypt>=3.1.3 in ./test_venv/lib/python3.6/site-packages (from paramiko>=2.0.0->netmiko)
Requirement already up-to-date: pynacl>=1.0.1 in ./test_venv/lib/python3.6/site-packages (from paramiko>=2.0.0->netmiko)
Requirement already up-to-date: cffi>=1.7; platform_python_implementation != "PyPy" in ./test_venv/lib/python3.6/site-packages (from cryptography>=1.5->paramiko>=2.0.0->netmiko)
Requirement already up-to-date: asn1crypto>=0.21.0 in ./test_venv/lib/python3.6/site-packages (from cryptography>=1.5->paramiko>=2.0.0->netmiko)
Requirement already up-to-date: idna>=2.1 in ./test_venv/lib/python3.6/site-packages (from cryptography>=1.5->paramiko>=2.0.0->netmiko)
Requirement already up-to-date: six>=1.4.1 in ./test_venv/lib/python3.6/site-packages (from cryptography>=1.5->paramiko>=2.0.0->netmiko)
Requirement already up-to-date: pycparser in ./test_venv/lib/python3.6/site-packages (from cffi>=1.7; platform_python_implementation != "PyPy"->cryptography>=1.5->paramiko>=2.0.0->netmiko)
Installing collected packages: netmiko
  Found existing installation: netmiko 2.0.1
    Uninstalling netmiko-2.0.1:
      Successfully uninstalled netmiko-2.0.1
Successfully installed netmiko-2.1.0



# Verify Netmiko version
$ python
Python 3.6.2 (default, Feb 19 2018, 21:58:17) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-11)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import netmiko
>>> netmiko.__version__
'2.1.0'



# Deactivate your virtual environment. See 'which python' is now being used?

(test_venv) [user@host VENV]$ deactivate
[user@host VENV]$ which python
/usr/bin/python

