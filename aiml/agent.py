from planner import decide_next_action
from tools import create_candidate_profile, schedule_meeting

def run_agent(goal):
    observation = ""

    while True:
        decision = decide_next_action(goal, observation)

        if decision["action"] == "finish":
            return "✅ Onboarding completed"

        if decision["action"] == "create_candidate_profile":
            result = create_candidate_profile(decision["input"])
        elif decision["action"] == "schedule_meeting":
            result = schedule_meeting(decision["input"])

        observation += " " + result
