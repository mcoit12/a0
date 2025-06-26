from python.helpers.extension import Extension
from agent import LoopData
from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage
from python.helpers import extract_tools

class AutoformatResponse(Extension):
    async def execute(self, message: str = "", loop_data: LoopData = LoopData(), **kwargs):
        if not message:
            return None
        system = self.agent.read_prompt("fw.msg_autoformat.md", original_response=message)
        try:
            response = await self.agent.call_utility_model(system, message)
        except Exception:
            return None
        try:
            return extract_tools.json_parse_dirty(response)
        except Exception:
            return None
