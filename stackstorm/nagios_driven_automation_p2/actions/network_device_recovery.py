import time
from st2common.runners.base_action import Action
from nornir import InitNornir
from nornir.core.task import Result
from netmiko import redispatch
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


__all__ = ["NetVmDown"]

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class NetVmDown(Action):
    def run(self, down_device):
        print(f"Attempting to recover {down_device}...")

        console_conn = f"{down_device.split('.')[0]}_console"
        nr = InitNornir(
            config_file="/opt/stackstorm/packs/super_cool_python/nornir/config.yaml"
        )
        nr = nr.filter(name=console_conn)
        result = nr.run(self.reset_cfg)
        results = [down_device, result]
        print(f"Device {down_device} is recovered?: {not result.failed}")
        return (not result.failed, results)

    def reset_cfg(self, task):
        task.host.open_connection("netmiko", None)
        conn = task.host.connections["netmiko"].connection
        conn.find_prompt()
        print("Connected to terminal server or KVM host...")

        conn.write_channel(f"telnet localhost {task.host['console_port']}")
        time.sleep(0.5)
        conn.write_channel("\r\n")
        time.sleep(0.5)

        for k, v in task.host["end_host_args"].items():
            if k != "device_type":
                setattr(conn, k, v)

        conn.telnet_login()
        redispatch(conn, task.host["end_host_args"]["device_type"])
        conn.find_prompt()
        conn.enable()
        print(f"Redispatched to {task.host}")

        cfg_check = conn.send_command(
            f"dir {task.host['filesystem']}:/{task.host['default_cfg']}",
            strip_prompt=False,
            strip_command=False,
        )
        if "No such file" in cfg_check:
            print(f"{task.host['default_cfg']} is not in {task.host['filesystem']}")
            raise ValueError(f"Default config file not found")

        cfg_replace = conn.send_command(
            f"{task.host['default_cfg_cmd']} {task.host['filesystem']}:/{task.host['default_cfg']}",
            strip_prompt=False,
            strip_command=False,
        )
        if "Rollback failed." in cfg_replace:
            failed = True
            print(f"{task.host} configuration replace failed. Output: {cfg_replace}")
        else:
            failed = False
            conn.save_config()
            print(f"{task.host} configuration replaced and config saved")

        return Result(host=task.host, result=cfg_replace, changed=True, failed=failed)
