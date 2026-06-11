class ContextManager:
    """
    Handles user session context for JANVIQ AI.
    """

    def __init__(self):
        """
        Initialize in-memory session storage.
        """
        self.sessions = {}

    def create_session(self, session_id):
        """
        Create a new user session.
        """
        self.sessions[session_id] = {
            "questions": [],
            "answers": [],
            "environment": {}
        }

    def add_conversation(self, session_id, question, answer):
        """
        Add question and answer to existing session.
        """
        self.sessions[session_id]["questions"].append(question)
        self.sessions[session_id]["answers"].append(answer)

    def get_context(self, session_id):
        """
        Get complete session context.
        """
        return self.sessions.get(session_id, {})

    def update_environment(self, session_id, environment):
        """
        Update user environment details.
        """
        self.sessions[session_id]["environment"] = environment