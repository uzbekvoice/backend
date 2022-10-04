from .messages import messages


class ViewKit:
    """View KIT is a set of views to keep DRY principle"""
    def get_query_manager(self):
        """Method to get Query manager of User models"""
        return self.model.objects  # noqa

    @classmethod
    def build_response(cls, status_code, result):
        """Method to build full response"""
        return {
            "message": messages[status_code],
            "result": result
        }
