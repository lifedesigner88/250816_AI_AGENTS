import vertexai
from vertexai import agent_engines

PROJECT_ID = "sejongclass"
LOCATION = "asia-northeast1"

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
)

# deployments = agent_engines.list()
#
# for deployment in deployments:
#     print(deployment)


DEPLOYMENT_ID = "projects/541371011875/locations/asia-northeast1/reasoningEngines/1634296491340201984"
remote_app = agent_engines.get(DEPLOYMENT_ID)

remote_session = remote_app.create_session(user_id="u_123")
print(remote_session)

SESSION_ID = "5742736587490328576"

for evnet in remote_app.stream_query(
        user_id="u_123",
        session_id=SESSION_ID,
        message="도쿄에 여행가려고 하는데 팁을 좀 줘."
):
    print(evnet, "\n", "=" * 50)


remote_app.delete(force=True)