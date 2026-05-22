class ErrorHandler:
    def recover(self, error, context):
        context.warn("recover", str(error))
        return None
