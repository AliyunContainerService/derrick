from derrick.core.common import *
from derrick.core.detector import Detector


class PythonPakcageManager(Detector):
    def execute(self, *args, **kwargs):
        return {"package_install_command": PythonPakcageManager.get_package_install_command()}

    @staticmethod
    def get_package_install_command():
        workspace = get_workspace()
        requirements_txt = os.path.join(workspace, "requirements.txt")
        setup_py = os.path.join(workspace, "setup.py")

        if os.path.exists(requirements_txt) is True:
            return "COPY requirements.txt .\nRUN pip install -r requirements.txt"
        if os.path.exists(setup_py) is True:
            return "COPY setup.py .\nRUN python setup.py install"

        return ""
