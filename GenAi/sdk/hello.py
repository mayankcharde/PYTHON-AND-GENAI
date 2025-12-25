from dotenv import load_dotenv

from agents import Agent, Runner


load_dotenv()


#  DEFINE AN AGENT 
hello_agent = Agent[Any](
    name = "Hello world agent",
    instructions = "You are an agent which greets the user and helps tehm ans using emojis and in funny way"
)


result = Runner.run_sync(hello_agent,"Hey there , my name is mayank charde")

print(result.final_output)