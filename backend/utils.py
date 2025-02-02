def generate_starting_prompt(child_name, prompt_type, *user_prompt):
    if prompt_type == "test":
        return f"A child named {child_name} will be having {user_prompt[0]} soon. They do not understand what {user_prompt[0]} is, explain it to them."
    elif prompt_type == "diagnosis":
        return f"A child named {child_name} has been diagnosed with {user_prompt[0]}. They do not understand what {user_prompt[0]} is, explain it to them. Introduce the disease using the main 2 symptoms that they would be experiencing and then explain what the disease is."
    elif prompt_type == "day_in_life":
        return f"A child named {child_name} has been diagnosed with {user_prompt[0]}. They need to know what a day in their life may look like with {user_prompt[0]}. Please explain this to them."
    elif prompt_type == "treatment":
        return f"A child named {child_name} has been diagnosed with {user_prompt[0]}. They will be receiving {user_prompt[1]}. They do not understand what this means. Explain to them what {user_prompt[1]} is including how they would take the medication."
    elif prompt_type == "red_flags":
        return f"A child named {child_name} has been diagnosed with {user_prompt[0]}. They need to know 3 main red flags or complications that they need to look out for. They also need to know what they, as a child, should do if these red flags happen. (e.g. tell a parent)"
