def decide_next_action(goal, observation):
    goal = goal.lower()

    if "onboard" in goal and "profile" not in observation:
        name = goal.split()[-1]
        return {"action": "create_candidate_profile", "input": name}

    if "onboard" in goal and "meeting" not in observation:
        name = goal.split()[-1]
        return {"action": "schedule_meeting", "input": name}

    return {"action": "finish"}
