"""Flow - general-purpose HTTP framework for those, who want solid foundation of their application.

Framework was build around concepts of Spring Framework, which allowed without any import statements
write pretty and solid applications which futher could be used and extended in different ways. Framework
builded around same idea and provides interface for performing same concepts as in spring.

There is several decorators and tools, that might help get You started. For more information: see official
documentation at <https://docs.the-omnia.ru/flow>

Version.
--------
0.1.0

Copyright.
----------
Omnia Community 2024

License.
--------
Omnia Closed Source License Revision 1
"""

__all__ = (
    "Configuration",
    "Middleware",
    "SecurityMiddleware",
    "FlowServer",
    "FlowServerState",
    "FlowWorker",
)

__version__ = "0.1.0"

from .configuration import Configuration
from .server import FlowServer
from .server import FlowServerState
from .worker import FlowWorker
