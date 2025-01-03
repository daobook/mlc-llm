import inspect
if not hasattr(inspect, 'getargspec'): # 修复
    inspect.getargspec = inspect.getfullargspec
from taolib.flows.tasks import sites

namespace = sites('docs', target='docs/_build/html')
