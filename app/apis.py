import json
import time

from flask import jsonify, request
import psutil

from app import app

from .Lib import command


def check_status(request):
    return jsonify(
        {
            "status": 0,
        }
    )


def docker_socks(request):
    get_api = app.config.get("DOCKER_API")
    get_thr = command.use_docker_sock(request.json, get_api)
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


def check_server_status(request):
    mem = psutil.virtual_memory()
    mem_swap = psutil.swap_memory()
    net = psutil.net_io_counters()
    data = {
        'cpu': {
            'cpu_used': psutil.cpu_percent(),
            'cpu_number': psutil.cpu_count()
        },
        'memory': {
            'total': float(mem.total) / 1024 / 1024 / 1024,
            'used': float(mem.used) / 1024 / 1024 / 1024,
            'free': float(mem.free) / 1024 / 1024 / 1024
        },
        'memory_swap': {
            'total': float(mem_swap.total) / 1024 / 1024 / 1024,
            'used': float(mem_swap.used) / 1024 / 1024 / 1024,
            'free': float(mem_swap.free) / 1024 / 1024 / 1024
        },
        'network': {
            'receive': float(net.bytes_recv),
            'send': float(net.bytes_sent),
            "time": time.time(),
        },
    }

    return jsonify(
        {
            'status': 0,
            'data': data,
        }
    )








def docker_get_logs(request):
    get_args = request.json.get("args")
    if get_args:
        get_thr = command.docker_logs(get_args)
    else:
        return jsonify({"status": -1})

    get_thr.wait()
    return jsonify(
        {
            "status": get_thr.poll(),
            "message": get_thr.stdout.read().decode().strip()
        }
    )
