import autogen

config_list = [
    {
        'model': 'gpt-4',
        'api_key': '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'
    }
]

llm_config ={
    "request_timeout": 300,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0, #0-1 the higher the temperature, the more creative

}

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config
)

user_proxy = autogen.UserProxyAgent(
    name="user-proxy",
    human_input_mode="TERMINATE", 
    # Three modes: "TERMINATE", "ALWAYS", "NEVER"
    # "TERMINATE" agents only prompt for human input only when termination message i received
    # "ALWAYS" agents prompt for human input every time a message is received
    # "NEVER agents will never prompt for human input 
    max_consecutive_auto_reply=10,
    # maximum number of agents talking to each other
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    # looks for keyword("TERMINATE") to end the task
    code_execution_config={"work_dir": "web"},
    # when code is executed, (set working directory to web folder)
    llm_config = llm_config,
    system_message ="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task = """
Give me a summary of this article:
"""

user_proxy.initate_chat(
    assistant,
    message = task
)