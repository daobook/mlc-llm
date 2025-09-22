import inspect
if not hasattr(inspect, 'getargspec'): # 修复
    inspect.getargspec = inspect.getfullargspec
import sys
from invoke import task
from taolib.flows.tasks import sites

# @task
# def make(ctx):
#     """构建 mlc_llm 库"""
#     # create build directory
#     cmd = "cd .. && mkdir -p build && cd build"
#     # generate build configuration
#     # cmd += f"&&{sys.executable} ../cmake/gen_cmake_config.py"
#     cmd += f"&&cp ../xinetzone/config.cmake ."
#     # build mlc_llm libraries
#     cmd += "&&cmake -G Ninja .. && cmake --build . --parallel $(nproc) && cd .."
#     ctx.run(cmd)

@task
def install(ctx):
    """安装 mlc_llm Python 包"""
    ctx.run("pip install -ve ..")
    ctx.run("pip install -e .[doc,dev]")

namespace = sites('../docs', target='../docs/_build/html')
# namespace.add_task(make)
namespace.add_task(install)
