import os
import inp
import StringIO

from inp import templating

def get_path_for(fname):
    path = os.path.dirname(os.path.abspath(inp.__file__))
    return os.path.join(path, fname)


def get_filelike(fname):
    with open(get_path_for(fname), 'rb') as f:
        filelike = StringIO.StringIO(f.read())
        filelike.name = 'install_script'
        return filelike


def install_script(script):
    return get_filelike(script)


def nodepool_config(cloud_env):
    nodepool_config_template = get_filelike('nodepool.yaml').read()
    nodepool_config = templating.bash_style_replace(cloud_env, nodepool_config_template)
    nodepool_config_file = StringIO.StringIO(nodepool_config)
    nodepool_config_file.name = 'nodepool.yaml'
    return nodepool_config_file

def secure_config(cloud_env):
    # keep it to be env replacible enven though it's not use currently.
    secure_config_template = get_filelike('secure.conf').read()
    secure_config = templating.bash_style_replace(cloud_env, secure_config_template)
    secure_config_file = StringIO.StringIO(secure_config)
    secure_config_file.name = 'secure.conf'
    return secure_config_file
