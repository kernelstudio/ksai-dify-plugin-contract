# coding=utf-8
# -*- coding: UTF-8 -*-
#
# This file is part of the kernelstudio package.
#
# (c) 2014-2025 zlin <admin@kernelstudio.com>
#
# For the full copyright and license information, please view the LICENSE file
# that was distributed with this source code.


def format_contract_extractor_prompt(instruction: str, text: str) -> str:
    prompts = f"""<|im_start|>system
你是一个专业的合同解析助手，需要准确提取合同关键信息.<|im_end|>
<|im_start|>user
{instruction}
合同文本：{text}<|im_end|>
<|im_start|>assistant
"""
    return prompts
