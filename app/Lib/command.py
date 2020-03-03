import subprocess


def send_message(cm:str)->subprocess.Popen:
    thr = subprocess.Popen(cm,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return thr



def docker_image()->subprocess.Popen:
    elementary_command = "docker images"
    get_thr = send_message(elementary_command)
    return get_thr

def docker_rmi(args:list)->subprocess.Popen:
    elementary_command = "docker rmi -f"
    for i in args:
        elementary_command = "%s %s"%(elementary_command,i)
    
    get_thr = send_message(elementary_command)
    return get_thr

def docker_ps(args_list:list)->subprocess.Popen:
    elementary_command = "docker ps"
    for i in args_list:
        elementary_command = "%s -%s"%(elementary_command,i)
    
    get_thr = send_message(elementary_command)
    return get_thr


def docker_pull(args_dict:dict)->subprocess.Popen:
    elementary_command = "docker pull"
    elementary_command = "%s %s"%(elementary_command,args_dict.get("image"))

    get_thr = send_message(elementary_command)
    return get_thr


def docker_run(args_dict:dict)->subprocess.Popen:
    elementary_command = "docker run"

    set_name = args_dict.get("name")
    if set_name:
        elementary_command = "%s --name %s"%(elementary_command,set_name)
    
    set_start = args_dict.get("restart")
    if set_start:
        elementary_command = "%s --restart %s"%(elementary_command,set_start)
    
    open_ports = args_dict.get("ports")
    if open_ports:
        for i in open_ports:
            elementary_command = "%s -p %s:%s"%(elementary_command,i[0],i[1])
    
    set_communication = args_dict.get("communicate")
    if set_communication:
        elementary_command = "%s -it"%(elementary_command)
    else:
        elementary_command = "%s -d"%(elementary_command)
    
    run_image = args_dict.get("image")
    elementary_command = "%s %s"%(elementary_command,run_image)

    run_args = args_dict.get("args")
    elementary_command = "%s %s"%(elementary_command, run_args)

    get_thr = send_message(elementary_command)
    return get_thr

def docker_rm(args:list)->subprocess.Popen:
    elementary_command = "docker rm -f"
    for i in args:
        elementary_command = "%s %s"%(elementary_command,i)
    
    get_thr = send_message(elementary_command)
    return get_thr

def docker_inspect(args:str)->subprocess.Popen:
    elementary_command = "docker inspect"
    elementary_command = "%s %s"%(elementary_command,args)

    get_thr = send_message(elementary_command)
    return get_thr

def docker_commit(args_dict:dict)->subprocess.Popen:
    elementary_command = "docker commit"

    get_container_id = args_dict.get("container")
    get_image_name = args_dict.get("image")

    elementary_command = "%s %s %s"%(elementary_command,get_container_id,get_image_name)

    get_thr = send_message(elementary_command)
    return get_thr


if __name__ == "__main__":
    #docker_run({"image":"aaa","args":"/bin/bash","ports":[[443,443],[80,80],[22,22]],"name":"test","restart":"always","communicate":"23423"})
    docker_inspect("sadfaf242r23")