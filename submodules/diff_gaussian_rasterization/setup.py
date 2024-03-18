
from setuptools import setup
from torch.utils.cpp_extension import CUDAExtension, BuildExtension, _get_build_directory, load
import os
os.path.dirname(os.path.abspath(__file__))


name="diff_gaussian_rasterization"
build_dir = _get_build_directory(name, verbose=False)
_C = load(
    name=name,
    sources=[
            "cuda_rasterizer/rasterizer_impl.cu",
            "cuda_rasterizer/forward.cu",
            "cuda_rasterizer/backward.cu",
            "rasterize_points.cu",
            "ext.cpp"],
    extra_cuda_cflags=["-I" + os.path.join(os.path.dirname(os.path.abspath(__file__)), "third_party/glm/")],
)