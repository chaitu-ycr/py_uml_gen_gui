"""Python 🐍 UML diagrams generator GUI"""

__version__ = "0.0.1"

# Import Python Libraries here
import os
import sys
import logging
from logging import handlers

# log initialisation and configuration
log = logging.getLogger('PY_UML_GEN_GUI_LOG')
py_uml_gen_gui_log_dir = r'D:\.py_logs'
if not os.path.exists(py_uml_gen_gui_log_dir):
    os.mkdir(py_uml_gen_gui_log_dir)
log.setLevel(logging.DEBUG)
log_format = logging.Formatter("%(asctime)s [PY_UML_GEN_GUI_LOG] [%(levelname)-5.5s]  %(message)s")
ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(log_format)
log.addHandler(ch)
fh = handlers.RotatingFileHandler(fr'{py_uml_gen_gui_log_dir}\py_uml_gen_gui.log', maxBytes=(1048576 * 5), backupCount=7)
fh.setFormatter(log_format)
log.addHandler(fh)


class PyUmlGenGui:
    r"""The PyUmlGenGui class represents python UML diagrams generator.
    """

    def __init__(self) -> None:
        pass
