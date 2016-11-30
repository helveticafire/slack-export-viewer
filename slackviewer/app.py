import flask


app = flask.Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


@app.route("/channel/<name>")
def channel_name(name):
    messages = flask._app_ctx_stack.channels[name]
    channels = list(flask._app_ctx_stack.channels.keys())
    private_channels = list(flask._app_ctx_stack.private_channels.keys())
    dms = list(flask._app_ctx_stack.dms.keys())
    return flask.render_template("viewer.html", messages=messages,
                                 name=name.format(name=name),
                                 channels=sorted(channels),
                                 private_channels=sorted(private_channels),
                                 dms=sorted(dms))

@app.route("/private-channel/<name>")
def private_channel_name(name):
    messages = flask._app_ctx_stack.private_channels[name]
    channels = list(flask._app_ctx_stack.channels.keys())
    private_channels = list(flask._app_ctx_stack.private_channels.keys())
    dms = list(flask._app_ctx_stack.dms.keys())

    return flask.render_template("viewer.html", messages=messages,
                                 name=name.format(name=name),
                                 channels=sorted(channels),
                                 private_channels=sorted(private_channels),
                                 dms=sorted(dms))


@app.route("/dm/<name>")
def dm_name(name):
    messages = flask._app_ctx_stack.dms[name]
    channels = list(flask._app_ctx_stack.channels.keys())
    private_channels = list(flask._app_ctx_stack.private_channels.keys())
    dms = list(flask._app_ctx_stack.dms.keys())
    return flask.render_template("viewer.html", messages=messages,
                                 name=name.format(name=name),
                                 channels=sorted(channels),
                                 private_channels=sorted(private_channels),
                                 dms=sorted(dms))

@app.route("/")
def index():
    channels = list(flask._app_ctx_stack.channels.keys())
    if "general" in channels:
        return channel_name("general")
    else:
        return channel_name(channels[0])
