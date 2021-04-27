from app import app, sql
from flask import url_for, request, redirect, render_template, jsonify, current_app, make_response


from . import apis


def certificate(request):
    psw = request.json.get('psw')
    get_c_id = sql.get_certification()
    if psw != get_c_id:
        return False
    else:
        return True


@app.route('/server/bind', methods=['POST'])
def bind_server():
    print(request.json)
    get_remote_c_id = request.json.get("psw")
    get_c_id = sql.get_certification()
    if get_c_id:
        return jsonify(
            {
                "status": -1,
                "message": "this server has binded"
            }
        )
    else:
        sql.create_certification(get_remote_c_id)
        return jsonify(
            {
                "status": 0,
                "message": "success"
            }
        )


@app.route('/server/delete', methods=['POST'])
def delete_server():
    print(request.json)
    if certificate(request):
        sql.delete_certification()
        return jsonify(
            {
                "status": 0,
                "message": "success"
            }
        )
    else:
        return jsonify(
            {
                "status": -1,
                "message": "certification wrong"
            }
        )


@app.route('/server/api', methods=['POST'])
def api():
    print(request.json)
    if not certificate(request):
        return jsonify({"ststus": -1, "message": "no certificate"})

    if request.json.get('api'):
        callback = route_api.get(request.json.get('api'))
        return callback(request)

    return jsonify({"ststus": 0, "message": "no api"})


route_api = {
    "docker_socks": apis.docker_socks,
    "check_server_status": apis.check_server_status,


    "check_status": apis.check_status,

    "docker_logs": apis.docker_get_logs,
}
