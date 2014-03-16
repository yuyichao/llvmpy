from binding import *
from ..namespace import llvm
from ..Module import Module
from ..Value import Function

if LLVM_VERSION >= (3, 5):
    llvm.includes.add('llvm/IR/Verifier.h')
else:
    llvm.includes.add('llvm/Analysis/Verifier.h')

VerifierFailureAction = llvm.Enum('VerifierFailureAction',
                                  '''AbortProcessAction
                                     PrintMessageAction
                                     ReturnStatusAction''')

verifyModule = llvm.CustomFunction('verifyModule',
                                   'llvm_verifyModule',
                                   PyObjectPtr,  # boolean -- failed?
                                   ref(Module),
                                   VerifierFailureAction,
                                   PyObjectPtr,       # errmsg
                                   )

verifyFunction = llvm.Function('verifyFunction',
                               cast(Bool, bool),  # failed?
                               ref(Function),
                               VerifierFailureAction)
