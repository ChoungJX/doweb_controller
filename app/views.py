from app import app
from flask import url_for, request, redirect, render_template,jsonify,current_app,make_response


from . import apis



@app.route('/server/api',methods=['POST'])
def api():
    if request.json.get('api'):
        callback = route_api.get(request.json.get('api'))
        return callback(request)

    return jsonify({"ststus":0,"message":"no api"})

route_api = {
    "check_status" : apis.check_status,
    "docker_images" : apis.send_docker_images_info,
    "docker_ps" : apis.send_docker_ps_info,
    "docker_pull" : apis.pull_new_images,
    "docker_rmi" : apis.del_images,
    "docker_rm" : apis.del_container,
    "docker_run" : apis.create_container,
    "docker_commit" : apis.commit_image,
}

