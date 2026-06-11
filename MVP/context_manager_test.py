from intelligence.context_manager import ContextManager


# Create Context Manager object
context = ContextManager()


# Create a new session
context.create_session("session_001")


# Add conversation
context.add_conversation(
    "session_001",
    "How to troubleshoot OIM scheduler issue?",
    "Check scheduler logs and database connectivity."
)


# Update environment details
context.update_environment(
    "session_001",
    {
        "product": "OIM 12c",
        "database": "Oracle",
        "server": "WebLogic"
    }
)


# Display complete context
print("JANVIQ AI Context:")
print(context.get_context("session_001"))