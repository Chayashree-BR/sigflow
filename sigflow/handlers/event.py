class EventHandler:
    def handle(self, frame, context):
        context.logger.info("frame stream=%s sequence=%s size=%s", frame.stream_id, frame.sequence, frame.size)
        return frame
