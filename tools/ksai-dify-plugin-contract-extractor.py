import logging
from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from ksai.contract.extractor import contract_content_extractor

logger = logging.getLogger(__name__)


class KsaiDifyPluginContractExtractorTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        ollama_host = self.runtime.credentials['ollama_host']
        extractor_model = self.runtime.credentials['extractor_model']

        rules = tool_parameters['rules']
        if rules is None or rules == '':
            rules = self.runtime.credentials['extractor_rules']
        tool_parameters['rules'] = rules

        response = contract_content_extractor(ollama_host, extractor_model, tool_parameters)
        yield self.create_text_message(response)
