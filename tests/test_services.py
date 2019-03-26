import os

import pytest


@pytest.mark.skip(reason="No way of currently testing this without commenting aws init from services.py")
def test_read_good_procfile():
    from ecs_deployer.services import read_procfile
    procfile_path = os.path.dirname(os.path.abspath(__file__)) + '/data/sample_procfile.yml'
    print(procfile_path)

    result = read_procfile(procfile_path)

    assert result == {
        'web': {
            'command': "ddtrace-run gunicorn --pythonpath app,app/apps app.wsgi:application --workers 4 --threads 4 --preload -b 0.0.0.0:8000 --timeout 90",
            'memory': 512,
            'cpu': 256,
            'ports': ['8000:8000']
        },
        'release': {
            'command': "python --version",
            'memory': 1024,
            'cpu': 512
        }
    }
