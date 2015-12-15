from setuptools import setup


setup(
    name='inp',
    version='0.2dev',
    description='Install Nodepool',
    packages=['inp'],
    install_requires=['fabric', 'PyYaml'],
    package_data = {
        'inp': [
            'installscript.sh',
            'nodepool_config.sh',
            'osci_installscript.sh',
            'osci_release.sh',
            'update.sh',
            'secure.conf',
            'nodepool.yaml',
            'osci.config',
            'backup.sh',
            'restore.sh',
            'osci_rewrite_config.sh',
            'nodepool_rewrite_config.sh',
            'functions.sh',
        ],
    },
    entry_points = {
        'console_scripts': [
            'inp-nodepool-install = inp.scripts:nodepool_install',
            'inp-upload-keys = inp.scripts:nodepool_upload_keys',
            'inp-nodepool-configure = inp.scripts:nodepool_configure',
            'inp-nodepool-update = inp.scripts:nodepool_update',
            'inp-osci-install = inp.scripts:osci_install',
            'inp-osci-update = inp.scripts:osci_update',
            'inp-osci-start = inp.scripts:osci_start',
            'inp-osci-stop = inp.scripts:osci_stop',
            'inp-osci-backup = inp.scripts:backup',
            'inp-osci-restore = inp.scripts:restore',
            'inp-osci-status = inp.scripts:ci_status',
            'inp-osci-upload-control = inp.scripts:osci_upload_control',
            'inp-osci-rewrite-config = inp.scripts:osci_rewrite_config',
            'inp-nodepool-rewrite-config = inp.scripts:nodepool_rewrite_config',
        ]
    }
)
