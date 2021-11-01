import pkg_resources

from .board import ConwayBoard, ConwayBoard3C, ConwayBoard3D
from .canvan import ConwayCanvan
from .simulator import Simulator


__author__ = "jelambrar96 <jelambrar@gmail.com>"
__version__ = pkg_resources.get_distribution("pyconway").version
