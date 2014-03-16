from binding import *
from ..namespace import llvm

@llvm.Class()
class AssemblyAnnotationWriter:
    if LLVM_VERSION >= (3, 5):
        _include_ = "llvm/IR/AssemblyAnnotationWriter.h"
    else:
        _include_ = "llvm/Assembly/AssemblyAnnotationWriter.h"
