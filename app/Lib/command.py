import subprocess
import json
import os


def send_message(cm) -> subprocess.Popen:
    thr = subprocess.Popen(
        cm, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return thr


def use_docker_sock(args_dict: dict, api_version: str) -> subprocess.Popen:
    #elementary_command = "curl -s"
    elementary_command = ["curl", "-s"]

    if args_dict['method'] != "GET":
        # elementary_command = "%s -X %s" % (
        #     elementary_command, args_dict['method']
        # )
        elementary_command.append("-X")
        elementary_command.append(args_dict['method'])
    else:
        pass
    if args_dict.get('data'):
        # elementary_command = '%s -H \"Content-Type: application/json\" -X POST  --data \'%s\'' % (
        #     elementary_command, json.dumps(args_dict.get('data'))
        # )
        elementary_command.append("--header")
        elementary_command.append('"Content-Type:application/json"')
        elementary_command.append("--data")
        elementary_command.append("'"+json.dumps(args_dict.get('data'))+"'")

    # elementary_command = "%s --unix-socket /var/run/docker.sock http://localhost%s" % (
    #     elementary_command, args_dict['url']
    # )
    elementary_command.append("--unix-socket")
    elementary_command.append("/var/run/docker.sock")
    elementary_command.append("http://localhost/%s%s" % (api_version, args_dict['url']))
    elementary_command = " ".join(elementary_command)
    print(elementary_command)
    get_thr = send_message(elementary_command)
    return get_thr



if __name__ == "__main__":
    # docker_run({"image":"aaa","args":"/bin/bash","ports":[[443,443],[80,80],[22,22]],"name":"test","restart":"always","communicate":"23423"})
    # docker_inspect("sadfaf242r23")
    #aaa = docker_network({})
    #import pdb; pdb.set_trace()
    pass
