class IrCodeReader(object):

    def get_ir_code(self) -> int:
        raise NotImplementedError


class CannotGetIrException(Exception):
    pass
