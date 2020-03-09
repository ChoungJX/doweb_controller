import json

from flask import jsonify, request

from app import app

from .Lib import command


def check_status(request):
    get_thr = command.docker_image()
    get_thr.wait()
    return jsonify(
        {
            "status": get_thr.poll(),
        }
    )


def docker_socks(request):
    get_thr = command.use_docker_sock(request.json)
    get_thr.wait()

    try:
        output = get_thr.stdout.read().decode()
        data = json.loads(output)
    except:
        data = output 

    return jsonify(
        {
            'status': get_thr.poll(),
            'data': data,
        }
    )


def send_docker_images_info(request):

    get_thr = command.docker_image()
    get_thr.wait()

    return_json = {
        "images": []
    }

    get_out = get_thr.stdout.readlines()
    get_out = get_out[1:]
    for i in get_out:
        one_image_list = list()
        one_data = i.decode()
        one_data = one_data.split("  ")
        for j in one_data:
            if j:
                one_image_list.append(j.strip())

        get_thr2 = command.docker_inspect(one_image_list[2])
        get_thr2.wait()
        one_image_info = json.loads(get_thr2.stdout.read())

        return_json["images"].append(one_image_info[0])

    return_json["status"] = get_thr.poll()
    return jsonify(return_json)


def send_docker_ps_info(request):

    get_args = request.json.get("args")
    if get_args:
        get_thr = command.docker_ps(get_args)
    else:
        get_thr = command.docker_ps([])
    get_thr.wait()

    return_json = {
        "containers": list()
    }

    get_out = get_thr.stdout.readlines()
    get_out = get_out[1:]
    for i in get_out:
        one_container_list = list()
        one_data = i.decode().split("  ")

        get_thr2 = command.docker_inspect(one_data[0].strip())
        get_thr2.wait()
        one_container_info = json.loads(get_thr2.stdout.read())

        return_json["containers"].append(one_container_info[0])
    return_json["status"] = get_thr.poll()
    return jsonify(return_json)


def pull_new_images(request):

    get_args = request.json.get("args")
    if get_args:
        get_thr = command.docker_pull(get_args)
    else:
        return jsonify({"status": -1})

    get_thr.wait()
    return jsonify(
        {
            "status": get_thr.poll(),
            "message": get_thr.stdout.read().decode().strip()
        }
    )


def del_images(request):

    get_args = request.json.get("args")
    if get_args:
        get_thr = command.docker_rmi(get_args)
    else:
        return jsonify({"status": -1})

    get_thr.wait()
    return jsonify(
        {
            "status": get_thr.poll(),
            "message": get_thr.stdout.read().decode().strip()
        }
    )


def del_container(request):

    get_args = request.json.get("args")
    if get_args:
        get_thr = command.docker_rm(get_args)
    else:
        return jsonify({"status": -1})

    get_thr.wait()
    return jsonify(
        {
            "status": get_thr.poll(),
            "message": get_thr.stdout.read().decode().strip()
        }
    )


def create_container(request):

    get_args = request.json.get("args")
    if get_args:
        get_thr = command.docker_run(get_args)
    else:
        return jsonify({"status": -1})

    get_thr.wait()
    return jsonify(
        {
            "status": get_thr.poll(),
            "message": get_thr.stdout.read().decode().strip()
        }
    )


def commit_image(request):

    get_args = request.json.get("args")
    if get_args:
        get_thr = command.docker_commit(get_args)
    else:
        return jsonify({"status": -1})

    get_thr.wait()
    return jsonify(
        {
            "status": get_thr.poll(),
            "message": get_thr.stdout.read().decode().strip()
        }
    )


def network_option(request):

    get_args = request.json.get("args")

    if get_args.get('option') == "ls":
        get_thr = command.docker_network(get_args)
        get_thr.wait()

        return_json = {
            'network': list(),
        }

        get_out = get_thr.stdout.readlines()
        get_out = get_out[1:]
        for i in get_out:
            one_network_list = list()
            one_data = i.decode()
            one_data = one_data.split("  ")
            for j in one_data:
                if j:
                    one_network_list.append(j.strip())

            get_thr2 = command.docker_inspect(one_network_list[0])
            get_thr2.wait()
            one_image_info = json.loads(get_thr2.stdout.read())

            return_json["network"].append(one_image_info[0])

        return_json["status"] = get_thr.poll()
        return jsonify(return_json)

    else:
        return jsonify({"status": -1})
